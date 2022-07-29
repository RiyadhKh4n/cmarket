# Testing

## [W3C Markup Validation Service](https://validator.w3.org/)

<details>
<summary>HTML Validation</summary>

Page                    | Image
--------------------    | ---------------
Whole Site              | ![site](documentation/testing/)
Home                    | ![home](documentation/testing/html-home.png)
Accounts                | ![acc](documentation/testing/html-accounts.png)
Products                | ![product](documentation/testing/html-products.png)
Product Details         | ![product-details](documentation/testing/html-product-details.png)
Bag                     | ![bag](documentation/testing/html-bag.png)
Checkout                | ![checkout](documentation/testing/html-checkout.png)
Wishlist                | ![wishlist](documentation/testing/html-wishlist.png)
Profile                 | ![profile](documentation/testing/html-profiles.png)
Product Management      | ![pm](documentation/testing/html-prod-man.png)
Contact                 | ![contact](documentation/testing/html-contact.png)
Newsletter              | ![newsletter](documentation/testing/html-news.png)
Privacy & T&C's         | ![ptc](documentation/testing/html-privacy.png)

</details>

## [W3C CSS Validation Service](https://jigsaw.w3.org/css-validator/)

![css](documentation/testing/css-validation.png)

## [JSHint Validator](https://jshint.com/)

<details>
<summary>JavaScript Validation</summary>

File                        | Result
--------------------        | ---------------
countryfield.js             | ![profiles](documentation/testing/js-countryfield.png)
quantity_input_script.html  | ![products](documentation/testing/js-quantity-script.png)
stripe_elements.js          | ![stripe](documentation/testing/js-stripe.png)

</details>
 
## [PEP8 Python Validation](http://pep8online.com/)

<details>
<summary>cMarket Main App</summary>

Python Files  | PEP8 result
------------- | -------------
settings.py   | ![settings.py file](documentation/testing/settings.png)
urls.py       | ![urls.py file](documentation/testing/cs-urls.png)
views.py      | ![views.py file](documentation/testing/cs-views.png)

</details>

<details>
<summary>Home App</summary>

Python Files  | PEP8 result
------------- | -------------
admin.py      | ![Home admin.py](documentation/testing/home-app.png)
app.py        | ![Home admin.py](documentation/testing/home-amin.png)
urls.py       | ![Home urls.py](documentation/testing/home-urls.png)
views.py      | ![Home views.py](documentation/testing/home-views.png)
forms.py      | ![Home forms.py](documentation/testing/home-form.png)
models.py     | ![Home models.py](documentation/testing/home-models.png)

</details>

<details>
<summary>Products App</summary>

Python Files  | PEP8 result
------------- | -------------
admin.py      | ![Products admin.py](documentation/testing/product-admin.png)
app.py        | ![Product admin.py](documentation/testing/product-app.png)
urls.py       | ![Product urls.py](documentation/testing/product-url.png)
views.py      | ![Product views.py](documentation/testing/product-views.png)
forms.py      | ![Product forms.py](documentation/testing/product-forms.png)
models.py     | ![Product models.py](documentation/testing/product-model.png)
widgets.py    | ![Product widgets.py](documentation/testing/product-widgets.png)

</details>

<details>
<summary>Bag App</summary>

Python Files  | PEP8 result
------------- | -------------
app.py        | ![apps.py](documentation/testing/bag-app.png)
urls.py       | ![urls.py](documentation/testing/bag-url.png)
views.py      | ![views.py](documentation/testing/bag-views.png)
contexts.py   | ![contexts.py](documentation/testing/bag-contexts.png)

</details>

<details>
<summary>Checkout App</summary>

Python Files  | PEP8 result
------------- | -------------
admin.py      | ![admin.py](documentation/testing/checkout-admin.png)
app.py        | ![apps.py](documentation/testing/checkout-apps.png)
urls.py       | ![urls.py](documentation/testing/checkout-urls.png)
views.py      | ![views.py](documentation/testing/checkout-views.png)
forms.py      | ![forms.py](documentation/testing/checkout-forms.png)
models.py     | ![models.py](documentation/testing/checkout-models.png)
signals.py    | ![signals.py](documentation/testing/chekcout-signals.png)

</details>

<details>
<summary>Profiles App</summary>

Python Files  | PEP8 result
------------- | -------------
app.py        | ![apps.py](documentation/testing/profiles-apps.png)
urls.py       | ![urls.py](documentation/testing/profile-urls.png)
views.py      | ![views.py](documentation/testing/profile-views.png)
forms.py      | ![forms.py](documentation/testing/profiles-forms.png)
models.py     | ![models.py](documentation/testing/profile-models.png)

</details>

<details>
<summary>Wishlist App</summary>

Python Files  | PEP8 result
------------- | -------------
app.py        | ![apps.py](documentation/testing/wishlist-app.png)
admin.py      | ![admin.py](documentation/testing/wishlist-admin.png)
urls.py       | ![urls.py](documentation/testing/wishlist-urls.png)
views.py      | ![views.py](documentation/testing/wishlist-views.png)
models.py     | ![models.py](documentation/testing/wishlist-models.png)

</details>

<details>
<summary>Root Level Files</summary>

Python Files            | PEP8 result
--------------------    | ---------------
custom_storages.py      | ![cs](documentation/testing/custom-storage.png)
manage.py               | ![manage.py](documentation/testing/manage.png)

</details>

<details>
<summary>Root Level Files</summary>

Python Files            | PEP8 result
--------------------    | ---------------
custom_storages.py      | ![cs](documentation/testing/custom-storage.png)
manage.py               | ![manage.py](documentation/testing/manage.png)

</details>

## Lighthouse Score

<details>
<summary>Results</summary>

Device                  | Lighthouse Score
--------------------    | ---------------
Desktop                 | ![desktop](documentation/testing/lighthouse-desktop.png)
Mobile                  | ![mobile](documentation/testing/lighthouse-mobile.png)

</details>

## User Story Tests

### General, site purpose, navigation:

1. As a visiting user I can easily find out what the purpose of the website is and learn more about the site owner and the products being sold so that I can decide to stay and browse or not

    ![home](documentation/testing/home-768.png)

2. As a site user I can navigate the site so that I can find the page I want to go to

    ![d.nav](documentation/testing/desktopnav.png)

3. As a user I can find the sites social media accounts so that I can follow them on social media to keep up to date with the business

    ![d.footer](documentation/testing/footerdesktop.png)

4. As a site user I can sign up to the newsletter so that I can stay informed and stay engaged with the shop

    ![news](documentation/testing/newsletter-425.png)

5. As a site user I can see a 'Page not found' page with consistent branding to the rest of the site, when I try to access a page in error so that I can find my way back to the website and know I have not left the website. Ensure page tells user which error they are getting.

    ![404](documentation/testing/404.png)

6. As a site user I can find the terms of use and privacy policy so that I can read these documents and have trust in the site

    ![privacy](documentation/testing/privacy-768.png)

7. As a user I can click on a back to top button so that I can get back to the top of the page without having to scroll

    I decided to not implement a Back To Top button within the site

8. As a user I can see a message confirming my actions (e.g. adding item to bag) so that I know my changes were received

    ![toasts](documentation/testing/toasts.png)

9. As a user I can quickly see which section of the website I am in from the main header so that I know which part of the website I am in and can navigate around easily

    Here the user is on the Contact Page which can be identified via the heading

    ![contact](documentation/testing/contact-320.png)

### Shop - Viewing Products:

10. As a site user I can easily view all the products in the shop so that I can see all the available products immediately without having to sort or filter or take any action

    ![shop](documentation/testing/product-768.png)

11. As a site user I can view an individual item details so that I can see the full details including the description and decide whether to buy

    ![prod-det](documentation/testing/product-details-768.png)

12. As a site user I can select a specific category of product so that I can view just the items in that category to make it easier to make a decision

    ![cat](documentation/testing/category.png)
    ![filter](documentation/testing/filter.png)

13. As a site user I can sort the products in the shop so that I can find what I'm looking for easier
    
    ![searcing](documentation/testing/searching.png)
    ![filter](documentation/testing/filter.png)

14. As a site user I can search for a product in the shop so that I can find a particular item quickly

    ![searcing](documentation/testing/searching.png)

15. As a user I can see the results for my filter option or search term so that I can quickly see how many products match my filter option/match my search term

    ![result](documentation/testing/results.png)

### Shop - Adding to/updating the cart:

16. As a site user I can add an item to my cart so that I can buy it

    ![bag](documentation/testing/bag-425.png)

17. As a site user I can select the quantity of an item before adding to my cart so that I can add multiple of that item at once

    ![a](documentation/testing/product-details-768.png)

18. As a site user I can see the total amount currently in my cart at all times so that I can keep track of how much I'll be spending

    ![cart](documentation/testing/cart-total.png)

19. As a site user I can see the items in my cart at any time so that I can check what I have already added to the cart

    ![bag](documentation/testing/bag-768.png)

20. As a site user I can adjust the quantity of a particular item in the cart so that I can buy more or less of the item directly from the cart

    ![bag](documentation/testing/bag-768.png)

21. As a site user I can remove an item from my cart so that I do not have to buy it if I've changed my mind

    ![remove-item](documentation/testing/remove-item.png)

### Shop - Payment & Checkout:

22. As a site user I can continue to the checkout process once I've decided on my purchase so that I can buy the items

    ![check](documentation/testing/checkout-768.png)

23. As a site user I can enter my delivery and payment details so that I can complete my purchase

    ![check](documentation/testing/checkout-768.png)

24. As a site user I can see the order summary while making payment so that I can still edit the details before payment if I made a mistake

    ![check](documentation/testing/checkout-768.png)

25. As a registered user I can save my delivery information when checking out so that it is saved to my profile for use with my next order

    ![profile](documentation/testing/profile-768.png)

26. As a site user I can see an order confirmation page so that I know that the order went through okay

    ![checkout-success](documentation/testing/checkout-success-new.png)

27. As a site user I can receive an email confirmation of my order so that I have this confirmation for my records

    ![order](documentation/testing/order-confirmation.png)

28. As a user I can see a preview of my shopping cart when I make changes so that I can easily see the new cart

    ![toasts](documentation/testing/toasts.png)

29. As a site owner I can ensure that an order is created once payment is made so that a customer does not make a payment, without an order being created in the database

    I decided to not include webhooks so this User Story has not been met

### User account setup, sign in and out:

30. As a site user I can sign up for an account so that I can enjoy the benefits of having an account with the site

    ![signup](documentation/testing/account-768.png)

31. As a site user I want to receive an email confirmation when I register so that I know my account registration was successful and secure

    ![ec](documentation/testing/ec.jpg)

32. As a registered user I can sign into my account so that I can access my profile to view all past orders

    ![profile](documentation/testing/profile-425.png)

33. As a registered user I can sign out of my account when finished so that I know I am signed out securely

    ![sign-out](documentation/testing/sign-out.png)

34. As a registered user I can easily see if I am signed into my account or not so that I know straight away if I need to sign in

    ![34](documentation/testing/user-story-34.png)

### User Profile:

35. As a registered user I can update my default delivery information in my profile so that the updated details are recorded for future orders

    ![35](documentation/testing/profile-empty.png)
    ![35](documentation/testing/profile-not-empty.png)

36. As a registered user I can see my previous orders in my profile so that I can see all the orders I made and can find details of a previous order

    ![36](documentation/testing/order-history.png)

37. As a registered user I can view details of a previous order so that I can check what was ordered and where it was delivered to

    ![37](documentation/testing/past-order.png)

38. As a registered user I can easily navigate within the My Account pages so that I understand what pages are available and can get to them easily and I know what page I am on

    ![my-account](documentation/testing/my-account.png)

### Admin for Shop Page:

39. As a website owner I can view all the products in the shop, even if they are not active, so that I can see an overview of all products, and so that I can edit inactive products

    ![admin](documentation/testing/admin-products.png)

40. As a website owner I can add a new product to the shop so that I can sell the product to customers

    ![pm](documentation/testing/product-man-425.png)

41. As a website owner I can edit the details of a product in the shop so that I can change the price, description etc. and customers will see the updated information

    ![e](documentation/testing/editing.png)
    ![e](documentation/testing/edit-product.png)

42. As a website owner I can turn on or off the active flag on a product so that I can add or remove it from appearing in the shop for customers when it is in/out of stock

    I decided not to implement this functionality

43. As a website owner I can delete a product so that it will not appear in the shop

    ![del](documentation/testing/delete.png)

44. As a website owner I can access the Django admin site for the categories so that I can add, edit or delete categories from here and new products for these categories can be added to the shop

    ![cat](documentation/testing/admin-cat.png)

45. As a site owner I can access the Django admin site for the products so that I can view, edit, delete products from here as well as from the website

    ![prod](documentation/testing/admin-product-page.png)

46. As a website owner I can see orders in the admin site so that I can access the order details and fulfil the orders

    ![order](documentation/testing/admin-order.png)

47. As a website owner I can add a product and the sku is created automatically so that the sku's for the products are standardised and I do not have to manually add a sku

    Decided not to implement the sku field in the product model

48. As a website owner I can have the sku of a product updated when the category is changed so that the sku of the product is reflects the new category

    Decided not to implement the sku field in the product model

### Admin for User Profiles:

49. As a site owner I can access the Django admin site for Profiles so that I can view user profiles

    ![profile](documentation/testing/50.png)

### Marketing / SEO

50. As a website owner I want my website to contain relevant keywords so that users searching for these keywords will be more likely to find my website in web search results

    ![meta](documentation/testing/metatag.png)

51. As a website owner I have a link to the Facebook business page on the website so that customers or visitors to the website can follow the Facebook page and I can generate more business through the Facebook page

    ![d.footer](documentation/testing/footerdesktop.png)
    ![fb](documentation/testing/facebook-page.png)

52. As a website owner I have relevant keywords included in the webpage metadata so that it helps improve SEO so that users searching for these keywords can find my website

    ![footer](documentation/testing/footerdesktop.png)

53. As a website owner I can have a sitemap.xml and robots.txt file created for the website so that search engines can crawl the essential pages of the site and therefore users can find the site when searching key terms in search engine searches

    ![sitemap](documentation/testing/sitemap-robots.png)

## Responsiveness Testing

<details>
<summary>Mobile (320px)</summary>

Page                    | Image
--------------------    | ---------------
Home                    | ![home](documentation/testing/homepage-320.png)
Accounts                | ![acc](documentation/testing/accounts-320.png)
Products                | ![product](documentation/testing/products-320.png)
Product Details         | ![product-details](documentation/testing/productdetails-320.png)
Bag                     | ![bag](documentation/testing/bag-320.png)
Checkout                | ![checkout](documentation/testing/checkout-320.png)
Wishlist                | ![wishlist](documentation/testing/wishlist-320.png)
Profile                 | ![profile](documentation/testing/profile-320.png)
Product Management      | ![pm](documentation/testing/product-man-320.png)
Contact                 | ![contact](documentation/testing/contact-320.png)
Newsletter              | ![newsletter](documentation/testing/newsletter-320.png)
Privacy & T&C's         | ![ptc](documentation/testing/privacy-320.png)

</details>

<details>
<summary>Mobile (375px)</summary>

Page                    | Image
--------------------    | ---------------
Home                    | ![home](documentation/testing/homepage-320.png)
Accounts                | ![acc](documentation/testing/accounts-320.png)
Products                | ![product](documentation/testing/products-320.png)
Product Details         | ![product-details](documentation/testing/productdetails-320.png)
Bag                     | ![bag](documentation/testing/bag-320.png)
Checkout                | ![checkout](documentation/testing/checkout-320.png)
Wishlist                | ![wishlist](documentation/testing/wishlist-320.png)
Profile                 | ![profile](documentation/testing/profile-320.png)
Product Management      | ![pm](documentation/testing/product-man-320.png)
Contact                 | ![contact](documentation/testing/contact-320.png)
Newsletter              | ![newsletter](documentation/testing/newsletter-320.png)
Privacy & T&C's         | ![ptc](documentation/testing/privacy-320.png)

</details>

<details>
<summary>Mobile (425px)</summary>

Page                    | Image
--------------------    | ---------------
Home                    | ![home](documentation/testing/homepage-425.png)
Accounts                | ![acc](documentation/testing/accounts-425.png)
Products                | ![prod](documentation/testing/products-425.png)
Product Details         | ![prod-det](documentation/testing/product-details-425.png)
Bag                     | ![bag](documentation/testing/bag-425.png)
Checkout                | ![check](documentation/testing/checkout-425.png)
Wishlist                | ![wish](documentation/testing/wishlist-425.png)
Profile                 | ![profile](documentation/testing/profile-425.png)
Product Management      | ![prod-man](documentation/testing/product-man-425.png)
Contact                 | ![cont](documentation/testing/contact-425.png)
Newsletter              | ![newsletter](documentation/testing/newsletter-425.png)
Privacy & T&C's         | ![ptc](documentation/testing/privacy-320.png)

</details>

<details>
<summary>Tablet (768px)</summary>

Page                    | Image
--------------------    | ---------------
Home                    | ![home](documentation/testing/home-768.png)
Accounts                | ![acc](documentation/testing/account-768.png)
Products                | ![prod](documentation/testing/product-768.png)
Product Details         | ![prod-d](documentation/testing/product-details-768.png)
Bag                     | ![bag](documentation/testing/bag-768.png)
Checkout                | ![check](documentation/testing/checkout-768.png)
Wishlist                | ![wishlist](documentation/testing/wishlist-768.png)
Profile                 | ![profile](documentation/testing/profile-768.png)
Product Management      | ![product-man](documentation/testing/product-man-768.png)
Contact                 | ![contact](documentation/testing/contact-768.png)
Newsletter              | ![news](documentation/testing/newsletter-768.png)
Privacy & T&C's         | ![ptc](documentation/testing/privacy-768.png)

</details>

<details>
<summary>Desktop (1024px & 1440px)</summary>

Page                    | Image
--------------------    | ---------------
Home                    | ![home](documentation/testing/homepage-1024.png)
Accounts                | ![acc](documentation/testing/accounts-1024.png)
Products                | ![prod](documentation/testing/products-1024.png)
Product Details         | ![prodd](documentation/testing/product-details-1024.png)
Bag                     | ![bag](documentation/testing/bag-page-1024.png)
Checkout                | ![check](documentation/testing/checkout-1024.png)
Wishlist                | ![wish](documentation/testing/wishlist-1024.png)
Profile                 | ![prof](documentation/testing/profile-1024.png)
Product Management      | ![prodman](documentation/testing/prod-man-1024.png)
Contact                 | ![cont](documentation/testing/contact-1024.png)
Newsletter              | ![news](documentation/testing/newsletter-1204.png)
Privacy & T&C's         | ![ptc](documentation/testing/pricacy-1024.png)

</details>

## Browser Compatibility Tests 

I will test cMarket on [Brave Browser](https://brave.com/), [Microsoft Edge](https://www.microsoft.com/en-us/edge) and [Firefox](https://www.mozilla.org/en-GB/firefox/new/):  

<details>
<summary>Brave Browser</summary>

Page                    | Image
--------------------    | ---------------
Home                    | ![home](documentation/testing/home-768.png)
Accounts                | ![acc](documentation/testing/account-768.png)
Products                | ![prod](documentation/testing/product-768.png)
Product Details         | ![prod-d](documentation/testing/product-details-768.png)
Bag                     | ![bag](documentation/testing/bag-768.png)
Checkout                | ![check](documentation/testing/checkout-768.png)
Wishlist                | ![wishlist](documentation/testing/wishlist-768.png)
Profile                 | ![profile](documentation/testing/profile-768.png)
Product Management      | ![product-man](documentation/testing/product-man-768.png)
Contact                 | ![contact](documentation/testing/contact-768.png)
Newsletter              | ![news](documentation/testing/newsletter-768.png)
Privacy & T&C's         | ![ptc](documentation/testing/privacy-768.png)

</details>

<details>
<summary>Microsoft Edge</summary>

Page                    | Image
--------------------    | ---------------
Home                    | ![home](documentation/testing/mic-home.png)
Accounts                | ![acc](documentation/testing/mic-account.png)
Products                | ![prod](documentation/testing/mic-prod.png)
Product Details         | ![prodd](documentation/testing/mic-prod-des.png)
Bag                     | ![bag](documentation/testing/mic-bag.png)
Checkout                | ![check](documentation/testing/mic-chekcout.png)
Wishlist                | ![wish](documentation/testing/mic-wishlist.png)
Profile                 | ![prof](documentation/testing/mic-prof.png)
Product Management      | ![prodman](documentation/testing/mic-prod-man.png)
Contact                 | ![cont](documentation/testing/mic-contact.png)
Newsletter              | ![news](documentation/testing/mic-newsletter.png)
Privacy & T&C's         | ![ptc](documentation/testing/mic-pricacy.png)

</details>

<details>
<summary>Firefox</summary>

Page                    | Image
--------------------    | ---------------
Home                    | ![home](documentation/testing/fire-home.png)
Accounts                | ![acc](documentation/testing/fire-account.png)
Products                | ![prod](documentation/testing/fire-products.png)
Product Details         | ![prodd](documentation/testing/fire-prod-det.png)
Bag                     | ![bag](documentation/testing/fire-bag.png)
Checkout                | ![check](documentation/testing/fire-checkout.png)
Wishlist                | ![wish](documentation/testing/fire-wishlist.png)
Profile                 | ![prof](documentation/testing/fire-profile.png)
Product Management      | ![prodman](documentation/testing/fire-prod-man.png)
Contact                 | ![cont](documentation/testing/fire-contact.png)
Newsletter              | ![news](documentation/testing/fire-newsletter.png)
Privacy & T&C's         | ![ptc](documentation/testing/fire-privacy.png)

</details>

## GitHub Issues

When developing the project, I used GitHub Issues as a way to track my work on GitHub, and make notes of any bugs or features that I needed to fix/implement.

- [Here](https://github.com/RiyadhKh4n/cmarket/issues?q=is%3Aissue+is%3Aclosed) you can find a list of all issues used for the development of cMarket 

## Bugs

- When the user completes their purchase, the overlay does not go above the footer or the fa-search in the navbar. I believe it is an issue to do with the z-index however this is something I will fix in later iterations of the project
