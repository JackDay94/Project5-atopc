from django.shortcuts import render, get_object_or_404, reverse, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.db.models import Q
from django.db.models.functions import Lower

from .models import Product, Category, Review
from .forms import ReviewForm, ProductForm


def all_products(request):
    """
    A view to show all products, including sorting and search queries.
    From CI Boutique Ado Walkthrough.
    Modified for rating sorting and category search queries.
    """

    products = Product.objects.all()
    query = None
    categories = None
    sort = None
    direction = None

    if request.GET:
        if 'sort' in request.GET:
            sortkey = request.GET['sort']
            sort = sortkey
            if sortkey == 'name':
                sortkey = 'lower_name'
                products = products.annotate(lower_name=Lower('name'))
            if sortkey == 'category':
                sortkey = 'category__name'

            if 'direction' in request.GET:
                direction = request.GET['direction']
                if direction == 'desc':
                    sortkey = f'-{sortkey}'
            products = products.order_by(sortkey)

        if 'category' in request.GET:
            categories = request.GET['category'].split(',')
            products = products.filter(category__name__in=categories)
            categories = Category.objects.filter(name__in=categories)

        if 'q' in request.GET:
            query = request.GET['q']
            if not query:
                messages.error(
                    request, "You didn't enter any search criteria!"
                    )
                return redirect(reverse('products'))

            queries = (
                Q(name__icontains=query) |
                Q(description__icontains=query) |
                Q(category__name__icontains=query)
            )
            products = products.filter(queries)

    current_sorting = f'{sort}_{direction}'

    context = {
        'products': products,
        'search_term': query,
        'current_categories': categories,
        'current_sorting': current_sorting,
    }

    return render(request, 'products/products.html', context)


def product_detail(request, product_id):
    """
    A view to show individual product details and display
    customer reviews.
    From CI Boutique Ado Walkthrough.
    Modified to include customer reviews.
    """

    product = get_object_or_404(Product, pk=product_id)
    reviews = Review.objects.filter(product_id=product.id)

    if request.method == 'POST':
        if 'review-submit' in request.POST:
            review_form = ReviewForm(request.POST)
            if review_form.is_valid():
                model = Review()
                model.review_content = review_form.cleaned_data[
                    'review_content']
                model.rating = review_form.cleaned_data['rating']
                model.author = request.user
                model.product = product
                model.user_id = request.user.id
                model.save()
                messages.success(request, 'Your Review has been added!')
                return redirect(reverse('product_detail', args=[product.id]))
            else:
                messages.error(
                    request, 'Error! Your review was not submitted.'
                    )
                return redirect(reverse('product_detail', args=[product.id]))
    else:
        review_form = ReviewForm()

    context = {
        'product': product,
        'reviews': reviews,
        'review_form': ReviewForm(),
    }

    return render(request, 'products/product_detail.html', context)


@login_required
def add_product(request):
    """
    A view to add a product to the store.
    From CI Boutique Ado walkthrough.
    """

    if not request.user.is_superuser:
        messages.error(request, 'Sorry only store owners can do that.')
        return redirect(reverse('home'))

    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            product = form.save()
            messages.success(request, 'Successfully added product!')
            return redirect(reverse('product_detail', args=[product.id]))
        else:
            messages.error(request, (
                'Failed to add product! Please check the form is valid.'
                ))
    else:
        form = ProductForm()

    template = 'products/add_product.html'
    context = {
        'form': form,
    }

    return render(request, template, context)


@login_required
def edit_product(request, product_id):
    """
    A view to edit a product in the store.
    From CI Boutique Ado walkthrough.
    """

    if not request.user.is_superuser:
        messages.error(request, 'Sorry only store owners can do that.')
        return redirect(reverse('home'))

    product = get_object_or_404(Product, pk=product_id)
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES, instance=product)
        if form.is_valid():
            form.save()
            messages.success(request, 'Successfully updated product!')
            return redirect(reverse('product_detail', args=[product.id]))
        else:
            messages.error(request, (
                'Failed to update product! Please check the form is valid.'
                ))
    else:
        form = ProductForm(instance=product)
        messages.info(request, f'You are editing {product.name}')

    template = 'products/edit_product.html'
    context = {
        'form': form,
        'product': product,
    }

    return render(request, template, context)


@login_required
def delete_product(request, product_id):
    """
    A view to delete a product from the store.
    Modified from Boutique Ado walkthrough.
    """

    if not request.user.is_superuser:
        messages.error(request, 'Sorry only store owners can do that.')
        return redirect(reverse('home'))

    product = get_object_or_404(Product, pk=product_id)

    if request.method == 'POST':
        product.delete()
        messages.success(request, 'Successfully deleted product!')
        return redirect(reverse('home'))
    else:
        messages.info(request, f'You are about to delete {product.name}')

    template = 'products/delete_product.html'
    context = {
        'product': product
    }

    return render(request, template, context)


@login_required
def edit_review(request, review_id):
    """
    A view to edit an existing product review.
    """

    review = get_object_or_404(Review, pk=review_id)
    product = review.product

    if not request.user == review.author and not request.user.is_superuser:
        messages.error(
            request, 'Sorry, you do not have permission to access this.'
            )
        return redirect(reverse('product_detail', args=[product.id]))

    if request.method == 'POST':
        form = ReviewForm(request.POST, instance=review)
        if form.is_valid():
            form.save()
            messages.success(request, 'Successfully updated review!')
            return redirect(reverse('product_detail', args=[product.id]))
        else:
            messages.error(request, (
                'Failed to update review! Please check the form is valid.'
                ))
    else:
        form = ReviewForm(instance=review)
        messages.info(
            request, f'You are editing your review for {product.name}'
            )

    template = 'products/edit_review.html'
    context = {
        'review_form': form,
        'product': product,
        'review': review,
    }

    return render(request, template, context)


@login_required
def delete_review(request, review_id):
    """
    A view to delete an existing product review.
    """

    review = get_object_or_404(Review, pk=review_id)
    product = review.product

    if not request.user == review.author and not request.user.is_superuser:
        messages.error(
            request, 'Sorry, you do not have permission to access this.'
            )
        return redirect(reverse('product_detail', args=[product.id]))

    if request.method == 'POST':
        review.delete()
        messages.success(request, 'Successfully deleted review!')
        return redirect(reverse('product_detail', args=[product.id]))
    else:
        messages.info(
            request, f'You are about to delete your review for {product.name}'
            )

    template = 'products/delete_review.html'
    context = {
        'product': product,
        'review': review,
    }

    return render(request, template, context)
