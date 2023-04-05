<h1 align="center">A to PC</h1>

## Introduction
A to PC is an online E-commerce store that is focused on selling PC monitors, storage and peripherals to customers. Users can browse a list of products and make purchases from the available products by filling out their delivery and billing information. Users also have the option to leave a review and rate products and can view and comment on blog posts in the site blog. This site is aimed at tech shoppers who are looking to purchase PC monitors, storage or peripherals.

[The live site can be accessed here.](https://atopc.herokuapp.com/)

![Responsive check](assets/readme-images/am-i-responsive.PNG)

## Table of Contents
1. [User Experience](#user-experience)
    - [Target Audience](#target-audience)
    - [User Stories](#user-stories)
    - [Unfinished User Stories](#unfinished-user-stories)
    - [Scope](#scope)
2. [Design](#design)
    - [Colours](#colours)
    - [Font Style](#font-style)
    - [Wireframes](#wireframes)
    - [Database Schema](#database-schema)

## User Experience

### Target Audience
A to PC was designed as a Business-to-customer(B2C) e-commerce store with a focus of selling PC monitors, storage and peripherals to customers. The users visiting this site will have basic knowledge of tech products and be looking to browse and purchase products that the website offers. Some users visiting this site may also be looking to leave a review on a product, sign up to the newsletter or browse the site blog. As the main purpose of the site is to sell products to customers, it was decided that the process of purchasing an item should be simple and hassle-free, with clear navigation for users to find what they are looking for and proceed to checkout.

### User Stories
Using github projects I created a series of user stories related to the site and its purpose. To follow the process of Agile Development, I used MoSCoW prioritization to label each story. These can be found [here.](https://github.com/users/JackDay94/projects/4)

The user stories can be divided into the following Epics:
1. Epic 1 - User Authentication and Account
    - As a site user I can register an account so that I can make purchases and review products. (must-have)
        - Acceptance Criteria: User can successfully register for an account using username, password and email.
    - As a site user/ owner I can sign into and sign out of my account to access certain site features that require being signed in when I need to. (must-have)
        - Acceptance Criteria: User can sign in/out of their registered account.
    - As a site user I can recover my forgotten password so that I am able to login to my account again. (should-have)
        - Acceptance Criteria: User can reset their password by providing their email used to register.
    - As a site user I can view my own personalised profile to see and update details of my order history and delivery/billing information. (should-have)
        - Acceptance Criteria: User profile created after registering, User has own profile page, User can view order history, User can view/edit delivery/billing info.
2. Epic 2 - Navigating the site
    - As a site user/ owner I can navigate pages of the site to find the content I wish to see with ease. (must-have)
        - Acceptance Criteria: Page links clear to user, Page links work, Page links named correctly.
    - As a site user I can browse between pages of products by clicking the next or prev page buttons to find products I may be looking for. (should-have)
        - Acceptance Criteria: Products page split into multiple pages, User can go back and forward between pages.
    - As a site user I can click on links to bring me to the social media pages for the website so that I can get involved. (could-have)
        - Acceptance Criteria: Social media links in footer, Social media pages open in new tab.
3. Epic 3 - Products
    - As a site user I can browse a list of products that are on sale so that I can make a choice on what to purchase. (must-have)
        - Acceptance Criteria: List of products displayed on page.
    - As a site user I can view the details of a product to find out more information about it to help me make a purchase. (must-have)
        - Acceptance Criteria: Product image, price, rating, description on product page, Each product has its own detail page.
    - As a site user I can search for products so that I can find what I am looking for easier. (should-have)
        - Acceptance Criteria: Searching in search box returns relevant products.
    - As a site user I can sort a list of products by rating, name, price and category to find certain products easier. (should-have)
        - Acceptance Criteria: Products list can be sorted by rating, name, price and category.
    - As a site user I can filter a list of products based on certain criteria to help me find products easier. (should-have)
        - Acceptance Criteria: Product list can be filtered to display certain products that match the filter criteria.
    - As a site user I can view discounts that I can apply to a product so that I can get some money off a purchase. (could-have)
        - Acceptance Criteria: Discounts shown for products, User can apply discounts to a product.
    - As a site admin I can add/edit/delete discounts from the store to encourage users to purchase discounted items. (could-have)
        - Acceptance Criteria: Admin can create discount codes, Admin can edit discount codes, Admin can delete discount codes, Admin can set discount codes for specific products.
4. Epic 4 - Reviews and ratings
    - As a site user I can view the average rating and reviews for a product to see what other people are saying about a product. (must-have)
        - Acceptance Criteria: Product reviews visible on product page, Product rating is average of user ratings, Average rating shown for products.
    - As a site user I can leave a rating and review on a product to share my opinion and experiences with others. (must-have)
        - Acceptance Criteria: User can write a review and add a rating for a product, User reviews appear on associated product page.
    - As a site admin/user I can update and delete reviews that I have made to change my opinion on a product or remove my review of the product. (must-have)
        - Acceptance Criteria: User can edit their review, User can delete their review, Admin can edit/delete any review, User cannot edit/delete other users reviews.
5. Epic 5 - Purchasing products
    - As a site user I can choose the quantity of the item that I want to purchase. (must-have)
        - Acceptance Criteria: User can increase/decrease quantity of items, User cannot add 0 or less items.
    - As a site user I can add or remove a product to my bag so that I make a decision on my purchase. (must-have)
        - Acceptance Criteria: Products can be added to bag, Products can be removed from bag.
    - As a site user I can view the total cost of the items in my bag so that I know how much I need to pay before completing my purchase. (must-have)
        - Acceptance Criteria: Bag displays products currently added, Bag shows quantity and price of each product in it, Bag shows total price of its contents.
    - As a site user I can checkout the items in my bag to enter my payment and delivery details and complete my purchase. (must-have)
        - Acceptance Criteria: Checkout displays a summary of bag contents, Checkout displays delivery information, Checkout displays card payment information, Checkout shows order confirmation page on successful purchase.
    - As a site user I can receive a notification by email when I make a purchase to show me the details of my purchase. (must-have)
        - Acceptance Criteria: User receives email after making purchase, Email contains order confirmation for the purchase.
6. Epic 6 - Wishlist
    - As a site user I can view my wishlist to see what I currently have added. (could-have)
        - Acceptance Criteria: User can access their wishlist page, Wishlist shows items currently added.
    - As a site user I can add/delete items to my wishlist so that I can save them to purchase at a later date or remove them when I don't want them anymore. (could-have)
        - Acceptance Criteria: User can add a product to their wishlist, User can remove a product from their wishlist.
7. Epic 7 - Blog
    - As a site user I can view blog posts made by the site to get updates on certain topics. (could-have)
        - Acceptance Criteria: List of blog posts available on the site, User can click on blog posts to view their content.
    - As a site admin I can add, edit and delete blog posts to the site to keep users updated on site news. (could-have)
        - Acceptance Criteria: Admin can add new blog posts, Admin can edit existing blog posts, Admin can delete blog posts, Users cannot add/edit/delete blog posts.
8. Epic 8 - Newsletter
    - As a site user I can use my email to sign up to a newsletter to be notified of deals and news. (should-have)
        - Acceptance Criteria: User can submit their email to a newsletter signup form, User is notified they have signed up successfully, Admin can see emails registered to newsletter.
9. Epic 9 - Admin management
    - As a site admin I can add new products to the existing product list to expand the available products in store. (must-have)
        - Acceptance Criteria: Admin can add products to site using product form, Newly added products show correctly in the store, Users cannot add products.
    - As a site admin I can edit and delete existing products to allow me to update product details or remove a product from the store. (must-have)
        - Acceptance Criteria: Admin can edit existing products, Admin can delete existing products, Product list updated to reflect edited/deleted products, Users cannot edit/delete products.

### Unfinished User Stories
For this project I employed an Agile approach through the use of github projects to plan and track user stories through the course of development. At the start of the project I created user stories that would fit the goal of the project and labelled these based on priority as either must-have, should-have or could-have. Initially all user stories were placed in the 'Todo' column, and as the project progressed and I began to work on a user story, I moved them to the 'In progress' column. When a user story was completed, I then moved it to the 'Done' column and moved on to the next. Overall a total of 26/29 user stories were completed.

Unfortunately, due to time constraints, I was unable to complete 3 of my user stories. However, these are not required for the site to function as needed and were considered a lower priority.

![User Stories](assets/readme-images/user-stories.PNG)

### Scope
With the target audience and business goals in mind, I set out to create a site that will function to meet their needs. To do this I chose to include the following features:

- Product page with a list of products on sale that can be sorted and filtered.
- Product detail page with a detail view of a chosen product showing product information, price etc.
- Responsive navbar with links to other pages in the store.
- Account creation and ability to login/logout for users.
- Profile page with default delivery/billing info and order history for users.
- Ability to add products to a bag and proceed to checkout to purchase items.
- Users can leave product reviews and ratings.
- Users can sign up to a newsletter mailing list.
- Home page to entice users to browse the rest of the store.

## Design

### Colours
To help users navigate the site better I wanted to ensure that the colour scheme was pleasant and not distracting from the main site content. I chose to use a mix of light and dark colours for the site, with the main content body having a white background and the top info banner and footer using darker backgrounds to seperate the content. The site uses mostly primary colours with the buttons and links, such as submit buttons for forms using a green colour to signify they are for submitting. I tried to keep a consistent colour scheme throughout the pages of the site to help provide a sense of fluidity when exploring the site.

### Font Style
I wanted to use a simple and easily readable font for the site, since the main purpose of the site is to provide products for a user to purchase. For this I chose the 'Lato' font style from Google Fonts as it is easy to read and clear on different screen sizes. I used a bold font weight for headings and some sub-headings to distinguish them from the rest of the content on the page.

### Wireframes
I used Balsamiq wireframes to create a set of basic wireframes for this project. I used the layouts from the wireframes as reference when creating the pages for the site and then adjusted content on the pages to make them fit better. For this reason, the wireframes do not 100% portray the end product.

<details>
<summary>Desktop</summary>
Home

![Desktop Wireframe home](assets/readme-images/desktop-home-wf.PNG)

All Products

![Desktop Wireframe all products](assets/readme-images/desktop-all-products-wf.PNG)

Product detail

![Desktop Wireframe product detail](assets/readme-images/desktop-product-wf.PNG)

Add Product

![Desktop Wireframe add product](assets/readme-images/desktop-add-product-wf.PNG)

Edit Product

![Desktop Wireframe edit product](assets/readme-images/desktop-edit-product-wf.PNG)

Register and Login

![Desktop Wireframe register and login](assets/readme-images/desktop-register-login-wf.PNG)

Bag

![Desktop Wireframe bag](assets/readme-images/desktop-bag-wf.PNG)

Checkout

![Desktop Wireframe checkout](assets/readme-images/desktop-checkout-wf.PNG)

Profile

![Desktop Wireframe profile](assets/readme-images/desktop-profile-wf.PNG)

</details>

<details>
<summary>Mobile</summary>

Home

![Mobile Wireframe home](assets/readme-images/mobile-home-wf.PNG)

All Products

![Mobile Wireframe all products](assets/readme-images/mobile-all-products-wf.PNG)

Product detail

![Mobile Wireframe product detail](assets/readme-images/mobile-product-wf.PNG)

Add Product

![Mobile Wireframe add product](assets/readme-images/mobile-add-product-wf.PNG)

Edit Product

![Mobile Wireframe edit product](assets/readme-images/mobile-edit-product-wf.PNG)

Register and Login

![Mobile Wireframe register and login](assets/readme-images/mobile-register-login-wf.PNG)

Bag

![Mobile Wireframe bag](assets/readme-images/mobile-bag-wf.PNG)

Checkout

![Mobile Wireframe checkout](assets/readme-images/mobile-checkout-wf.PNG)

Profile

![Mobile Wireframe profile](assets/readme-images/mobile-profile-wf.PNG)

</details>

### Database Schema
