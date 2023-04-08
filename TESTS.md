<h1 align="center">Manual Testing</h1>

## Contents
1. [Navigation](#navigation)
2. [Home page](#home-page)
3. [Products page](#products-page)
4. [Product detail page](#product-detail-page)
5. [Add product page](#add-product-page)
6. [Edit product page](#edit-product-page)
7. [Delete product page](#delete-product-page)
8. [Edit review page](#edit-review-page)
9. [Delete review page](#delete-review-page)
10. [Bag page](#bag-page)
11. [Checkout page](#checkout-page)
12. [Checkout success page](#checkout-success-page)
13. [Profile page](#profile-page)
14. [Wishlist page](#wishlist-page)
15. [Newsletter page](#newsletter-page)
16. 

## Navigation

| Test                                  | Action          | Expected result                                                                      | Result |
|---------------------------------------|-----------------|--------------------------------------------------------------------------------------|--------|
| Navbar Home                           | Click link      | Go to home page                                                                      | Pass   |
| Navbar logo                           | Click logo      | Go to home page                                                                      | Pass   |
| Navbar Wishlist Signed out            | Click link      | Redirect to sign In page                                                             | Pass   |
| Navbar Wishlist Signed In             | Click link      | Go to Wishlist page                                                                  | Pass   |
| Navbar Account Signed out             | Click dropdown  | Only Sign In and Register visible                                                    | Pass   |
| Navbar Account Signed In              | Click dropdown  | Only My profile, Change password and Sign out visible                                | Pass   |
| Navbar Account Superuser              | Click dropdown  | Admin, Add Product, My profile, Change password and Sign out visible                 | Pass   |
| Account dropdown Sign In              | Click link      | Go to Sign In page                                                                   | Pass   |
| Account dropdown Register             | Click link      | Go to Register page                                                                  | Pass   |
| Account dropdown Sign out             | Click link      | Go to Sign out page                                                                  | Pass   |
| Account dropdown My profile           | Click link      | Go to profile page                                                                   | Pass   |
| Account dropdown Change password      | Click link      | Go to change password page                                                           | Pass   |
| Account dropdown Admin                | Click link      | Go to Admin panel                                                                    | Pass   |
| Bag                                   | Click link      | Go to bag page                                                                       | Pass   |
| Bag no items                          | No items added  | Bag colour is black and 'Bag' displayed under bag icon                               | Pass   |
| Bag has items                         | Items in bag    | Bag colour is blue and grand total of bag items displayed under bag                  | Pass   |
| All products dropdown                 | Click dropdown  | By Price, By Rating, By Category and All products links viisble                      | Pass   |
| All products dropdown By Price        | Click link      | Go to all products sorted by price page                                              | Pass   |
| All products dropdown By Rating       | Click link      | Go to all products sorted by rating page                                             | Pass   |
| All products dropdown By Category     | Click link      | Go to all products sorted by category page                                           | Pass   |
| All products dropdown All Products    | Click link      | Go to all products page                                                              | Pass   |
| Peripherals dropdown                  | Click dropdown  | Keyboards, Headphones, Mice and All Peripherals links visible                        | Pass   |
| Peripherals dropdown Keyboards        | Click link      | Go to products filtered by keyboards category page                                   | Pass   |
| Peripherals dropdown Headphones       | Click link      | Go to products filtered by headphones category page                                  | Pass   |
| Peripherals dropdown Mice             | Click link      | Go to products filtered by Mice category page                                        | Pass   |
| Peripherals dropdown All peripherals  | Click link      | Go to products filtered by keyboards, headphones and mice categories page            | Pass   |
| Monitors dropdown                     | Click dropdown  | 1080p, 1440p, 4k and All Monitors links visible                                      | Pass   |
| Monitors dropdown 1080p               | Click link      | Go to products filtered by 1080p category page                                       | Pass   |
| Monitors dropdown 1440p               | Click link      | Go to products filtered by 1440p category page                                       | Pass   |
| Monitors dropdown 4k                  | Click link      | Go to products filtered by 4k category page                                          | Pass   |
| Monitors dropdown All Monitors        | Click link      | Go to products filtered by 1080p, 1440p and 4k categories page                       | Pass   |
| Storage dropdown                      | Click dropdown  | Hard drives, Solid state drives and All storage links visible                        | Pass   |
| Storage dropdown Hard drives          | Click link      | Go to products filtered by Hard drives category page                                 | Pass   |
| Storage dropdown Solid state drives   | Click link      | Go to products filtered by Solid state drives category page                          | Pass   |
| Storage dropdown All Storage          | Click link      | Go to products filtered by Hard drives and Solid state drives categories page        | Pass   |
| Deals dropdown                        | Click dropdown  | Latest Deals, Clearance and All Deals links visible                                  | Pass   |
| Deals dropdown Latest deals           | Click link      | Go to products filtered by Latest deals category page                                | Pass   |
| Deals dropdown Clearance              | Click link      | Go to products filtered by Clearance category page                                   | Pass   |
| Deals dropdown All deals              | Click link      | Go to products filtered by Latest deals and Clearance categories page                | Pass   |
| Search bar                            | Search          | Go to products page with products filtered by search query                           | Pass   |
| Navbar small screen                   | View on phone   | Navbar and logo collapses to menu icon and search bar collapses to search icon       | Pass   |
| Search icon small screen              | Click icon      | Expands the search bar below the nav icons                                           | Pass   |
| Navbar small screen menu              | Click menu icon | Expands to offcanvas navbar from the left side of the screen                         | Pass   |
| Offcanvas Navbar                      | Click 'x'       | Collapses the offcanvas navbar                                                       | Pass   |
| Footer Facebook icon                  | Click icon      | Go to Facebook in a new tab                                                          | Pass   |
| Footer Twitter icon                   | Click icon      | Go to Twitter in a new tab                                                           | Pass   |
| Footer Youtube icon                   | Click icon      | Go to Youtube in a new tab                                                           | Pass   |
| Footer Instagram icon                 | Click icon      | Go to instagram in a new tab                                                         | Pass   |
| Footer Information Signed out         | Visual check    | Only About us, Blog and Privacy policy links visible                                 | Pass   |
| Footer Information Signed In          | Visual check    | Only My Profile, About us, Blog and Privacy policy links visible                     | Pass   |
| Footer Information Superuser          | Visual check    | Admin, My Profile, About us, Blog and Privacy policy links visible                   | Pass   |
| Footer Information About us           | Click link      | Go to About us page                                                                  | Pass   |
| Footer Information Blog               | Click link      | Go to Blog page                                                                      | Pass   |
| Footer Information Privacy policy     | Click link      | Go to Privacy policy page                                                            | Pass   |
| Footer Information My Profile         | Click link      | Go to Profile page                                                                   | Pass   |
| Footer Information Admin              | Click link      | Go to Admin panel                                                                    | Pass   |
| Footer Newsletter Sign up             | Click link      | Go to Newsletter page                                                                | Pass   |

## Home Page

| Test                                  | Action          | Expected result                                                                      | Result |
|---------------------------------------|-----------------|--------------------------------------------------------------------------------------|--------|
| Home splash image                     | Click image     | Go to products filtered by Latest deals and Clearance categories page                | Pass   |
| New In Store List                     | Visual check    | 4 Newest products added displayed                                                    | Pass   |
| Top Peripherals list                  | Visual check    | 4 highest rated peripherals displayed                                                | Pass   |
| Top Monitors list                     | Visual check    | 4 highest rated monitors displayed                                                   | Pass   |
| Top Storage list                      | Visual check    | 4 highest rated storage displayed                                                    | Pass   |
| Blog list                             | Visual check    | 4 Latest blog posts displayed                                                        | Pass   |
| Explore More button                   | Click button    | Go to Blog page                                                                      | Pass   |
| Product preview                       | Visual check    | Product image, name, price, rating, category and 'add to basket' displayed           | Pass   |
| Product preview                       | Click image     | Go to product detail page of product                                                 | Pass   |
| Product preview                       | Click category  | Go to products filtered by relevant category page                                    | Pass   |
| Product preview                       | Click add to bag| Adds 1 of the product to bag and display success message with bag preview            | Pass   |
| Product preview superuser             | Visual check    | Edit and Delete links displayed above 'add to basket'                                | Pass   |
| Product preview superuser edit        | Click link      | Go to edit product page for relevant product                                         | Pass   |
| Product preview superuser delete      | Click link      | Go to delete product page for relevant product                                       | Pass   |
| Blog post preview                     | Visual check    | Blog post image, title, subtitle and 'view post' displayed                           | Pass   |
| Blog post preview                     | Click image     | Go to Blog post page of the relevant post                                            | Pass   |
| Blog post preview                     | Click button    | Go to Blog post page of the relevant post                                            | Pass   |
| Blog post preview superuser           | Visual check    | Edit and delete links displayed above 'view post'                                    | Pass   |
| Blog post preview superuser edit      | Click link      | Go to edit blog post page for relevant post                                          | Pass   |
| Blog post preview superuser delete    | Click link      | Go to delete blog post page for relevant post                                        | Pass   |

## Products Page

| Test                                  | Action          | Expected result                                                                      | Result |
|---------------------------------------|-----------------|--------------------------------------------------------------------------------------|--------|
| Products list                         | Visual check    | Products displayed in list correctly                                                 | Pass   |
| Sort Selector                         | Select option   | Products sorted correctly by sorting option                                          | Pass   |
| Product preview                       | Visual check    | Product image, name, price, rating, category and 'add to basket' displayed           | Pass   |
| Product preview                       | Click image     | Go to product detail page of product                                                 | Pass   |
| Product preview                       | Click category  | Go to products filtered by relevant category page                                    | Pass   |
| Product preview                       | Click add to bag| Adds 1 of the product to bag and display success message with bag preview                             | Pass   |
| Product preview superuser             | Visual check    | Edit and Delete links displayed above 'add to basket'                                | Pass   |
| Product preview superuser edit        | Click link      | Go to edit product page for relevant product                                         | Pass   |
| Product preview superuser delete      | Click link      | Go to delete product page for relevant product                                       | Pass   |
| Products list filtered                | Visual check    | Filtered product list displayed and category badge displayed at top                  | Pass   |
| Category badge                        | Click link      | Go to product page filtered by relevant category                                     | Pass   |
| Products Home                         | Click link      | Go to all products page                                                              | Pass   |
| Products list                         | No products     | Display text informing user no products found                                        | Pass   |
| Back to top button                    | Click button    | Scroll back to the top of page                                                       | Pass   |

## Product Detail Page

| Test                                  | Action                                | Expected result                                                                      | Result |
|---------------------------------------|---------------------------------------|--------------------------------------------------------------------------------------|--------|
| Product Details                       | Visual check                          | Product image, name, sku, rating, price, category and description displayed          | Pass   |
| Product Details Superuser             | Visual check                          | Edit and delete links displayed next to product rating                               | Pass   |
| Product Details superuser edit        | Click link                            | Go to edit product page for relevant product                                         | Pass   |
| Product Details superuser delete      | Click link                            | Go to delete product page for relevant product                                       | Pass   |
| Product Image                         | Click image                           | Opens the product image in a new tab                                                 | Pass   |
| Product category                      | Click link                            | Go to Products page filtered by relevant product category                            | Pass   |
| Quantity Input                        | Click '+'                             | Quantity increases by 1                                                              | Pass   |
| Quantity Input                        | Click '-'                             | Quantity decreases by 1                                                              | Pass   |
| Quantity Input                        | Enter quantity                        | Quantity changed to the inputted number                                              | Pass   |
| Quantity Input                        | Non-number input                      | Message displayed asking to enter a number                                           | Pass   |
| Quantity Input                        | Quantity at 1                         | Decrease quantity button disabled                                                    | Pass   |
| Quantity Input                        | Quantity at 99                        | Increase quantity button disabled                                                    | Pass   |
| Quantity Input                        | Quantity < 1                          | Message displayed asking quantity to be no less than 1                               | Pass   |
| Quantity Input                        | Quantity > 99                         | Message displayed asking quantity to be no more than 99                              | Pass   |
| Add to Bag                            | Click button                          | Add product with quantity to bag and display success message with bag preview        | Pass   |
| Wishlist Sign In                      | Click button                          | Add product to user wishlist, redirect to wishlist and display success message       | Pass   |
| Wishlist Product on wishlist          | Click button                          | Remove product from user wishlist, redirect to wishlist and display success message  | Pass   |
| Wishlist Sign Out                     | Click button                          | Redirect to sign In page                                                             | Pass   |
| Product reviews                       | Visual check                          | Reviews for the product show author, rating, created date, edited date and content   | Pass   |
| Product reviews                       | Visual check                          | Total number of reviews for the product displayed                                    | Pass   |
| Review form                           | Visual check                          | Product review form displayed to authenticated users                                 | Pass   |
| Review form                           | Submit review form without content    | Form not submitted and message displayed asking to fill in relevant fields           | Pass   |
| Review form                           | Submit review form with content       | Form submitted and success message displayed, page reloaded, ratings updated         | Pass   |
| Review buttons                        | Visual check                          | Edit and delete links only visible to review author and superusers                   | Pass   |
| Review edit                           | Click link                            | Go to edit review page for relevant review                                           | Pass   |
| Review delete                         | Click link                            | Go to delete review page for relevant review                                         | Pass   |

## Add Product Page

| Test                                  | Action                  | Expected result                                                                                                 | Result |
|---------------------------------------|-------------------------|-----------------------------------------------------------------------------------------------------------------|--------|
| Add Product form                      | Visual check            | Add product form displayed                                                                                      | Pass   |
| Add Product form                      | Submit empty form       | Form does not submit and message displayed asking to fill in required fields                                    | Pass   |
| Add Product form                      | Submit invalid data     | Form does not submit and message displayed to correct invalid fields                                            | Pass   |
| Add Product form                      | Submit only name        | Form does not submit and message displayed asking to fill in required fields                                    | Pass   |
| Add Product form                      | Submit name and price   | Form does not submit and message displayed asking to fill in required fields                                    | Pass   |
| Add Product form                      | Submit required fields  | Form submits and user redirected to new product page with success message. Product added to Products model      | Pass   |
| Add Product form                      | Click select image      | User is asked to select an image file to upload an image                                                        | Pass   |
| Add Product form                      | Submit no Image         | Product is given a placeholder image                                                                            | Pass   |
| Cancel                                | Click button            | User is redirected to the all products page                                                                     | Pass   |

## Edit Product Page

| Test                                  | Action                  | Expected result                                                                                                 | Result |
|---------------------------------------|-------------------------|-----------------------------------------------------------------------------------------------------------------|--------|
| Alert Message                         | Visual check            | Alert message is displayed to user on entering page informing them of the product they are editing              | Pass   |
| Edit Product form                     | Visual check            | Edit product form displayed                                                                                     | Pass   |
| Edit Product form                     | Product data loaded     | Form is pre-populated with the data of the product                                                              | Pass   |
| Edit Product form                     | Submit empty form       | Form does not submit and message displayed asking to fill in required fields                                    | Pass   |
| Edit Product form                     | Submit invalid data     | Form does not submit and message displayed to correct invalid fields                                            | Pass   |
| Edit Product form                     | Submit only name        | Form does not submit and message displayed asking to fill in required fields                                    | Pass   |
| Edit Product form                     | Submit name and price   | Form does not submit and message displayed asking to fill in required fields                                    | Pass   |
| Edit Product form                     | Submit required fields  | Form submits and user redirected to product page with success message. Product updated in Products model        | Pass   |
| Edit Product form                     | Current image displayed | Form displays the current product image if it has one                                                           | Pass   |
| Edit Product form                     | Click select image      | User is asked to select an image file to upload an image                                                        | Pass   |
| Edit Product form                     | Submit no Image         | Product is given a placeholder image                                                                            | Pass   |
| Cancel                                | Click button            | User is redirected to the relevant product page                                                                 | Pass   |

## Delete Product Page

| Test                                  | Action                  | Expected result                                                                                                 | Result |
|---------------------------------------|-------------------------|-----------------------------------------------------------------------------------------------------------------|--------|
| Alert Message                         | Visual check            | Alert message is displayed to user on entering page informing them of the product they are deleting             | Pass   |
| Product Details                       | Visual check            | Product image, name, sku, price, category, rating and description displayed                                     | Pass   |
| Delete                                | Click button            | Product is deleted from the store and products model, user redirected to home with success message              | Pass   |
| Cancel                                | Click button            | User is redirected to the relevant product page                                                                 | Pass   |

## Edit Review Page

| Test                                  | Action                  | Expected result                                                                                                                                            | Result |
|---------------------------------------|-------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------|--------|
| Alert Message                         | Visual check            | Alert message is displayed to user on entering page informing them of the review they are editing                                                          | Pass   |
| Edit Review form                      | Visual check            | Edit review form displayed                                                                                                                                 | Pass   |
| Edit Review form                      | Review data loaded      | Form is pre-populated with the data of the review                                                                                                          | Pass   |
| Edit Review form                      | Submit empty form       | Form does not submit and message displayed asking to fill in required fields                                                                               | Pass   |
| Edit Review form                      | Submit required fields  | Form submits and user redirected to product page with success message. Review updated in Reviews model and 'edited on' value changed to current time       | Pass   |
| Cancel                                | Click button            | User is redirected to the relevant product page                                                                                                            | Pass   |

## Delete Review Page

| Test                                  | Action                  | Expected result                                                                                                                                            | Result |
|---------------------------------------|-------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------|--------|
| Alert Message                         | Visual check            | Alert message is displayed to user on entering page informing them of the review they are deleting                                                         | Pass   |
| Review details                        | Visual check            | Review content for the related product are displayed                                                                                                       | Pass   |
| Delete                                | Click button            | Review is deleted from the store and Reviews model, user redirected to product page with success message, product rating is updated                        | Pass   |
| Cancel                                | Click button            | User is redirected to the relevant product page                                                                                                            | Pass   |

## Bag Page

| Test                                  | Action                  | Expected result                                                                                                                                            | Result |
|---------------------------------------|-------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------|--------|
| Empty bag                             | Visual check            | User informed bag is empty and button to keep shopping displayed                                                                                           | Pass   |
| Keep shopping                         | Click button            | Go to all products page                                                                                                                                    | Pass   |
| Bag has items                         | Visual check            | Products that were added to bag are displayed correctly                                                                                                    | Pass   |
| Product Image                         | Click image             | Go to relevant product page                                                                                                                                | Pass   |
| Product Name                          | Click link              | Go to relevant product page                                                                                                                                | Pass   |
| Quantity Input                        | Visual check            | Initial product quantity same as what was set outside of the bag page                                                                                      | Pass   |
| Quantity Input                        | Click '+'               | Quantity increases by 1                                                                                                                                    | Pass   |
| Quantity Input                        | Click '-'               | Quantity decreases by 1                                                                                                                                    | Pass   |
| Quantity Input                        | Enter quantity          | Quantity changed to the inputted number                                                                                                                    | Pass   |
| Quantity Input                        | Non-number input        | Message displayed asking to enter a number                                                                                                                 | Pass   |
| Quantity Input                        | Quantity at 1           | Decrease quantity button disabled                                                                                                                          | Pass   |
| Quantity Input                        | Quantity at 99          | Increase quantity button disabled                                                                                                                          | Pass   |
| Quantity Input                        | Quantity < 1            | Product is removed from bag with success message displayed                                                                                                 | Pass   |
| Quantity Input                        | Quantity > 99           | Message displayed asking quantity to be no more than 99                                                                                                    | Pass   |
| Quantity Input Update                 | Click button            | Updates the quantity to selected input and reloads page with success message                                                                               | Pass   |
| Quantity Input Remove                 | Click button            | Removes the product from the bag and reloads the page with success message                                                                                 | Pass   |
| Bag Total                             | Visual check            | Bag total is the correct amount for items in the bag                                                                                                       | Pass   |
| Delivery Total                        | Visual check            | Delivery total is the correct amount for items in the bag, 0 if bag total is > 100                                                                         | Pass   |
| Grand Total                           | Visual check            | Grand total is the correct amount for items in the bag                                                                                                     | Pass   |
| Secure Checkout                       | Click button            | Go to checkout page                                                                                                                                        | Pass   |

## Checkout Page

| Test                                  | Action                                | Expected result                                                                                                                                            | Result |
|---------------------------------------|---------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------|--------|
| Order Summary                         | Visual check                          | Bag items displayed correctly with correct order total, delivery total and grand total                                                                     | Pass   |
| Order Form                            | Visual check                          | Order Form displayed correctly                                                                                                                             | Pass   |
| Order Form Saved details              | Visual check                          | Order Form displayed correctly with fields pre-populated with saved details                                                                                | Pass   |
| Order Form Signed In                  | Visual check                          | Checkbox to save delivery information to profile visible                                                                                                   | Pass   |
| Order Form Signed Out                 | Visual check                          | Create an account and login links displayed instead of checkbox                                                                                            | Pass   |
| Order Form                            | Submit empty form                     | Form does not submit and message displayed asking to fill in required fields                                                                               | Pass   |
| Order Form                            | Submit invalid data                   | Form does not submit and message displayed to correct invalid fields                                                                                       | Pass   |
| Order Form                            | Submit required fields no payment     | Form does not submit and message displayed to complete payment field                                                                                       | Pass   |
| Stripe Payment                        | Invalid Card                          | Message displays asking for correct details                                                                                                                | Pass   |
| Stripe Payment                        | Valid Card                            | No error message for payment field                                                                                                                         | Pass   |
| Order Form                            | Submit required fields valid payment  | Loading overlay displayed and user redirected to checkout success page with success message, Order model updated                                           | Pass   |

## Checkout Success Page

| Test                                  | Action                                | Expected result                                                                                                                                            | Result |
|---------------------------------------|---------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------|--------|
| Order Information                     | Visual check                          | Order Information is displayed correctly for the items purchased                                                                                           | Pass   |
| Confirmation Email                    | Email Sent                            | Order Confirmation email correctly sent to the email supplied on the order                                                                                 | Pass   |
| Latest deals                          | Click button                          | Go to products filtered by Latest deals and Clearance categories page                                                                                      | Pass   |

## Profile Page

| Test                                  | Action                                | Expected result                                                                                                                                            | Result |
|---------------------------------------|---------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------|--------|
| Profile Form                          | Visual check                          | Profile Form displayed correctly                                                                                                                           | Pass   |
| Profile Form Saved details            | Visual check                          | Profile Form displayed correctly with fields pre-populated with saved details                                                                              | Pass   |
| Update details                        | Click button                          | Updates the user profile with the data filled in the profile form, reloads page with success message and updates the profile model                         | Pass   |
| Order History                         | Visual check                          | Past orders displayed correctly with order number, date, items and order total                                                                             | Pass   |
| Order History Order Number            | Click link                            | Go to order history page for the relevant order number and display alert message informing user they are looking at a past order                           | Pass   |
| Order History Item name               | Click link                            | Go to relevant product page                                                                                                                                | Pass   |

## Wishlist Page

| Test                                  | Action                  | Expected result                                                                                                                                            | Result |
|---------------------------------------|-------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------|--------|
| Empty wishlist                        | Visual check            | User informed their wishlist is empty and button to explore the store displayed                                                                            | Pass   |
| Explore store                         | Click button            | Go to all products page                                                                                                                                    | Pass   |
| Wishlist has items                    | Visual check            | Products that were added to wishlist are displayed correctly                                                                                               | Pass   |
| Product Image                         | Click image             | Go to relevant product page                                                                                                                                | Pass   |
| Product Name                          | Click link              | Go to relevant product page                                                                                                                                | Pass   |
| Add to Bag                            | Click button            | Add product to bag and display success message with bag preview                                                                                            | Pass   |
| Remove                                | Click button            | Remove the product from the wishlist, reload the page and display a success message                                                                        | Pass   |

## Newsletter Page

| Test                                  | Action                                | Expected result                                                                                                                                            | Result |
|---------------------------------------|---------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------|--------|
| Newsletter Form                       | Visual check                          | Newsletter Form displayed correctly                                                                                                                        | Pass   |
| Newsletter Form                       | Submit empty form                     | Form does not submit and message displayed asking to fill in required fields                                                                               | Pass   |
| Newsletter Form                       | Submit invalid data                   | Form does not submit and message displayed to correct invalid fields                                                                                       | Pass   |
| Newsletter Form                       | Submit duplicate email                | Form does not submit, page reloads and error message displayed                                                                                             | Pass   |
| Newsletter Form                       | Submit valid data                     | Form submits, page reloads and success message displayed. Newsletter model updates                                                                         | Pass   |
| Go Back Home                          | Click button                          | Go to Home page                                                                                                                                            | Pass   |

## Blog Page

| Test                                  | Action          | Expected result                                                                      | Result |
|---------------------------------------|-----------------|--------------------------------------------------------------------------------------|--------|
| Blog post list                        | Visual check    | Published Blog posts displayed in list correctly                                     | Pass   |
| Blog post list superuser              | Visual check    | Add Post button at top of page                                                       | Pass   |
| Add Post                              | Click button    | Go to add blog post page                                                             | Pass   |
| Pagination                            | Click page link | Go between pages of blog posts                                                       | Pass   |
| Blog post preview                     | Visual check    | Blog post image, title, subtitle and 'view post' displayed                           | Pass   |
| Blog post preview                     | Click image     | Go to Blog post page of the relevant post                                            | Pass   |
| Blog post preview                     | Click button    | Go to Blog post page of the relevant post                                            | Pass   |
| Blog post preview superuser           | Visual check    | Edit and delete links displayed above 'view post'                                    | Pass   |
| Blog post preview superuser edit      | Click link      | Go to edit blog post page for relevant post                                          | Pass   |
| Blog post preview superuser delete    | Click link      | Go to delete blog post page for relevant post                                        | Pass   |

## Blog Post Page

| Test                                  | Action                                | Expected result                                                                      | Result |
|---------------------------------------|---------------------------------------|--------------------------------------------------------------------------------------|--------|
| Blog Post Details                     | Visual check                          | Post image, title, subtitle, author, date_created, date_edited and content displayed | Pass   |
| Blog Post Details Superuser           | Visual check                          | Edit and delete links displayed below post image                                     | Pass   |
| Product Details superuser edit        | Click link                            | Go to edit post page for relevant post                                               | Pass   |
| Product Details superuser delete      | Click link                            | Go to delete post page for relevant post                                             | Pass   |
| Post Comments                         | Visual check                          | Comments for the post show author,created date, edited date and content              | Pass   |
| Comment form                          | Visual check                          | Post comment form displayed to authenticated users                                   | Pass   |
| Comment form                          | Submit comment form without content   | Form not submitted and message displayed asking to fill in relevant fields           | Pass   |
| Comment form                          | Submit review form with content       | Form submitted and success message displayed, page reloaded, Comment model updated   | Pass   |
| Comment buttons                       | Visual check                          | Edit and delete links only visible to comment author and superusers                  | Pass   |
| Comment edit                          | Click link                            | Go to edit review page for relevant review                                           | Pass   |
| Comment delete                        | Click link                            | Go to delete review page for relevant review                                         | Pass   |

## Add Blog Post page

| Test                                  | Action                                    | Expected result                                                                                                 | Result |
|---------------------------------------|-------------------------------------------|-----------------------------------------------------------------------------------------------------------------|--------|
| Add Blog post form                    | Visual check                              | Add blog post form displayed                                                                                    | Pass   |
| Add Blog post form                    | Submit empty form                         | Form does not submit and message displayed asking to fill in required fields                                    | Pass   |
| Add Blog post form                    | Submit invalid data                       | Form does not submit, error message displayed and redirected to blog post list                                  | Pass   |
| Add Blog post form                    | Submit valid data status published        | Form submits, success message displayed and redirected to the blog post. Blog post model updated                | Pass   |
| Add Blog post form                    | Submit valid data status draft            | Form submits, success message displayed and redirected to the blog list. Blog post model updated                | Pass   |
| Add Blog post form                    | Submit with no image                      | Form submits and image is set to placeholder image                                                              | Pass   |
| Add Blog post form                    | Click select image                        | User is asked to select an image file to upload an image                                                        | Pass   |
| Cancel                                | Click button                              | User is redirected to the Blog list page                                                                        | Pass   |

## Edit Blog Post page

| Test                                  | Action                                    | Expected result                                                                                                 | Result |
|---------------------------------------|-------------------------------------------|-----------------------------------------------------------------------------------------------------------------|--------|
| Alert Message                         | Visual check                              | Alert message is displayed to user on entering page informing them of the post they are editing                 | Pass   |
| Edit Post form                        | Visual check                              | Edit post form displayed                                                                                        | Pass   |
| Edit Post form                        | Post data loaded                          | Form is pre-populated with the data of the post                                                                 | Pass   |
| Edit Post form                        | Submit empty form                         | Form does not submit and message displayed asking to fill in required fields                                    | Pass   |
| Edit Post form                        | Submit invalid data                       | Form does not submit and message displayed to correct invalid fields                                            | Pass   |
| Edit Post form                        | Submit valid data status published        | Form submits, success message displayed and redirected to the blog post. Blog post model updated                | Pass   |
| Edit Post form                        | Submit valid data status draft            | Form submits, success message displayed and redirected to the blog list. Blog post model updated                | Pass   |
| Edit Post form                        | Current image displayed                   | Form displays the current post image if it has one                                                              | Pass   |
| Edit Post form                        | Click select image                        | User is asked to select an image file to upload an image                                                        | Pass   |
| Edit Post form                        | Submit no Image                           | Product is given a placeholder image                                                                            | Pass   |
| Cancel                                | Click button                              | User is redirected to the relevant product page                                                                 | Pass   |

## Delete Blog Post Page

| Test                                  | Action                  | Expected result                                                                                                 | Result |
|---------------------------------------|-------------------------|-----------------------------------------------------------------------------------------------------------------|--------|
| Alert Message                         | Visual check            | Alert message is displayed to user on entering page informing them of the post they are deleting                | Pass   |
| Post Details                          | Visual check            | Post image, title, subtitle, date created, date edited, author and content displayed                            | Pass   |
| Delete                                | Click button            | Post is deleted from the blog and blog posts model, user redirected to post list with success message           | Pass   |
| Cancel                                | Click button            | User is redirected to the relevant blog post                                                                    | Pass   |

## Edit Comment Page

| Test                                  | Action                  | Expected result                                                                                                                                            | Result |
|---------------------------------------|-------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------|--------|
| Alert Message                         | Visual check            | Alert message is displayed to user on entering page informing them of the comment they are editing                                                         | Pass   |
| Edit Comment form                     | Visual check            | Edit comment form displayed                                                                                                                                | Pass   |
| Edit Comment form                     | Comment data loaded     | Form is pre-populated with the data of the comment                                                                                                         | Pass   |
| Edit Comment form                     | Submit empty form       | Form does not submit and message displayed asking to fill in required fields                                                                               | Pass   |
| Edit Comment form                     | Submit required fields  | Form submits and user redirected to post page with success message. Comment updated in Blog Comments model and 'edited on' value changed to current time   | Pass   |
| Cancel                                | Click button            | User is redirected to the post list page                                                                                                                   | Pass   |

## Delete Comment Page

| Test                                  | Action                  | Expected result                                                                                                                                            | Result |
|---------------------------------------|-------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------|--------|
| Alert Message                         | Visual check            | Alert message is displayed to user on entering page informing them of the comment they are deleting                                                        | Pass   |
| Comment details                       | Visual check            | Comment content for the related post is displayed                                                                                                          | Pass   |
| Delete                                | Click button            | Comment is deleted from the post and Blog comments model, user redirected to post page with success message                                                | Pass   |
| Cancel                                | Click button            | User is redirected to the post list page                                                                                                                   | Pass   |

## Register Page

| Test                                  | Action                  | Expected result                                                                                                 | Result |
|---------------------------------------|-------------------------|-----------------------------------------------------------------------------------------------------------------|--------|
| Register Form                         | Visual check            | Register form shows email, email confirmation, username, password, password confirmation                        | Pass   |
| Register Form                         | Submit empty form       | Form does not submit and message displayed asking to fill in required fields                                    | Pass   |
| Register Form                         | Submit invalid form     | Form does not submit and message displayed to correct invalid fields                                            | Pass   |
| Register Form                         | Submit valid data       | User is redirected to confirm email page and confirmation email sent to their sign up email                     | Pass   |
| Verifies Email                        | User verifies email     | User email is given verified status and they can now sign in                                                    | Pass   |
| Sign In link                          | Click link              | Go to sign in page                                                                                              | Pass   |

## Sign In Page

| Test                                  | Action                  | Expected result                                                                                                 | Result |
|---------------------------------------|-------------------------|-----------------------------------------------------------------------------------------------------------------|--------|
| Sign in Form                          | Visual check            | Sign in form shows login and password fields                                                                    | Pass   |
| Sign in Form                          | Submit empty form       | Form does not submit and message displayed asking to fill in required fields                                    | Pass   |
| Sign in Form                          | Submit invalid form     | Form does not submit and message displayed to correct invalid fields                                            | Pass   |
| Sign in Form                          | Submit valid data       | User is logged into their account and redirected to home page with a success message                            | Pass   |
| Sign up link                          | Click link              | Go to Register page                                                                                             | Pass   |
| Forgotten password link               | Click link              | Go to password reset page                                                                                       | Pass   |

## Sign Out Page

| Test                                  | Action                  | Expected result                                                                                                 | Result |
|---------------------------------------|-------------------------|-----------------------------------------------------------------------------------------------------------------|--------|
| Sign out button                       | Click button            | User signed out of their account and redirected to the home page                                                | Pass   |
| Cancel button                         | Click button            | Go to Home page                                                                                                 | Pass   |

## Password reset Page

| Test                                  | Action                  | Expected result                                                                                                 | Result |
|---------------------------------------|-------------------------|-----------------------------------------------------------------------------------------------------------------|--------|
| Password reset form                   | Visual check            | Password reset form shows email field                                                                           | Pass   |
| Password reset Form                   | Submit empty form       | Form does not submit and message displayed asking to fill in required fields                                    | Pass   |
| Password reset Form                   | Submit invalid form     | Form does not submit and message displayed to correct invalid fields                                            | Pass   |
| Password reset Form                   | Submit valid data       | User is sent a password reset email to their registered email address                                           | Pass   |
| Back to login button                  | Click button            | Go to sign in page                                                                                              | Pass   |

## Change Password Page

| Test                                  | Action                  | Expected result                                                                                                 | Result |
|---------------------------------------|-------------------------|-----------------------------------------------------------------------------------------------------------------|--------|
| Change password Form                  | Visual check            | Change Password form shows current password, new password and new password (again) fields                       | Pass   |
| Change password Form                  | Submit empty form       | Form does not submit and message displayed asking to fill in required fields                                    | Pass   |
| Change password Form                  | Submit invalid form     | Form does not submit and message displayed to correct invalid fields                                            | Pass   |
| Password reset Form                   | Submit valid data       | User password is updated to the new password                                                                    | Pass   |
| Cancel button                         | Click button            | Go to Home page                                                                                                 | Pass   |
