# cMarket

cMarket is an E-Commerce site where customers can purchase cryptocurrency related merchandise. In additon to being able to purchase clothing and accessories, users are able to add items to their wishlist and subscribe to the cMarket newsletter which contains all of the latest deals and products coming to the site.

cMarket is a Full-Stack application built with the Django framework which includes full CRUD functionality allowing users to Sign Up / Log In to their account as well as viewing all products, adding items to their bag and wishlist and having full payment functionality through Stripe.

[Deployed Site](https://c--market.herokuapp.com/)

---

![AmIResponsive]()

---
 
## Purpose 

The primary purpose of the website is for the website owner to sell cryptocurrency related merchandise online.

## Aims 

To provide users an intuative e-commerce experience where cryptocurrency enthusiasts can go to browse and purchase crypto-related accessories and clothing items

## Users's Goals:
- Buy crypto-related clothing online
- Create a profile so that they can save their delivery information and also see their order history and qualify for customer benefits

## Site Owner's Goals:
- Sell their crypto-related merchandise online
- Maintain a list of registered users so they can send the newsletter to them, offering exclusive products and discounts
    
## Target Audience

The global cryptocurrency market stood at a revenue of $1,542.9m in 2021, and with that, it has lead to a growth in crypto-related products like clothing and accessories. As a result, cMarket's target audience are for cryptocurrency enthusiasts who would like to purchase items of clothing related to their favourite coin/token. Our site offers a variety of products, from T-Shirts, Hoddies, Gym Vests and Hats allowing customers to have a range of options to chose from. 

# E-Commerce Business Model

The following section documents the planning process for the website, based on the type of e-commerce application it is, what products it is selling, and the customers it will have.

## E-commerce application type

This e-commerce application sells its products to customers who are individuals, therefore the business model is a B2C (Business to Customer). The website will sell products (rather than services) and is based on a single payment model, i.e. the customer pays for the product and that completes the transaction, there are no ongoing fees or subscriptions. The model is a Direct to Consumer one, i.e. there are no third party intermediaries involved.

These factors mean that the following need to be taken account in the design/planning of the website:

- Customers, as individuals rather than businesses, might make impulse buys
- The website will need good quality images of the products, to show the customers what they are buying and to build trust in what they are buying
- The decision making process is shorter and they can make their own choice to buy the product (as opposed to justifying the expenditure to managers, which is the case in the B2B model)
- As a result, the steps the user needs to take to complete a purchase on the website should be as easy as possible and the design should take account of this.
- Since products are being sold, the database will need to store the details of these products
- There should be an ability for the customer to sort and filter products in the shop
- As the payment is a single payment, customers would expect to receive a confirmation once they have completed their purchase

## Features to be included

Based on the above analysis, an initial overview of features that would be needed are listed below. The full list of features implemented are outlined in the [Existing Features](https://github.com/RiyadhKh4n/portfolio-project-5#existing-features) section.

- Since items will be sold direct to customer and are all cryptocurrency related, the website should make it clear that all products are crypto-related (this should follow into the product descriptions)
- The site should contain high-quality images of all products as well as descriptions of the products so users can easily make the decision to buy
- The shop should allow users to sort and filter the products by the relevant categories so customers can find what they are looking for
- The path to making the purchase should be as easy/seamless as possible to allow the customer complete the transaction
- There must be a shopping bag/cart functionality so that users can add items to the cart, view the cart and ither go back to shopping or complete the checkout process
- There needs to be a login and authentication mechanism for users, so they can view their details and order history. Anonymous checkout should also be allowed if users do not have an account created
- There needs to be a chekcout process, and for registered users an option to use their saved delivery details for a quicker checkout
- Customer loyalty is an important factor, so there should also be a newsletter sign up, so that the site owner can keep customers up to date with latest products and deals. There should also be a Facebook Business page which is linked in the footer

## Databases and Data Required

Based on the above analysis, an inital overview of the models that would be needed for the site, and type of data in these tables can be seen below. A full description of the data models can be found in the [Database Schema section](https://github.com/RiyadhKh4n/portfolio-project-5#erd-diagram).

- A Users table, to store information about users, such as name, email address and password so they are able to login
- A UserProfile table can extend the above, to include additional information such as the saved delivery address
- A Products table, used to store information such as product name, description, price, sku, image and the category
- An Orders table, to store the user, their delivery information and the order details
- A linked table to this would be OrderLineItems which would be the individual items in an order and store the product information and quantity of that product

# Search Engine Optimisation (SEO)

SEO is important for all business, so that the website can be found by search engines and rank in their results, so that users will actually find the website when searching for the relevant terms. There are two parts to this: determining the keywords that might be searched for, and using them in the website; and generating the files the search engines will use to crawl the website.

## Keywords

Keyword research was completed in order to determine which keywords to include in the website's content, image file names and alt text, headings, page titles and in the meta description and meta keywords. A mix of short and long tail keywords were identified (from brainstorming and using Google to find related searches), within the key topics for the website like cryptocurrency and clothing. Without having access to paid keyword planner websites, it is somewhat difficult to find alternative words for some of the most popular keywords, however this would be a future feature to be implemented if the business was a real business.

### Implementation of keywords

- The ```meta``` ```description``` and ```keywords``` tags were included in base.html, so that they are present for all pages. These were then tweaked on some pages to be more specific to those pages
    
    - The products page has specific meta description and meta keywords related to the products
    - In the product details page the product name is added to the meta description

- The content aims to be trustworthy, relevant, expert and authoratative. The website includes a Privacy Policy and Terms of Use documents for trustworthiness. The product and market images are high quality (bearing in mind these are sourced using free resources but would be professional images if this were a real business)

### sitemap.xml & robots.txt

The sitemap.xml was created to list all the page urls that can be accessed without logging in, this helps the search engines crawl the site. A robots.txt was created, listing the urls for search engines not to access (the listed urls are to do with account sign in, the bag and checkout process and the adding of products since these are not relevant for search results). The existence of the robots.txt file will help improve SEO ranking as it shows the website acknowledges that the search engines are allowed onto the site, so is an indicator of quality. Both files exist on the deployed site. Note: since this is a project and not a live site for a real business (and hasn't been deployed to a custom domain), the last steps of registering the sitemap with Google and testing the robots.txt have not been done.

# Marketing

The first part of the marketing strategy for this business is ensuring that the webpage is optimised as far as possible in terms of search engines. The measures taken to address this are outlined above in the [Search Engine Optimisation (SEO)](https://github.com/RiyadhKh4n/portfolio-project-5#search-engine-optimisation-seo) section. The other marketing measures to be employed are explained below.

cMarket is a small, one person business and its goals are to sell its crypto-related products online. The website users will be a mix of male/female as crypto is for everyone, as a result, we will accomodate for both male and female shoppers by offering unisex and gender specific items of clothing, with the estimated average age of users being 20 - 40. This age group are amongst users who use social media heavily, as a result, the most appropriate platform would be those with a more visual basis such as Instagram and Facebook as these are the most popular with the given age range. TikTok will not be used as its audience is mainly younger, however this can be revised in the future. As the business is new and does not have the budget for aggressive advertising, it will focus on organic growth through Social Media Marketing.

A Facebook Business Page will be created which will promote the business, promote the products being sold and be a platform which advertising campaign can be held to help reach a wider audience. The content on the Facebook page can be reused on the other social channels and can include:

- Photos showing the products on offer
- Posts alerting followers of new products, special offers and products back in stock
- Informative posts about the business and its misson
- Posts asking for user engagement such as a poll to see which products customers would like to see
- Posts which alert followers of giveaways where they can potentially win items for free

During project development, the Facebook business page was created and the link added to the website foooter. The business details were added, with a Shop button, a link to the website, page description and a welcome post. However, as expected because the business doesn't exist, the page was taken down by Facebook so the link no longer works. [Here is a screenshot of the Facebook business page](documentation/testing/facebook-page.png) before it was taken down.

Email marketing is free (for the numbers this small business will initially have) and relatively easy to set up, so the business will use this too. The website will include a section in the footer to sign up to the newsletter. Building up a list of email subscribers through the newsletter sign up means the business will then have a pool of people who it knows are interested in its products (as they voluntarily signed up!) so are more likely to make a purchase.

The business owner can use the newsletter to:

- highlight when new products have been added to the website
- let subscribers know about any discounts or promotions which are live
- let subscribers know when an item is back in stock on the website

The business owner doesn't have to invest much time to manage the email marketing, and can try out different types of formats for the newsletter over time to see what works, so it is an easy strategy to get started with in the early days of the business. They need to ensure they are GDPR compliant by making it an opt in process (which it will be via the sign up form) and making it easy to unsubscribe - the link to unsubscribe should be in each email sent.

# User Experience (UX)

## User Stories

For ease of reading, the user stories around similar actions have been grouped into loose categories:

### General, site purpose, navigation:

- [#1](https://github.com/RiyadhKh4n/portfolio-project-5/issues/1) As a visiting user I can easily find out what the purpose of the website is and learn more about the site owner and the products being sold so that I can decide to stay and browse or not
- [#2](https://github.com/RiyadhKh4n/portfolio-project-5/issues/2) As a site user I can navigate the site so that I can find the page I want to go to
- [#3](https://github.com/RiyadhKh4n/portfolio-project-5/issues/3) As a user I can find the sites social media accounts so that I can follow them on social media to keep up to date with the business
- [#4](https://github.com/RiyadhKh4n/portfolio-project-5/issues/4) As a site user I can sign up to the newsletter so that I can stay informed and stay engaged with the shop
- [#5](https://github.com/RiyadhKh4n/portfolio-project-5/issues/5) As a site user I can see a 'Page not found' page with consistent branding to the rest of the site, when I try to access a page in error so that I can find my way back to the website and know I have not left the website. Ensure page tells user which error they are getting.
- [#6](https://github.com/RiyadhKh4n/portfolio-project-5/issues/6) As a site user I can find the terms of use and privacy policy so that I can read these documents and have trust in the site
- [#7](https://github.com/RiyadhKh4n/portfolio-project-5/issues/7) As a user I can click on a back to top button so that I can get back to the top of the page without having to scroll
- [#8](https://github.com/RiyadhKh4n/portfolio-project-5/issues/8) As a user I can see a message confirming my actions (e.g. adding item to bag) so that I know my changes were received
- [#9](https://github.com/RiyadhKh4n/portfolio-project-5/issues/9) As a user I can quickly see which section of the website I am in from the main header so that I know which part of the website I am in and can navigate around easily

### Shop - Viewing Products:

- [#10](https://github.com/RiyadhKh4n/portfolio-project-5/issues/10) As a site user I can easily view all the products in the shop so that I can see all the available products immediately without having to sort or filter or take any action
- [#11](https://github.com/RiyadhKh4n/portfolio-project-5/issues/11) As a site user I can view an individual item details so that I can see the full details including the description and decide whether to buy
- [#12](https://github.com/RiyadhKh4n/portfolio-project-5/issues/12) As a site user I can select a specific category of product so that I can view just the items in that category to make it easier to make a decision
- [#13](https://github.com/RiyadhKh4n/portfolio-project-5/issues/13) As a site user I can sort the products in the shop so that I can find what I'm looking for easier
- [#14](https://github.com/RiyadhKh4n/portfolio-project-5/issues/14) As a site user I can search for a product in the shop so that I can find a particular item quickly
- [#15](https://github.com/RiyadhKh4n/portfolio-project-5/issues/15) As a user I can see the results for my filter option or search term so that I can quickly see how many products match my filter option/match my search term

### Shop - Adding to/updating the cart:

- [#16](https://github.com/RiyadhKh4n/portfolio-project-5/issues/16) As a site user I can add an item to my cart so that I can buy it
- [#17](https://github.com/RiyadhKh4n/portfolio-project-5/issues/17) As a site user I can select the quantity of an item before adding to my cart so that I can add multiple of that item at once
- [#18](https://github.com/RiyadhKh4n/portfolio-project-5/issues/18) As a site user I can see the total amount currently in my cart at all times so that I can keep track of how much I'll be spending
- [#19](https://github.com/RiyadhKh4n/portfolio-project-5/issues/19) As a site user I can see the items in my cart at any time so that I can check what I have already added to the cart
- [#20](https://github.com/RiyadhKh4n/portfolio-project-5/issues/20) As a site user I can adjust the quantity of a particular item in the cart so that I can buy more or less of the item directly from the cart
- [#21](https://github.com/RiyadhKh4n/portfolio-project-5/issues/21) As a site user I can remove an item from my cart so that I do not have to buy it if I've changed my mind

### Shop - Payment & Checkout:

- [#22](https://github.com/RiyadhKh4n/portfolio-project-5/issues/22) As a site user I can continue to the checkout process once I've decided on my purchase so that I can buy the items
- [#23](https://github.com/RiyadhKh4n/portfolio-project-5/issues/23) As a site user I can enter my delivery and payment details so that I can complete my purchase
- [#24](https://github.com/RiyadhKh4n/portfolio-project-5/issues/24) As a site user I can see the order summary while making payment so that I can still edit the details before payment if I made a mistake
- [#25](https://github.com/RiyadhKh4n/portfolio-project-5/issues/25) As a registered user I can save my delivery information when checking out so that it is saved to my profile for use with my next order
- [#26](https://github.com/RiyadhKh4n/portfolio-project-5/issues/26) As a site user I can see an order confirmation page so that I know that the order went through okay
- [#27](https://github.com/RiyadhKh4n/portfolio-project-5/issues/27) As a site user I can receive an email confirmation of my order so that I have this confirmation for my records
- [#28](https://github.com/RiyadhKh4n/portfolio-project-5/issues/28) As a user I can see a preview of my shopping cart when I make changes so that I can easily see the new cart
- [#29](https://github.com/RiyadhKh4n/portfolio-project-5/issues/29) As a site owner I can ensure that an order is created once payment is made so that a customer does not make a payment, without an order being created in the database

### User account setup, sign in and out:

- [#30](https://github.com/RiyadhKh4n/portfolio-project-5/issues/30) As a site user I can sign up for an account so that I can enjoy the benefits of having an account with the site
- [#31](https://github.com/RiyadhKh4n/portfolio-project-5/issues/31) As a site user I want to receive an email confirmation when I register so that I know my account registration was successful and secure
- [#32](https://github.com/RiyadhKh4n/portfolio-project-5/issues/32) As a registered user I can sign into my account so that I can access my profile to view all past orders
- [#33](https://github.com/RiyadhKh4n/portfolio-project-5/issues/33) As a registered user I can sign out of my account when finished so that I know I am signed out securely
- [#34](https://github.com/RiyadhKh4n/portfolio-project-5/issues/34) As a registered user I can easily see if I am signed into my account or not so that I know straight away if I need to sign in

### User Profile:

- [#35](https://github.com/RiyadhKh4n/portfolio-project-5/issues/35) As a registered user I can update my default delivery information in my profile so that the updated details are recorded for future orders
- [#36](https://github.com/RiyadhKh4n/portfolio-project-5/issues/36) As a registered user I can see my previous orders in my profile so that I can see all the orders I made and can find details of a previous order
- [#37](https://github.com/RiyadhKh4n/portfolio-project-5/issues/37) As a registered user I can view details of a previous order so that I can check what was ordered and where it was delivered to
- [#38](https://github.com/RiyadhKh4n/portfolio-project-5/issues/38) As a registered user I can easily navigate within the My Account pages so that I understand what pages are available and can get to them easily and I know what page I am on

### Admin for Shop Page:

- [#39](https://github.com/RiyadhKh4n/portfolio-project-5/issues/39) As a website owner I can view all the products in the shop, even if they are not active, so that I can see an overview of all products, and so that I can edit inactive products
- [#40](https://github.com/RiyadhKh4n/portfolio-project-5/issues/40) As a website owner I can add a new product to the shop so that I can sell the product to customers
- [#41](https://github.com/RiyadhKh4n/portfolio-project-5/issues/41) As a website owner I can edit the details of a product in the shop so that I can change the price, description etc. and customers will see the updated information
- [#42](https://github.com/RiyadhKh4n/portfolio-project-5/issues/42) As a website owner I can turn on or off the active flag on a product so that I can add or remove it from appearing in the shop for customers when it is in/out of stock
- [#43](https://github.com/RiyadhKh4n/portfolio-project-5/issues/43) As a website owner I can delete a product so that it will not appear in the shop
- [#44](https://github.com/RiyadhKh4n/portfolio-project-5/issues/44) As a website owner I can access the Django admin site for the categories so that I can add, edit or delete categories from here and new products for these categories can be added to the shop
- [#45](https://github.com/RiyadhKh4n/portfolio-project-5/issues/45) As a site owner I can access the Django admin site for the products so that I can view, edit, delete products from here as well as from the website
- [#46](https://github.com/RiyadhKh4n/portfolio-project-5/issues/46) As a website owner I can see orders in the admin site so that I can access the order details and fulfil the orders
- [#47](https://github.com/RiyadhKh4n/portfolio-project-5/issues/47) As a website owner I can add a product and the sku is created automatically so that the sku's for the products are standardised and I do not have to manually add a sku
- [#48](https://github.com/RiyadhKh4n/portfolio-project-5/issues/48) As a website owner I can have the sku of a product updated when the category is changed so that the sku of the product is reflects the new category

### Admin for User Profiles:

- [#49](https://github.com/RiyadhKh4n/portfolio-project-5/issues/49) As a site owner I can access the Django admin site for Profiles so that I can view user profiles

### Marketing / SEO

- [#50](https://github.com/RiyadhKh4n/portfolio-project-5/issues/50) As a website owner I want my website to contain relevant keywords so that users searching for these keywords will be more likely to find my website in web search results
- [#51](https://github.com/RiyadhKh4n/portfolio-project-5/issues/51) As a website owner I have a link to the Facebook business page on the website so that customers or visitors to the website can follow the Facebook page and I can generate more business through the Facebook page
- [#52](https://github.com/RiyadhKh4n/portfolio-project-5/issues/52) As a website owner I have relevant keywords included in the webpage metadata so that it helps improve SEO so that users searching for these keywords can find my website
- [#53](https://github.com/RiyadhKh4n/portfolio-project-5/issues/53) As a website owner I can have a sitemap.xml and robots.txt file created for the website so that search engines can crawl the essential pages of the site and therefore users can find the site when searching key terms in search engine searches

## Development Method

When developing cMarket I will take an Agile Approach. Meaning I will take an iterative approach to project management and software development helping me to deliver value faster and speed up development time. I will focus on working software over comprehensive documentation and responding to change over following a plan when creating the project.

I also intergrated the MoSoCoW method which is a four-step approach to prioritizing which project requirements will provide the best return on investment (ROI). MoSCoW stands for Must- Have, Should-Have, Could-Have and Wont-Have. Using this method, I am able to label and order my User Stories into four categories, allowing me to know which ones to focus on and to ensure I meet my project vision and aims.

## Design

### Wireframes

![m.wireframe](documentation/testing/mobilewireframe.png)
![d.wireframe](documentation/testing/desktopwireframe.png)

### Database Schema

The datasets for the project are:

- Home Information: allows users to join newsletter or contact the site admin
- User Information: username, email, password and saved delivery info
- Product Information: products displayed in shop
- Category Information: the category each product belongs to
- Order Information: items the user purchased
- Wishlist Information: saved items users added to wishlist

The data is organised using the following models:

- **User**: Django built in User model. For authentication and authorisation
- **UserProfile**: to store extra information relating to the user, in this case their delivery details
    - extends the Django User model using a OneToOne relationship
    - an instance of this model will be created each time a User record is created
    - the delivery info fields can all be blank as a user does not have to save these details to their profile
    - delivery info can be saved/edited on the UserProfile record by the user either ticking te save delivery info checkbox on the Checkout form, or by updating the USerProfile form on the profile page
- **Category**: Holds the categories for the products
    - friendly name is the name shown on the front-end
    - name must be unique so as to avoid conflicts when filtering by category
    - admin user will create/edit/delete instances of this model via the Django admin site
- **Product**: Holds the details of the products that will be displayed on the Shop page
    - each product must have a category, Category is a ForeignKey (One-To-Many) in the Product model
    - product name must be unique
    - admin user will create instances of this model via the form on the add product page on the frontend. They will edit and delete from the links on each product in the Shop page also. (Shop page displays all products, not just active, to the admin user)
- **Order**: The details of an Order
    - instances of this model are created during the Checkout process
    - this model will have some methods to create the order_number, calcuate the order_total, delivery_cost and grand_total and works in conjunction with the OrderLineItem model
    - this model includes two fields which will be used during the webhook handling process with Stripe. During this process, a check is done to see if the order is already in the database, and if not then create it. Since the same customer can order the same item(s) on more than one occasion, there needs to be some unique fields to prevent the previous identical order being found as this new order. These fields are: 'original_cart', a TextField containing a json dump of the bag, and 'stripe_pid', the Stripe payment intent id from the order, which is unique.
- **OrderLineItem**: The individual items in the Order instance
    - Order is a ForeignKey in this model (one order to many line items)
    - Product is a ForeignKey in this model to access the product details
    - this model calculates the total for each line item, which is then used by the ORder model to calculate the grand total
- **Wishlist**: The items a user adds to their wishlist
    - each time a user clicks the 'heart' on a product, it will be added to their wishlist
    - within the wishlist, users can edit and delete items from it

    ### Entity Relationship Diagram

    ![ERD Diagram](documentation/testing/erd.png)

    * Lightblue = Custom Models

    ### Project Structure

    cMarket will be developed using Django, as a result I will split the program functionality into separate apps. A Django application is a Python package that is specifically inteded for use in a Django project. For my project I will create six apps; Home, Products, Bag, Profiles, Checkout and Wishlist.

    Home:
    - To display the Home page (index.html)
    - Will contain two models, Newsletter and ContactForm. This is because the functionality for these two features will be within the footer, whose template will be within the Home app.

    Products: 
    - To handle the viewing of products in the Shop page, as well as the creating, editing and deleting of products by the admin user
    - Will have a Product model (product details) and Category model (product categrory names)
    - Templates:
        - Shop (displays all products, filter/sort options)
        - Product Details (displays individual product)
        - Add Product (add product form, admin user only)
        - Edit Product (edit product form, admin user only)

    Bag: 
    - To handle adding items to the shopping cart, adjusting quanitity in the shopping bag and removing items
    - There is no model in this app, however it will use the Product model from the Products App in its views
    - Templates:
        - Bag (display items in the shopping bag)

    Profiles:
    - To handle the user information - their saved delivery details and their order history
    - Will have a USerProfile model which extends the Django User model using a OneToOne link, to store the extra information (delivery details)
    - This app also uses the Order model from the Checkout App to display the order history
    - Templates:
        - My Profile (display/allows edits of saved delivery details and displays order histroy, registered users only)

    Checkout: 
    - To handle the checkout and payment process
    - Will have an Order model (order delivery and amount details) and OrderLineItem model (details of each individual item in the order)
    - This app will also use the Product and UserProfile models from the other apps in the views
    - Will contain the code which contect to the Stripe webhook as well as the JavaScript needed to get the payment process working
    - Templates:
        - Checkout (delivery + payment form)
        - Order confirmation (success page after checkout, also used to display details og a previous order form the profile page)

    Wishlist:
    - To handle the wishlist functionality of the site
    - Will have the wishlist model which stores the product being added, its image as well as the date when it was added
    - Will contain the code which handles the CRUD functionality of the wishlist
    - Templates:
        - Wishlist (allow users to view, edit and delete items from their wishlist)

* ### Colour Scheme

    When designing cMarket I wanted to ensure the colour scheme of my site was visually appealing, I used the [Coin Bureau Shop](https://store.coinbureau.com/shop/) to get the colour scheme for their site and implemented them into my own, as I liked the dark theme of their shop. 

    As a result, the main two colours used in the site are #24262b which is used for the majority of the site and #373b46 which is used for the product cards. For the sites accents I used rgb(106,90,205) which contrasts the dark-grey quite nicely and adds a nice pop of colour to the site without taking away from the dark theme.

* ### Typography

    When considering the typography of the site, I wanted to use fonts that were readable, professional and easy on the eye. As a result, for the main headings I went with [Righteous](https://fonts.google.com/specimen/Righteous?query=Righteous). For all other text on the website I went with [Lato](https://fonts.google.com/specimen/Lato?query=Lato) as I feel that is compliments Righteous nicely and conforms to the three points I set out when chosing the typography for cMarket.

* ### Icons

    All icons used in the website were taken from [fontawesome](https://fontawesome.com/start)

    - #### Favicon

        The favicon for the site was created with [favicon.cc](https://www.favicon.cc/) 
 
# Features
 
Here describes the main features of the website and what the user can expect when viewing ~
 
## Current Features:

### Navbar:

Navbar where users can easily naviagte through the site

![d.nav](documentation/testing/desktopnav.png)

Navabr is styled to be responsive and collapsible for smaller screens

![m.nav](documentation/testing/mobilenavbar.png)

### Homepage

The home page is designed to maintain simplicity. Less and direct information is provided for the site visitor when they first land on the page. The user is shown a button which they can click to view the shop.

![home](documentation/testing/homepage.png)

### Footer

The Footer is fixed to the bottom of the page. The footer contains all the necessary links customers may need like the privacy policy, terms and conditions, contact form and the cMarket newsletter.

![d.footer](documentation/testing/footerdesktop.png)

The footer is fully responsive for all screen sizes and can smoothly adjust style for screen size.

![m.footer](documentation/testing/mobilefooter.png)

### Product Page

Here users can find all the products available on cMarket from T-Shirts and Hoodies to Hats and Mugs. Each Product is in the form of cards that has an image, title, price, category and rating. This page also features a filtering section where users can filter the products depending on Gender or Product Type.

![products](documentation/testing/desktopproducts.png)

### Search & Filter Functionality

Find products by searching and filtering. Users can find what they want by searching about it in the search field. The type of product, name of item, cryptocurrency or category; are ways users can search for products in the site

Once the search result is generated, the number of items found based on their search, and a button to go back to all Products is provided

For each search requested, items found will be listed, here I am searching for products related to ETH:

![searcing](documentation/testing/searching.png)

Users can also use the in-built filtering functionality in order to only see products of a certain type, here I am filtering for Womens Clothes:

![filter](documentation/testing/filter.png)

### Product Details Page

When a user clicks on a product, they will see the product details page where they can view the product description as well as select their size and add the item to basket or their wishlist

![pd](documentation/testing/product-details.png)

### Wishlist

Authenticated users can add any product they like to their wishlist page if they want to.

Wishlist will help users to list all the products that they may like to buy in the future. Users can use this page to differentiate, identify and select their favourite product from cMarket.

Users can also delete an item from their wishlist if they so chose

![wishlist](documentation/testing/wishlist.png)

### Profile

Every registered user will have a profile page. In order to access your profile page, you must be registered and signed in. This page can be used to manage their delivery information and view all past orders.

![empty-profile](documentation/testing/profile-empty.png)
![not-empty-profile](documentation/testing/profile-not-empty.png)

### Bag

Once users have selected the items they would like to buy, they can view their bag and checkout. Here users can update the quantity of each item, as well as remove an item from their bag. They can also see the grand total and navigate back to the shop or continue onto checkout.

![bag](documentation/testing/bag-desktop.png)

### Checkout

When checking out, users must enter personal details like Name and Email. As well as this, they must enter the delivery address which can either be auto-filled via the profile page or manually entered for non-authenticated users. The payment field is generated using [Stripe](https://stripe.com/en-se), it is a safe and secure payment system. Stripe does validation and authenticates the card owner for completing the payment process. Users are notified how much their card will be charged when they click payment button. 

Users can see a preview of their order on the right hand side of the screen as well as the grand total.

Currently you can make payments with their test card number:

`4242 4242 4242 4242 | 04/24 | 242 | 42424`

![checkout](documentation/testing/checkout-desktop.png)

While the transaction is in progress, a loader is displayed letting the user know the transaction is being made:

![overlay](documentation/testing/overlay.png)

If they payment goes through without problems, the user will see the checkout confirmation page letting them know their order details

![checkout-success](documentation/testing/checkout-success-new.png)

### Privacy and Terms & Conditions Page

![privacy](documentation/testing/extra-pages.png)

### Contact Us Page

Users are able to fill out a form if they would like to contact the owner to suggest site improvements, product suggestions or general feedback.

![contact](documentation/testing/contact-us.png)

### Newsletter Subscription

Subscription is for subscribing to our site newsletter. Any site visitor can subscribe to the newsletter, they do not have to register to the site for subscribing to our newsletter.

![newsletter](documentation/testing/newsletter.png)

### Admin Only Features

As the site admin, I am able to add, edit and delete products through the front-end via the 'Product Management' section

![menu](documentation/testing/menu.png)
![add-product](documentation/testing/add-product.png)
![edit-product](documentation/testing/edit-product.png)

## Future Features:

# Technologies
## Programming Languages:

- [HTML](https://developer.mozilla.org/en-US/docs/Learn/Getting_started_with_the_web/HTML_basics) - The HyperText Markup Language or HTML is the standard markup language for documents designed to be displayed in a web browser

- [CSS](https://en.wikipedia.org/wiki/CSS) - Cascading Style Sheets is a style sheet language used for describing the presentation of a document

- [Python](https://www.python.org/) - Python is an interpreted high-level general-purpose programming language. It is used when creating the backend functionality in Django

- [JavaScript](https://www.javascript.com/) - JavaScript is a high-level language that has dynamic typing, prototype-based object-orientation, and first-class functions. It is multi-paradigm, supporting event-driven, functional, and imperative programming styles.
 
I used GitHub [Project Boards](https://github.com/RiyadhKh4n/portfolio-project-5/projects/1) to keep track of all the User Stories and Tasks necessary in order to build Cryptics

- The [User Story Project Board](https://github.com/RiyadhKh4n/cryptics/projects/1) was used to keep track of my User Stories and ensure I implemented all the functionality I set out to implement. I used the MoSCoW method to prioritize which project requirements will provide the best user experience.

## Frameworks

1. [Django](https://www.djangoproject.com/)
    * Django is a Python-based free and open-source web framework that follows the model–template–views architectural pattern.

2. [Bootstrap](https://getbootstrap.com/)
    * Bootstrap is a free and open-source CSS framework directed at responsive, mobile-first front-end web development.

3. [Oauthlib](https://github.com/oauthlib/oauthlib)
    * OAuthLib is a framework which implements the logic of OAuth1 or OAuth2 without assuming a specific HTTP request object or web framework.

## Libraries 

1. [Os Library](https://docs.python.org/3/library/os.html)
    * Used to clear the console.

2. [Requests](https://pypi.org/project/requests/)
    * Allowed me to send HTTP requests without having to manually add query to strings to the URLs.

3. [dj-database-url](https://pypi.org/project/dj-database-url/)
    * This simple Django utility allows you to utilize the 12factor inspired DATABASE_URL environment variable to configure your Django application.
 
4. [asgiref](https://github.com/django/asgiref)
    * ASGI is a standard for Python asynchronous web apps and servers to communicate with each other, and positioned as an asynchronous successor to WSGI.

5. [django-allauth](https://django-allauth.readthedocs.io/en/latest/)
    * Integrated set of Django applications addressing authentication, registration, account management as well as 3rd party (social) account authentication.

6. [gunicorn](https://gunicorn.org/)
    * The Gunicorn "Green Unicorn" is a Python Web Server Gateway Interface HTTP server.

7. [psycopg2](https://pypi.org/project/psycopg2/)
    * Psycopg is the most popular PostgreSQL database adapter for the Python programming language. 

8. [PyJWT](https://pyjwt.readthedocs.io/en/latest/)
    * PyJWT is a Python library which allows you to encode and decode JSON Web Tokens (JWT).

9. [sqlparse](https://pypi.org/project/sqlparse/)
    * Sqlparse is a non-validating SQL parser for Python. It provides support for parsing, splitting and formatting SQL statements.

## Programs Used:
 
1. [GitPod](https://www.gitpod.io/):
    * GitPod was the IDE used to create the site
 
2. [Git](https://git-scm.com/):
    * Git was used for version control by utilizing the Gitpod terminal to commit to Git and Push to GitHub.
 
3. [GitHub](https://github.com/):
    * GitHub is used to store the projects code after being pushed from Git.
 
4. [Google Developer Tools](https://developer.chrome.com/docs/devtools/):
    * Used to test the program throughout development
 
5. [Heroku](https://dashboard.heroku.com/login):
    * Used to Deploy the Project
 
6. [AMiResponsive](http://ami.responsivedesign.is/):
    * To generate the image at the beginning of the README
 
7. [TinyPNG](https://tinypng.com/):
    * This was used to compress all images used in the README.md
 
8. [PEP8](http://pep8online.com/):
    * Used to validate my Python code
 
9. [favicon.cc](https://www.favicon.cc/):
    * Used to create the favicon

10. [HerokuSQL](https://www.heroku.com/postgres):
    * Database used for deployed project

11. [Balsamiq](https://balsamiq.com/wireframes/):
    * Used to create Wireframes

12. [SmartDraw](https://www.smartdraw.com/): 
    * Used to create ERD diagrams

13. [W3C Markup Validation Service](https://validator.w3.org/):
    * Used to validate HTML code

14. [W3C CSS Validation Service](https://jigsaw.w3.org/css-validator/):
    * Used to validate CSS

15. [JSHint](https://jshint.com/):
    * Used to validate any JavaScript code used

16. [Stripe](https://stripe.com/gb):
    * Used to handle payments (currently only set up to handle test payments)

17. [Gmail](https://mail.google.com/):
    * Used to send emails

18. [Facebook](https://www.facebook.com/):
    * Used to created the Facebook Business page

19. [AWS](https://aws.amazon.com/what-is-aws/):
    * Used to store static files

# Testing
 
Due to the size of the testing section for Cryptics I have created [TESTING.md](TESTING.md). It contains all my validator testing, lighthouse scores, Django Testing, User Story Testing, Manual Tests, Responsiveness Tests, Browser Compatibility Tests as well as any bugs.
 
[Link To TESTING.md](TESTING.md)
   
# Deployment
 
## GitPod - during development

Gitpod was used as the development environment, with GitHub for version control and hosting the repository. The repository for this project, and the associated workspace, was created from the [Code Institute student tempate](https://github.com/Code-Institute-Org/gitpod-full-template).

- During development, code was written in the Gitpod workspace and changes to the frontend were previewed by opening the browser via the terminal in Gitpod, using the command ```python3 manage.py runserver``` and then selecting the Open Browser button when the following message appeared: "a service is available on Port 8000".
- Libraries/Frameworks used in the application were installed by typing the relevant install command (as per documentation) in the terminal, e.g. ```pip3 install django```, where Django is the name of the framework being installed
- Files and code were added to the staging area in Gitpod using the command ```git add .``` and commited using ```git commit -m "commit message"```.
- Commited changes were then pushed to GitHub using the ```git push``` command.

## Deployment to Heroku

The following steps show how to deploy the application to [Heroku](https://id.heroku.com/login), using [AWS](https://aws.amazon.com/) to host media and static files. Note: these steps explain how you would do this, however some steps will be irrelevant if you are forking the repository as it will already contain settings.py file for example. You can also install the requirements in one go using the requirements.txt file instead of individually as explained below. The below steps are intended as a guide to explain how this project was deployed.

### Inital set up in workspace:

Before deploying to Heroku, the initial set up and creation of the project and app need to be completed in the IDE, in this case Gitpod workspace. Do the following in the command line:

1. Install django ```pip3 install Django==3.2``` Note: using version 3.2 of Django and not the latest version which is version 4. and gunicorn: ```pip3 install django gunicorn```
2. Install gunicorn for running the deployed website ```pip3 install gunicorn```
3. Install supporting libraries - for postgres: ```pip3 install dj_database_url pyscopg2```
4. Install any other required libraries/tools
5. Create the requirements.txt file: ```pip3 freeze --local > requirements```. This creates the requirements.txt file with the above dependencies. Later on in development, any further dependencies that are installed can be added to the file using ```pip3 freeze > requirements.txt```. Heroku will use this file to install the requirements when creating the application on Heroku.
6. Create the django project: ```django-admin startproject projectname .```. The ```.``` means create the project in the current directory
7. Create a ```.gitignore``` file at the top directory level and add ```*.sqlite3``` to it, so that any sensitive data in the development database doesn't get pushed to GitHub, and ```*.pyc``` and ```__pycache__/``` because the complied python code is not needed in version control
8. Create app: ```python3 manage.py startapp appname```.
9. Go to ```settings.py``` (this is located in the project folder) and add the appname to ```INSTALLED_APPS``` list
10. The creation of the app creates initial migrations for the model and these need to be migrated. Back in the commandline: ```python3 manage.py migrate```

Repeat steps 8, 9 and 10 throughout development as you create further apps within the project. When models are created or updated during development, the changes also need to be made and migrated using ```python3 manage.py makemigration``` and ```python3 manage.py migrate```. Remember you will need to do the migrations on the production database as well. To view the local version of the project before deployment to heroku, use ```python3 manage.py runserver```, and open the port 8000 when it pops up.

### Create the app on [Heroku](https://id.heroku.com/login) and attach the database:

1. Sign in to/create account on Heroku, and "create app". If you don't have an account, then set one up: Click the Sign up button in the header, fill out the form and Click Create Free Account when done. You will receive an email, click the link to confirm. Then you will be brought to page called SET YOUR PASSWORD. Enter password, click SET PASSWORD AND LOG IN. Will then show welcome page, click on CLICK HERE TO PROCEED, then click Accept to accept the terms of service. Then click on "Create new app". If you do have an account then Sign In to your account and go to the Dashboard. Click on "New" on the top right of the screen and then "Create new app"

2. Under App name, enter the name of the application. Note: the name must be unique, so you would not be able to name it the same as the already deployed version

3. Then choose the Region and click "Create app"

4. Attach the database: go to the Resources tab, Add-ons and then search for 'Heroku Postgres'. Add and choose e.g. Hobby Dev

5. Back in the workspace, create a new file called ```env.py``` to store the environment variables. The file should be in the top level directory, and it should also be added to the ```.gitignore``` file to ensure it does not get pushed to GitHub as it contains sensitive information

6. In env.py:

    - import os
    - ```os.environ["SECRET_KEY"] = '```generate a secret key and paste it here'

7. Back in Heroku, go to Settings tab, Config Vars, click Reveal Config Vars. Add `SECRET_KEY`, `AWS_ACCESS_KEY_ID`, `AWS_SECRET_ACCESS_KEY`, `DATABASE_URL`, `EMAIL_HOST_PASS`, `EMAIL_HOST_USER`, `STRIPE_PUBLIC_KEY`, `STRIPE_SECRET_KEY`, `USE_AWS` and paste in the value from the ```env.py``` file

8. In the workspace go to the ```settings.py``` file and do the following (no need if using this project's settings.py file):

    - add ```import``` os underneath where it says ```from pathlib import Path```
    - underneath this, ```import dj_database_url```
    - and then add a conditional statement to import the ```env.py``` when in the development environment.

    ```python
    if os.path.isfile('env.py'):
    import env
    ```

    This means the environment variables in ```env.py``` are used while in the development workspace, but if not in the development environment then it will use the ones set in Heroku.

    - update the value for ```SECRET_KEY``` to get it from ```env.py``` or Heroku: ```SECRET_KEY = os.environ.get('SECRET_KEY')```
    - update the ```DATABASES``` section so that it connects to Heroku Postgres database on the deployed site (where there is a DATABASE_URL config var), and to the development sqlite3 in the local environment:

    ```python
        if 'DATABASE_URL' in os.environ:
        DATABASES = {
                'default': dj_database_url.parse(os.environ.get('DATABASE_URL'))
            }
        else:
            DATABASES = {
                'default': {
                    'ENGINE': 'django.db.backends.sqlite3',
                    'NAME': BASE_DIR / 'db.sqlite3',
                }
            }
    ```

    When you need to connect to the Postgres database from the local development environment (e.g. to run migrations, create a superuser, etc.), you can adjust the above as needed so that you connect to Postgres. You will need to add the DATABASE_URL value to connect, but remember not to commit this to the repo as it should remain secret.

9. Attach to the Postgres database (adjust in settings.py as needed, and use the database_url key but do not commit it) and in the command line, make the migrations to the Heroku Postgres database: ```python3 manage.py migrate```

10. Then import the data using the fixtures files. Repeat the following command, with appropriate file name for each fixture file (categories, products, counties, markets) to import the data to the Postgres database: ```python3 manage.py loaddate filename```. Note the categories file must be imported before products, and counties before markets as they contain the foreign key information.

11. After doing the above, revert the DATABASES settings back as shown in step 8 above, so that production is connected to Postgres and development attached to local sqllite3 database.

### Add allowed hosts and create Procfile:

1. In ```settings.py```, find the ```ALLOWED_HOSTS``` list and add the heroku appname to it: ```ALLOWED_HOSTS = ['yourherokuappname.herokuapp.com', 'localhost']```. This is so that the Heroku hostname is recognised and Django will allow it to run the project

2. Create a file named ```Procfile```, this must be at the top level directory

3. Inside the Procfile add ```web: gunicorn projectname.wsgi```. This is so that Heroku knows how to run the project


### Inital Deployment:

1. Add all the changes above, commit them and push them to GitHub using ```git add```, ```git commit -m "commit msg"``` and ```git push``` commands in command line

2. Go to Heroku and in Config vars, add ```DISABLE_COLLECTSTATIC``` with a value of 1, for the initial deployment.

3. In the Deploy Tab, go to Deployment method and click GitHub

    - If have not connected to GitHub previously:
        
        - Underneath, it will show a section called Connect to GitHub, with a button at the bottom called “Connect to GitHub”. Press this button.

        - A pop up will ask you to Authorize Heroku’s access to your GitHub – click to Authorize, then enter your password and Confirm Password

        - The pop up will close and in the Connect to GitHub section it will show your GitHub username and a box to search for the repository to connect to.

    - If have already connected to GitHub you do not need to do the above and it should show your GitHub username and a box to search for the repo name as above

    - Enter the repo-name in the box and press Search

    - Underneath, it will display the repo: ```yourGitHubUsername/your-github-repo-name```, then press "Connect"     

    - Once connected it will show: Connected to ```yourGitHubUsername/your-github-repo-name``` by ```yourGitHubUsername```

4. Underneath the Connect section, there are two options "Automatic deploys" or "Manual deploy"

    - Automatic – future pushes to GitHub will mean Heroku automatically builds a new version of the app with the pushed changes

    - Manual – the app is not automatically updated with future pushes to GitHub but these can be manually made if needed.

    - Click, Deploy Branch. I deployed using Manual. The logs will show the dependencies and requirements being installed. When done, the page will refresh and say “Your app was successfully deployed” with a View button.

#### To do the above setps 3 & 4 through command line instead:

- Use command ```heroku login -i``` and enter you username and password when prompted. You will see confirmation in the terminal that you are logged in.

- Set the remote for the app on heroku using command heroku ```git:remote -a APP-NAME```. You should see confirmation that the remote has been set to the heroku remote for that app.

- Push to heroku to do the deployment, using command ```git push heroku main``` (when you push to the repo on github you will use command ```git push origin main```)

- You will see the build log in the terminal and after it has completed it will confirm the deployment was done, with the version number and the url for the website

*The rest of the process is the same regardless of whether the deployment was done through Heroku dashboard or via the command line:*

5. In Heroku, Click the Open app (or View button if still in the Deploy tab in Heroku) to view the app – it opens in a new window. For the initial deployment the static and media files have not been used but the database information should be there.

**To add AWS for hosting static and media files:**

If you don't have an account, create one, if you do, log in.

#### Create Bucket to Store the Files:

1. From services, go to S3 and Buckets, and Create bucket

2. Type in the name of the bucket (keep it similar to project name to avoid confusion), select the region, uncheck 'block all public access' (it needs to be public to access the static files) and Create the bucket

3. Go to Properties tab, scroll down to 'Static website hosting', click Edit. Select 'Host a static website', fill in default index.html and error.html (we won't be using these) and press Save

4. Then go to the Permissions tab and scroll down to 'Cross-origin resource sharing (CORS)'. Click Edit and paste in the following: 

```python
[ { "AllowedHeaders": [ "Authorization" ], "AllowedMethods": [ "GET" ], "AllowedOrigins": [ "*" ], "ExposeHeaders": [] } ]
```

5. Still in Permissions, scroll to the 'Bucket policy' section and select 'Policy generator' (opens in a new tab). In the Policy Type, select 'S3 Bucket Policy'. In Principal, type in * (to all all). In the Action dropdown, select 'Get Object'. And in Amazon Resources Name (ARN), paste in the code from the other tab, it will look like: ```arn:aws:s3::your-bucket-name```. Then click 'Add Statement'. Then click 'Generate Policy'. Copy the code in the 'Policy JSON Document' and paste it into the Bucket policy editor window in the other tab. Before pressing save, add ```/*``` onto the end of the bucket ARN in the Resource key (this is to allow access to all resources in the bucket). Then click Save.

#### Create a User to access the Bucket:

1. From services, go to IAM and User groups, and Create group

2. Give the group a name (e.g. ```manage-c-market``` so it is clear it's related to this project and the bucket created earlier), click Create Group
Create the policy that will be used to access the bucket. In Permissions. click on 'Add permissions' and then 'Create inline policy'. Go to the JSON tab and click on 'Import managed policies'. In the search box, type in S3, then from the resulting list select 'AmazonS3FullAccess' and press Import. In the JSON box, update the "Resource" key so that we allow access to just the bucket and everything in it. Update it from "Resource": "*" to the below, using the ARN:

3. Create the policy that will be used to access the bucket. In Permissions. click on 'Add permissions' and then 'Create inline policy'. Go to the JSON tab and click on 'Import managed policies'. In the search box, type in S3, then from the resulting list select 'AmazonS3FullAccess' and press Import. In the JSON box, update the "Resource" key so that we allow access to just the bucket and everything in it. Update it from ```"Resource": "*"``` to the below, using the ARN:

```python
"Resource": [
                "arn:aws:s3:::bucket-name",
                "arn:aws:s3:::bucket-name/*"
            ]
```

Then click 'Next: Tags', then 'Next:Review', then give the policy a Name and Description, then click Create Policy. 4. Then go to User Groups, choose the group created in step 2, then in the Permissions tab choose Add Permission and Attach policies. Find the policy just created in step 3, and click Add Permission. 5. Then go to the Users page (from the side menu), click Add Users. Fill in the User name (e.g. c-makret-static-files-user) and click the option for 'Access key - Programmatic access', click Next, add the user to the group created in step 2, click the next buttons until you get to Create user 6. Download the csv file which contains the access key and secret access key for this user. Make sure to download as it won't be available again

#### Upload Media Files to AWS:

1. In AWS, go to S3 and locate the bucket created earlier. Create a new folder called 'media' inside the bucket.

2. Inside this folder, click Upload and select the media files (download them from GitHub) to upload - these are the product images, market images, and home page images.

#### Add settings and environment variables for S3:

1. Back in the workspace, install boto3 and django-storages: ```pip3 install boto3 pip3 install django-storages```, update ```requirements.txt``` and in ```settings.py``` add ```'storages'``` to the ```INSTALLED_APPS```

2. Go to settings.py and add the following (no need to do so if using this project's settings.py file):

```python
if 'USE_AWS' in os.environ:
    AWS_STORAGE_BUCKET_NAME = 'bucket-name'
    AWS_S3_REGION_NAME = 'your bucket region'
    AWS_ACCESS_KEY_ID = os.environ.get('AWS_ACCESS_KEY_ID')
    AWS_SECRET_ACCESS_KEY = os.environ.get('AWS_SECRET_ACCESS_KEY')
    AWS_S3_CUSTOM_DOMAIN = f'{AWS_STORAGE_BUCKET_NAME}.s3.amazonaws.com'

    STATICFILES_STORAGE = 'custom_storages.StaticStorage'
    STATICFILES_LOCATION = 'static'
    DEFAULT_FILE_STORAGE = 'custom_storages.MediaStorage'
    MEDIAFILES_LOCATION = 'media'

    STATIC_URL = f'https://{AWS_S3_CUSTOM_DOMAIN}/{STATICFILES_LOCATION}/'
    MEDIA_URL = f'https://{AWS_S3_CUSTOM_DOMAIN}/{MEDIAFILES_LOCATION}/'
```

This tells Django which bucket to communicate with, where the static files will be coming from in production (the bucket name followed by .s3.amazonaws.com), to use S3 to store the static files when collectstatic is run, and to store uploaded images in S3 (references custom_storages.py which outlines these locations) 3. In Heroku, add ```Config vars``` for ```AWS_ACCESS_KEY_ID``` (value from csv file downloaded earlier), ```AWS_SECRET_ACCESS_KEY``` (value from csv file downloaded earlier), and ```USE_AWS``` (set to True so that the above settings are used in production).

#### To add Stripe for payments:

This project uses Stripe to handle payment processing (currently set up for test payments only). Stripe can be set up as follows:

1. Go to [Stripe](https://stripe.com/gb) and Sign up for an account, or Sign in if you already have one

2. Go to the developers dashboard and from the menu at the side, select API keys. Underneath Standard Keys you will see a Publishable key and a Secret key (note you can toggle between Test and Live keys. This project is currently set up with test keys and would need to be switched over to live keys if it was being launched as a live shop)

3. Add the following to your ```env.py```

```python
os.environ['STRIPE_PUBLIC_KEY'] = 'replace this with Publishable key from Stripe'  
os.environ['STRIPE_SECRET_KEY'] = 'replace this with Secret key from Stripe'
```

4. Add the same variables to the Heroku Config Vars

5. In settings.py add the following code:

```python
STRIPE_CURRENCY = 'gbp'
STRIPE_PUBLIC_KEY = os.getenv('STRIPE_PUBLIC_KEY', '')
STRIPE_SECRET_KEY = os.getenv('STRIPE_SECRET_KEY', '')
```

#### To add Email Service for Sending Emails:

This project uses Gmail to send emails for account sign ups etc., and order confirmation emails in production. (Emails are printed to the terminal in development.) Gmail for sending emails can be set up as follows:

1. Either create an account or sign into Gmail and go to Settings, then 'Accounts and Import' and then 'Other Google Account Settings'

2. Go to the Security tab and under Signing into Google, select to turn on 2-Step Verification, follow the steps to verify yourself to turn this on

3. Now under this same heading there will be a new option called App passwords, click on this (may need to enter password again) and set up the new app password: under 'select app' choose Mail and under 'select device' choose other and enter a name, e.g. Django, or something simialar, to identify this password. Then click on GENERATE

4. The next screen will show the app password for the device, copy this

5. In Heroku config vars, add two new variables of ```EMAIL_HOST_PASS```, value will be the app password copied above and ```EMAIL_HOST_USER```, with a value equal to the email address that you set the app password on. (These variables are not needed in env.py because this is for production emails only)

6. In settings.py, add the below to get the Gmail account and app password set up to send emails in production, and print emails to the terminal in development (this assumes there is a DEVELOPMENT variable in development environment and no such variable in Heroku):

```python
if 'DEVELOPMENT' in os.environ:
    EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'
    DEFAULT_FROM_EMAIL = 'dummyemailaddress@example.com'
else:
    EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
    EMAIL_USE_TLS = True
    EMAIL_PORT = 587
    EMAIL_HOST = 'smtp.gmail.com'
    EMAIL_HOST_USER = os.environ.get('EMAIL_HOST_USER')
    EMAIL_HOST_PASSWORD = os.environ.get('EMAIL_HOST_PASS')
    DEFAULT_FROM_EMAIL = os.environ.get('EMAIL_HOST_USER')
```

### Further Deployments during Development and for Final Deployment:

During development for future deployments:

1. Ensure ```DEBUG``` in ```settings.py``` is set to ```False``` (or to ```'DEVELOPMENT' in os.environ```, if you have a DEVELOPMENT environment variable in your env.py and no such variable in the Heroku Config vars)

2. Ensure all changes are pushed to GitHub

3. In Heroku remove the ```DISABLE_COLLECTSTATIC``` config var once you have static files and have set up AWS bucket and user.

4. Follow steps 4 and 5 from the Initial Deployment section above to deploy and view the updated deployed app. Note: if the Heroku dashboard doesn't have the option to connect to GitHub (functionality removed as of 16th April 2022 but may be reinstated), then follow the command line instructions outlined there instead.

## Forking the GitHub Repository

The repository can be forked on GitHub, this creates a copy of the repository that can be viewed or amended without affecting the original repository. This can be done using the following steps:

1. Login to [GitHub](https://github.com/)

2. Locate the relevant repository on GitHub. [This is the cMarket repo](https://github.com/RiyadhKh4n/cmarket)

3. At the top right of the repository (under your avatar) locate the Fork button and click this button

4. You should now have a copy of the repository in your own GitHub account, to which you can make changes

5. To run the project locally, you will need to create an ```env.py``` file with the environment variables [`SECRET_KEY`, `DATABASE_URL`, `STRIPE_PUBLIC_KEY` and `STRIPE_SECRET_KEY`] and install the requirements from the ```requirements.txt``` file using ```pip3 install -r requirements.txt```

## Making a Local Clone
 
1. Log in to GitHub and locate the [GitHub Repository](https://github.com/RiyadhKh4n/cmarket)
2. Under the repository name, click "Clone or download".
3. To clone the repository using HTTPS, under "Clone with HTTPS", copy the link.
4. Open Git Bash
5. Change the current working directory to the location where you want the cloned directory to be made.
6. Type `git clone`, and then paste the URL you copied in Step 3.
 
    $ `https://github.com/RiyadhKh4n/cmarket.git`
 
7. Press Enter. Your local clone will be created.
 
```shell
$ git clone https://github.com/RiyadhKh4n/cmarket.git
> Cloning into `CI-Clone`...
> remote: Counting objects: 10, done.
> remote: Compressing objects: 100% (8/8), done.
> remove: Total 10 (delta 1), reused 10 (delta 1)
> Unpacking objects: 100% (10/10), done.
```
 
Alternatively, if using Gitpod, you can click below to create your own workspace using this repository.
 
[![Open in Gitpod](https://gitpod.io/button/open-in-gitpod.svg)](https://gitpod.io/#https://github.com/RiyadhKh4n/cmarket)

You will need to also install all required packages in order to run this application on Heroku, refer to [requirements.txt](requirements.txt)
* Command to install this apps requirements is `pip3 install -r requirements.txt`

You will also need the following environment variables [`SECRET_KEY`, `DATABASE_URL`, `STRIPE_PUBLIC_KEY` and `STRIPE_SECRET_KEY`] in `env.py` 
 
# Credits

During the process of project development, there have been various sources that gave me idea how to do a particular feature or fix a bug. The following are the sources that I got knowledge from:

- [Stack Overflow](https://stackoverflow.com/)
- [Django Allauth](https://django-allauth.readthedocs.io/en/latest/installation.html)
- [Django Docs](https://docs.djangoproject.com/en/4.0/)
- [Code Institute](https://codeinstitute.net/) course materials and the Boutique Ado Walkthrough Project.
- [Bootstrap](https://getbootstrap.com/)
- [Crispy Forms](https://django-crispy-forms.readthedocs.io/en/latest/)

## Code

### Acknowledgements
* [Tim Nelson](https://www.linkedin.com/in/travel-tim-nelson/) - My Mentor
* Tutor Support
* Slack community
 
