# ADD SITE NAME


[NAME - Deployed Site]()

---

![AmIResponsive]()

---

# User Experience (UX)
 
* ## Purpose 

    The primary purpose of the website is for the website owner to sell cryptocurrency related merchandise online.
   

* ## Aims 


* ## Users's Goals:
    - Buy crypto-related clothing online
    - Create a profile so that they can save their delivery information and also see their order history and qualify for customer benefits

* ## Site Owner's Goals:
    - Sell their crypto-related merchandise online
    - Maintain a list of registered users so they can send the newsletter to them, offering exclusive products and discounts
    
* ## Target Audience

    The global cryptocurrency market stood at a revenue of $1,542.9m in 2021, and with that, it has lead to a growth in crypto-related products like clothing and accessories. As a result, (WEBSITE's) target audience are for cryptocurrency enthusiasts who would like to purchase items of clothing related to their favourite coin/token. Our site offers a variety of products, from T-Shirts, Hoddies, Gym Vests and Hats allowing customers to have a range of options to chose from. 
 
* ## User Stories


* ## Development Method

    When developing (WEBSITE) I will take an Agile Approach. Meaning I will take an iterative approach to project management and software development helping me to deliver value faster and speed up development time. I will focus on working software over comprehensive documentation and responding to change over following a plan when creating the project.

    I also intergrated the MoSoCoW method which is a four-step approach to prioritizing which project requirements will provide the best return on investment (ROI). MoSCoW stands for Must- Have, Should-Have, Could-Have and Wont-Have. Using this method, I am able to label and order my User Stories into four categories, allowing me to know which ones to focus on and to ensure I meet my project vision and aims.
   

* ## Structure

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

## Design

* ### Wireframes

* ### ERD Diagram

    ![ERD Diagram]()

* ### Colour Scheme

    ![ColorSpace]()

* ### Typography


* ### Icons

    All icons used in the website were taken from [fontawesome](https://fontawesome.com/start)

    - #### Favicon

        The favicon for the site was created with [favicon.cc](https://www.favicon.cc/) 
 
# Features
 
Here describes the main features of the website and what the user can expect when viewing ~
 
## Existing Features:

## Future Features:

 
# Technologies
## Programming Languages:

- [HTML](https://developer.mozilla.org/en-US/docs/Learn/Getting_started_with_the_web/HTML_basics) - The HyperText Markup Language or HTML is the standard markup language for documents designed to be displayed in a web browser

- [CSS](https://en.wikipedia.org/wiki/CSS) - Cascading Style Sheets is a style sheet language used for describing the presentation of a document

- [Python](https://www.python.org/) - Python is an interpreted high-level general-purpose programming language. It is used when creating the backend functionality in Django

- [JavaScript](https://www.javascript.com/) - JavaScript is one of the core technologies of the World Wide Web, alongside HTML and CSS. Over 97% of websites use JavaScript on the client side for web page behavior, often incorporating third-party libraries
 
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

13. [ColorSpace](https://mycolor.space/):
    * Used to find the colour scheme of the site

14. [W3C Markup Validation Service](https://validator.w3.org/):
    * Used to validate HTML code

15. [W3C CSS Validation Service](https://jigsaw.w3.org/css-validator/):
    * Used to validate CSS

16. [JSHint](https://jshint.com/):
    * Used to validate any JavaScript code used

17. [Stripe](https://stripe.com/gb):
    * Used to handle payments (currently only set up to handle test payments)

18. [Gmail](https://mail.google.com/):
    * Used to send emails

19. [Mailchimp](https://mailchimp.com/en-gb/):
    * Used for the newsletter sign up form

20. [Facebook](https://www.facebook.com/):
    * Used to created the Facebook Business page

# Testing
 
Due to the size of the testing section for Cryptics I have created [TESTING.md](TESTING.md). It contains all my validator testing, lighthouse scores, Django Testing, User Story Testing, Manual Tests, Responsiveness Tests, Browser Compatibility Tests as well as any bugs.
 
[Link To TESTING.md](TESTING.md)
   
# Deployment
 
Deploying the project using Heroku:


## Making a Local Clone
 
1. Log in to GitHub and locate the [GitHub Repository]()
2. Under the repository name, click "Clone or download".
3. To clone the repository using HTTPS, under "Clone with HTTPS", copy the link.
4. Open Git Bash
5. Change the current working directory to the location where you want the cloned directory to be made.
6. Type `git clone`, and then paste the URL you copied in Step 3.
 
    $ `ADD LINK`
 
7. Press Enter. Your local clone will be created.
 
```shell
$ git clone ADD LINK
> Cloning into `CI-Clone`...
> remote: Counting objects: 10, done.
> remote: Compressing objects: 100% (8/8), done.
> remove: Total 10 (delta 1), reused 10 (delta 1)
> Unpacking objects: 100% (10/10), done.
```
 
Alternatively, if using Gitpod, you can click below to create your own workspace using this repository.
 
[![Open in Gitpod](https://gitpod.io/button/open-in-gitpod.svg)]()

You will need to also install all required packages in order to run this application on Heroku, refer to [requirements.txt](requirements.txt)
* Command to install this apps requirements is `pip3 install -r requirements.txt`
 
# Credits

## Code

### Acknowledgements
* [Tim Nelson](https://www.linkedin.com/in/travel-tim-nelson/) - My Mentor
* Tutor Support
* Slack community
 
