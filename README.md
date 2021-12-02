# **FlyWatch**

![Mock up FlyWatch](images-readme/mockimageFlywatch.PNG)

## **FlyWatch** 

Welcome to FlyWatch.

Come to our website to find the most exclusives watches in the market.
It works with Stripe to make the process easier and safer.

This is not an online store therefore, it will not process any order.
It's the final project from the code institute software development course.

If you have any feedback or questions, head over to my GitHub contact details and feel free to reach out to me.

---
<a></a>

## Table of contents 
* [UX](#ux)
    * [User Goals](#user-goals)
    * [User Stories](#user-stories)
    * [Site Owners Goals](#site-owners-goals)
    * [User Requirements and Expectations](#user-requirements-and-expectations)
        * [Requirements](#requirements)
        * [Expectations](#expectations)
    * [Design Choices](#design-choices)
        * [Fonts](#fonts)
        * [Colors](#colors)
        * [Structure](#structure)
* [Wireframes and Flowcharts](#wireframes-and-flowcharts)
    * [Wireframes](#wireframes)
    * [Flowcharts](#flowcharts)
    * [Database Structure](#database-structure)
* [Features](#features)
    * [Existing Features](#existing-features)
    * [Features to be implemented](#features-to-be-implemented)
* [Technologies used](#technologies-used)
    * [Languages](#languages)
    * [Libraries and Frameworks](#libraries-and-frameworks)
    * [Tools](#tools)
* [Testing](#testing)
* [Bugs](#bugs)
* [Deployment](#deployment)
    * [Local Deployment](#local-deployment)
    * [Heroku Deployment](#heroku-deployment)
* [Credits](#credits)

--- 

<a name="ux"></a>

## **UX**

<a></a>

### **User Goals**

The home page should be very attractive in order to take the possible customer to an order.
The webstore should work well on all devices.
The webstore should contain information of all producuts shown.
The payment should be easy, quick and safe.

<a></a>

### **User Stories**

As a user:

A user wants the webstore to be very attractive so they can make an order.
A user wants to have information on the products that is shown on the webstore.
A user wants to see any sale either on the product or for delivery.
A user wants to make a payment online with credit cards.
A user wants to look for watches based on price, brand or other category.

### **Site owners Goals**

As an owner:

The owner wants to sell the products available on the webstore.
The owner wants to make the webstore popular on the internet.
The owner wants to see all the orders made through the website.
The owner wants to be able to upload or delete a products on their website.
The owner wants to the possibility of updating a product on the website.

<a></a>

<a></a>

### **User Requirements and Expectations**

<a></a>

#### Requirements

The webstore has to be easy to be navigated on.
The webstore have to have colors with contrast.
The products on the website have to easy to be found.
Images of the products have to be up to date.

<a></a>

#### Expectations

The webstore will not have broken pages when displayed in differents devices such as tablets, iphones and laptops.
The webstore has to have its links working and that the links take the customer to the right and expected place.
Webstore is in line with the customer's journey.
The website has show the products prices and the prices updated when the customer change their order.

<a></a>

### **Design Choices**

The main colours of the webstore is black and white. 

I used the [Coolors](https://coolors.co/ "Coolors.co") to come up with the color pallette.

<a></a>

#### Colors

Main colors used for the webstore is:

- White (#fff)
- Black (#000)

Other than these main colors there are a few other colors that dont make huge difference to the website.

<a></a>

#### Fonts

The font used for this website was the 'Roboto' from [Google Fonts](https://fonts.google.com/ "Google Fonts").

<a></a>

#### Structure

The webstore will start with the land page which contains the navigation on top of the background image.
Other than land page, the website also has the following pages:

* ### Home Page
    The home page is the main page of the project. It has to big pictures on the background of the website. It has an appealing design which can bring possible customers to an order.

* ### All Products
    It's a page with all the products that the website can offer the customers. The user can also filter the search by price, rating and brands.

* ### Brands
    It's a page that takes the customer to a specific chosen brand by the customer.

* ### Watches Around the World
    This page is a mini blog which contains more details about 3 specific products.

* ### Product detail
    This page is a page with the specific details of a product chosen by the customer.

* ### Bag
    This page has the products details along the price and delivery information. The customer can also update the order or delete it. 

* ### Checkout
    This page the customer can go ahead the their order and place the order.


## **Wireframes and Flowcharts**

<a></a>

### **Wireframes**
I have used [Balsamic](https://balsamiq.com/wireframes/) to create wireframes for my webstore.
[Landing / Home page](wireframes/home.png) 

### **Flowcharts**

To make the flowchart for the purchasing process I decided to use [Draw.io](https://draw.io/). The picture is down here below.

![Flowchart](images-readme/flowchart_process.png)


### **Database Structure**

For the project I set up 12 database Models which you can see in the image below. 
I have highlighted the relationships between the various models.

![Database Structure](images-readme/flywatch-data-flow.png)

<a></a>

## **Features**

<a></a>

### **Existing Features**

* Registration and Sign in function through allauth package from Django
* 2 big background images on the home page to call the customer attention
* A small blog with a few products to add more value to the webstore
* Checkout page that allows customer to place an order
* The add products function that makes a superuser add or delete a product to the webstore.

The user can also check the order history to check the previous orders that they have made.

There is a function in the bag that saves the products that were not bought through cache.

<a></a>

### **Features to be implemented**

* A super promotion that calculates and shows on the screen depending on the number of items that are being putting in the bag.
* A function that finds the prices of watches from different places and try to show the product price depending on the actual store income.
* A function that takes the photo of customer wrist and show a picture of the customer wearing the watch on the screen.


<a></a>

## **Technologies used**

<a></a>

* [HTML](https://en.wikipedia.org/wiki/HTML)
* [CSS](https://en.wikipedia.org/wiki/Cascading_Style_Sheets)
* [JavaScript](https://en.wikipedia.org/wiki/JavaScript)
* [Python](https://www.python.org/)

<a></a>

### **Libraries and Frameworks**

* [Font Awesome](https://fontawesome.com/)
* [Bootstrap](https://getbootstrap.com/)
* [Google Fonts](https://fonts.google.com/)
* [jQuery](https://jquery.com/)
* [Stripe](http://stripe.com/)

### **Tools**

* [Django](https://www.djangoproject.com/)
* [Git](https://git-scm.com/)
* [GitPod](https://www.gitpod.io/)
* [Heroku](https://www.heroku.com/)
* [Balsamic](https://balsamiq.com/wireframes/)
* [W3C HTML Validation Service](https://validator.w3.org/)
* [W3C CSS Validation Service](https://jigsaw.w3.org/css-validator/)


<a></a>

## Testing

## Table of contents 
* [Homepage](#homepage)
* [Products](#rooms)
* [Checkout](#reservation)
* [Profile](#profile)
* [Navigation](#navigation)
* [Social Media](#social-media)
* [Footer](#footer)
* [Reservations overview for Admin ](#reservations-overview-for-admin)

I have tested all the html files using [HTML Validator](https://validator.w3.org/).
I have tested all the CSS files using  [CSS Validator](https://jigsaw.w3.org/css-validator/).
I have tested all the JS files using [Javascript Validator](https://jshint.com/).

## Homepage
### **Responsiveness**
#### Where did I test?
I have tested the homepage on a few devices using inspect.
I have also tested how the home page display on microsoft edge and google chrome.

#### What did I test?
* Quality and display of hero image
* Display of carousel  

#### Conclusion
The 2 background images look good in all devices.
The carousel image from the blog page looks also good.  
The carousel from the blog page will not display on small screen which looks good.
Carousel resizes the height depending of the content of the slide.

### **Functionality**
Button 'Coming soon' on the home page works as it is expected to work taking the customer to the products page. 
Disabled carousel on the blog page for small screens. It looks better on big screens.  

The right/left carousel arrows work as it is expected to work. There are 2 pictures in this carousel.

### **Lighthouse report**






