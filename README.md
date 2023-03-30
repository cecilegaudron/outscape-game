# OUTscape Game Berlin
TO BE COMPLETED

## Table of Contents
- [First Approach](#firstapproach)
- [Agile](#agile)
- [Visual Design](#visualdesign)
- [Development](#development)
- [Testing](#testing)
- [Technologies](#technologies)
- [Credits](#credits)

## First Approach
This milestone project is intended to be actually online in the spring 2023. The OUTscape website has been in the works for several months, but the game isn't completely finished yet, so the website is on hold. I decided to offer to make the OUTscape website for my milestone project 4 for Code Institute because it brought together the various technical constraints requested for the submission. Moreover, it is a concrete project and not only a work project. This is even more motivating and challenging!  

The website had to be created with Wordpress, I'm even happier and more motivated to do it from A to Z and to offer a completely customized work to the game creators. They will be able to take full advantage of the different techniques. 

### The project in a few words
My husband and a friend decided to start a small company to market a game they had in mind for some time: an outdoor escape game. It's a treasure hunt through the streets of Berlin where clues are hidden. The players are given a bag with different objects to be used to solve the different riddles. As they solve the riddles, the players advance through the streets of Berlin. The players must find the bust of Nefertiti that was stolen from the Neues Museum in Berlin.

### Existing Work
A homepage is already available and online at [OUTscape Berlin](https://outscapeberlin.de)
This is a small teaser to briefly present the game, while beginning the work of natural referencing. It is only a single page with different sections because the game is available in three languages (German, English and French).  

The website has two vocations: 
-	the first one is to propose an online booking of the game
-	the second is to be present on the Web and to be able to communicate about the game in a concrete way

### User Stories
1. **Customers**
There are several types of customers: 
- The group of Berliners
- The group of tourists wanting to see the city while having fun
- Tthe group of friends celebrating a birthday or a bachelorette/guest party
- The family with children or teenagers
- The team of colleagues in team building or team event

These customer groups are different but they have the same way of navigating the website. They want:
- Have concrete and practical information about the game
- Book a slot online to participate in the game
The creation of a customer account is necessary to make the reservation. This personal account then allows you to view the reservation, modify it or even cancel it. 
TO BE COMPLETED

2. **Admin**
Admins also need to log in to the site in order to :
- Confirm reservations submitted by users
- Modify reservations
- Cancel reservations (including those previously accepted)
- View upcoming reservations
- View customer information

### User Experience Design
The website must reflect the professionalism of the company. Customers must feel confident and want to purchase a gaming experience. The website must be clean, professional and trustworthy. And of course, it must be easy to use.  
In the future, customers will not need to create an account on the site to book a gaming slot. This feature is only present for the milestone project 4. It is important that the customer can purchase their gaming experience simply and quickly, without having to register and give all this information. 
TO BE COMPLETED

### Tree Structure
![TREE STRUCTURE](/media/screenshots/tree-structure.png)


## AGILE
I used the Agile methodology to organize my work.  
I created Epic stories that contain the most important tasks, which are also the biggest in terms of work to be done. Then I split these Epic stories into User stories that detail the different tasks to be done.  
Some User stories are labeled "MustHave", it's something that is very important and must be present in the final project.  
Others are labeled "ShouldHave", they are less important, but still interesting to implement. They may not be present in the final project. They will nevertheless be included in the project that will actually be put online for the game organizers.  
The iterations represent about one week of work each.

![Iterations board](/media/screenshots/agile-board.png)

- **Iteration 1**  
The iteration 1 can be consulted [here](https://github.com/cecilegaudron/outscape-game/milestone/1)

![Iteration 1](/media/screenshots/agile-iteration1.png)

- **Iteration 2**  
The iteration 2 can be consulted [here](https://github.com/cecilegaudron/outscape-game/milestone/2)
![Iteration 2](/media/screenshots/agile-iteration2.png)

- **Iteration 3**  
The iteration 3 can be consulted [here](https://github.com/cecilegaudron/outscape-game/milestone/3)
![Iteration 3](/media/screenshots/agile-iteration3.png)

## VISUAL DESIGN
### Wireframes
The wireframes represent the mobile view and the desktop view of the website.  

- **Mobile**  

![Mobile Wireframe 1](/media/screenshots/wireframe-mobile1.png)  

![Mobile Wireframe 2](/media/screenshots/wireframe-mobile2.png)  

![Mobile Wireframe 3](/media/screenshots/wireframe-mobile3.png)  

- **Desktop**  

![Desktop Wireframe 1](/media/screenshots/wireframe-desk1.png)  

![Desktop Wireframe 2](/media/screenshots/wireframe-desk2.png)  

![Desktop Wireframe 3](/media/screenshots/wireframe-desk3.png)  

### Graphic Charter
A graphic charter was created for the project. It contains all the information concerning the visual identity of the project, such as the multiple variations of the logo, the fonts used and the predominant colors. This graphic charter is the foundation of the OUTscape's visual identity and will be used on all communication media (business cards, flyers, stickers...), social networks and of course the website as well as various communications such as booking emails, confirmation emails, etc.  
The graphic charter is available here : [Graphic Charter](https://drive.google.com/file/d/1RP0541dsNWJTJjWlPPK5DmRFllAQtQWW/view?usp=share_link)

### Logo
The logo is created by me. It represents a key, which is one of the symbols of escape games, along with the padlock. As the game is played outside, a skyline of the most representative buildings of the city of Berlin are arranged on the key.  
The punchline "The great escape" can be added to the logo on some communication supports to bring an added value.

### Fonts
The fonts used for the logo are not available for the web. I looked for other fonts that look like the ones used in the graphic. 
"Kanit" has several styles which looks like the font used for "Berlin".  
Also the font “Lato” is closed to the “OUT” of OUTscape presents on the logo.

### Visual elements
- **Pictograms**
The pictograms on the home page were made by me. They make it possible to synthesize an idea such as the game takes place in the streets of the city or that the game can be played with several players.

- **Pictures**
The pictures on the homepage and on the Game page do not give any particular information about the activity offered for sale on the website, except the fact that the game takes place in Berlin. The Fernsehturm is the symbol of the city of Berlin. The other picture represents Gendarmenmarkt which is a tourist place where the players will have to go. The intention is to illustrate the website simply, to give a concrete visual to the Internet user.  
In the future, photos will be taken by the organizers in a real situation in the city of Berlin with elements of the game in the hands of players.  

All the graphic elements of the site have been treated with the [BulkResize](https://bulkresizephotos.com/en) site in order to reduce the quality/weight ratio and to save in webp format. They are hosted on Cloudinary.  

## Development
The organization of the website is very simple. It is a site composed of **four pages of content, accessible to all**:  
- Home page
- The Game
- Contact
- Book  

The **pages of connection** to the site for users:  
- Register
- Log in
- Log out  

The "Book" page displays the booking form when the user is logged in.  
**When the user is logged in, he/she has access to**: 
- Booking list
- Booking detail  
- Booking update 
- Booking delete  

The admins have **access to a space reserved for them**:  
- Log in
- Admin panel with dashboard, list of users, list of bookings...

A 404 page is also available.  

### Database  
- **Database Diagram**  

![Model Database](/media/screenshots/model-database.png)  

- **Custom Model**  
I decide to use the User Model without creating another one. Indeed, the admins don't want to store information about the users. They are more interested in knowing the information about the reservations.  

This custom model was therefore very important to create and had to be particularly adapted to expectations.  
- The "first_name" and "last_name" fields allow to know the identity of the customer for a better communication.  
- The "email" field eventually allows you to send personalized emails with appointment reminders.  
- The "mobile" field accepts up to 14 characters. The customer can be German (12 digit numbers) or French (10 digit numbers). It is requested to indicate its indicator for ease of use.  
- The "players" field only accepts entries between 1 and 10. Tickets can be entered up to 10 as well, but it is also possible not to enter any information.  
- The "bookdate" field allows to choose the date of the reservation. A calendar opens for users to make their choice. It is not possible to book for the same day, nor in the past.  
- The "timeslot" field displays several possible timeslots.  
I want it to be possible to book a time slot only once, so I chose to use the "constraints" method so that a "date" value coupled with a "time" value is considered unique.  
- The basic status of each new booking is by default 0, i.e. pending. A booking must be confirmed or declined by an admin.  

### Page Construction
- **Django Templates**
I used Django templates to build my pages. The head, logo, navigation bar, navigation if the user is connected and the footer are filled in the **base.html** document. 
The stylesheet is called by the link **{% static 'css/style.css' %}** so that all pages regardless of their location. The pages for logging in, registering or logging out of the user account are not in the same folder as the Home page for example.  
The different content pages use this document to load common elements such as the footer or the navigation, among others. The content pages only contain their own content.  

### Menu
The menu is presented in two ways: 
- **Collapsed Menu for mobiles**
In order to make the navigation pleasant for mobile users, the menu is presented in a collapsed way. More commonly called hamburger menu, this menu unfolds as soon as the user selects the "hamburger" icon with the three horizontal lines. 
- **Navigation bar for large screens**
For computer users, the navigation menu is presented in the traditional way, on a horizontal line with the different links presented.  

The link leading to the page for booking is deliberately highlighted. Indeed, it is the main action of the user on the website. This link must absolutely be put forward.  
Icons of social networks, Instagram and Facebook, are also present in the navigation because these platforms are very important nowadays and particularly in the context of an online sale. That's why these icons are present in the navigation.

### Menu for logged-in users
Below the navigation menu is a small brick-colored insert with the following information.
1. **If the user is not logged in :**  
- Register
- Login  

![Connected Navigation when the user is log out](/media/screenshots/connected-nav-logout.png) 

2. **If the user is logged in :**
- Book the game
- Your booking
- Log out  

![Connected Navigation when the user is log in](/media/screenshots/connected-nav-login.png) 

A small icon of a man is displayed as well as the user name is displayed at the login.  

### Features  
-__Header__  
The header is composed of the OUTscape game logo, the navigation menu (collapsed for mobile and bar for computer).  

-__Footer__  
The footer is composed of links to the game's social networks, Facebook and Instagram. There are also links to my GitHub as well as the copyright with the current year.  

-__Home Page__  
The Home page is the first page that users arrive on. I want this page to be nice, without too much text but so that the user understands quickly what site he is on and what he can expect. From the titles **h1** and **h2**, the user understands that this site is about a game taking place in Berlin.   
The image confirms the location in Berlin with the Fernsehturm which is one of the symbols of the city. The few lines below briefly explain the game before presenting the scenario at the bottom of the page.  
The three pictograms briefly present the three main features of the game: **an outdoor game, a game with two riddles and a game for 1 to 6 players**.
Two "Book the game" buttons allow the user to book his experience quickly during his reading.  

-__The Game__  
The Game page answers questions users may have: What is it? How to play?  
The meeting place is indicated in the form of a map. The different questions are presented as an accordion for better readability.  

-__Contact__  
The contact page gives the different ways to contact (phone and email) the organizers in order to have additional information or to book a personalized game experience. When the game is launched and the site is actually online, this page will contain a contact form whose messages will be sent directly to the organizers' email box.  

-__Admin Panel__  
This space is reserved for the game administrators. They have the possibility to see the different bookings. They can confirm or cancel a booking.  
They can also access the users' information if they want to contact them.  
 
-__User Account__  
On this version of the project, users can create a user account. They can then connect and disconnect from it. This user account allows to make a booking, to consult it, to modify it and to cancel it.  

- __Booking Formular__  
It is accessible only to users logged in to their personal account. Different fields are to be filled in, allowing users to choose the date and time of the game, to indicate the number of players, the number of transport tickets if necessary, a specific comment and to fill in their personal information.  

- __Booking List and Booking Detail__  
When a user is logged in and a booking has already been made and confirmed by the admins, it is possible to view the booking information in the booking list. The user can only see his booking.  

-__Booking Management__  
The user can modify or delete his booking when he is logged in to his account. He can do this from his booking list and then from his booking details. He can of course perform these actions only on bookings he has made himself.  

-__Error Page__  
If a user wishes to access a page that is not referenced, a 404 page is displayed.  

-__User Messages__  
For each action of the user, whether he wants to create his account, log in, log out, a message appears below the navigation to inform him of the success of this operation or its failure. It is the same for actions related to reservations:  
- Creation of a reservation
- Modification of a booking
- Delete a booking  

![User Message](/media/screenshots/user-message.png) 

### Features Left to Implement
In the future version of the website, the organizers do not want users to need to create an account, nor do they need to log in to make a reservation. The organizers want to make the booking as easy as possible without having to create yet another customer account on a website. Moreover, this will eliminate the possible problems of keeping personal data. As soon as the game has been played, the personal informations of the customers will not be kept in the database.

-__Online payment__
Online payment is one of the most important features of the website after booking. It is very important that people can pay for the game when they book. This will be possible when the website goes live with Stripe.  
With calculation of the price to be paid if transport tickets are requested. 

-__User ratings and reviews__
After the game, users can receive an email with the possibility to give a rating and write a comment about their game experience. Both of these will then be posted on the website.

-__Sending emails to users__
For better communication with customers and to perfect the organization, it is more than essential that customers receive emails from the OUTscape game:
- Reservation request confirmation email
- Booking confirmation email with game scenario and practical information (meeting place, access map, sneakers and rain gear to bring, how to meet for the meeting, etc.) 
- Reminder email a few days before the scheduled date of the day
- Email confirmation of reservation changes and cancellations
- Thank you email after the game and request for feedbacks and ratings

-__Acceptance of cookies__
A banner will be present when the internet user arrives on the website. The internet user will be able to accept or decline cookies.

- __Addition of new pages__
For the site that will actually go live, new pages will be added:
- **General Terms and Conditions of Sale**: essential when using an online sales service in order to establish a clear contract with the user and the organizer
- **About**: a page to introduce the creators of the game, the origin of the idea, their background. This page is necessary to make the experience human, it is always more appreciable to book a service with someone who has been introduced to us. It also implies a notion of trust by removing the feeling of paying for the game without knowing if it's a scam, all this while keeping the professional side.

-__Translation of the website into German and French__
It is possible to play the OUTscape game in English, French or German. The site must therefore be available in these three languages. Small flags will be available in the navigation bar and in the collapsed menu.

-__Synchronization with Google Calendar__
So that the admins can save the appointments for the next bookings in their personal digital agenda, in order not to forget any appointment.

-__Management with Google Calendar__
For the owners of the game, it would be very interesting if they could manage their slots for the game. If there are days or times when neither organizer is available, this possibility should not be offered for booking.

-__Dual administrator account__
There are two owners of the game and it would be more interesting if each had their own space, even if the information is shared. For example, they will take turns to run the game. They should be able to assign certain reservations to each other so that everyone knows what they have to do. That each one can note on the agenda his unavailability to take care of the game :
- View and validate client comments following the game
- Consult and validate the notes given by the clients following the game
- Generate invoices by directly associating the information given by the client

-__Sending emails to admins__
Admins should also receive emails or alerts when a reservation is made. The confirmation must be done quickly, so the admins must be quickly, easily and automatically informed of a reservation request.  
Same for a modification request or a cancellation.

TO BE COMPLETED

## Testing
TO BE COMPLETED

### Validator Testing
- HTML
No errors were returned when passing through the official [W3C validator](https://validator.w3.org/nu/)
- CSS
No errors were found when passing through the official [Jigsaw validator](https://jigsaw.w3.org/css-validator/)
- JavaScript
No errors were found when passing through the official [JSHint validator](https://jshint.com/)
- Python
TO BE COMPLETED

### Lighthouse
I asked the Lighthouse tool to analyze the performance of my site.  
The results are satisfactory. I still need to fine-tune the SEO and accessibility results.  

![Lighthouse for mobile](/media/screenshots/lighthouse-mobile.png)  

![Lighthouse for desktop](/media/screenshots/lighthouse-desktop.png)  

### Unfixed Bugs
TO BE COMPLETED

## Deployment
The website has been deployed via Heroku.  
The project is created on GitHub with the 'gitpod full template' provided by Code Institute. [Code Institute Template](https://github.com/Code-Institute-Org/gitpod-full-template)  

The project name is *outscape*.  
The name of the app is *outscapebooking*.  

- **Install Django and supporting libraries**
On Gitpod, it is necessary to install Django and supporting libraries. I decide to follow the deployment steps proposed by Code Institute.
  1. Install Django4, psycopg2 and Cloudinary  

    > pip3 install 'django<4' gunicorn  
    > pip3 install dj_database_url psycopg2  
    > pip3 install dj3-cloudinary-storage  

  2. Then create the requirements file with the command :  

    > *pip3 freeze --local > requirements.txt*

- **Create an external database**  
ElephantSQL is the service of choice for creating an external database.
  1. Create a free account
  2. Create new instance
  3. Name the database with the project name
  4. Choose a geographical region
  5. Copy the URL of the database  

- **Create an app in Heroku**
  1. Create a new app
  2. Open the Settings tab
  3. Reveal Config Vars
  4. Add a new Config Var called *DATABASE_URL* and paste the external database URL as the value
  5. Add a new Config Var called *SECRET_KEY* and paste my Secret Key

- **Create the env.py file**  
This file contains the secret datas about the project.  
  > import os
  > os.environ["DATABASE_URL"] = "Paste the database URL"
  > os.environ["SECRET_KEY"] = "My Secret Key"

- **Prepare the environment**  
  1. Do a reference to the env.py on the settings file.  
    > import os
    > import dj_database_url
    >
    >if os.path.isfile("env.py"):
    >   import env

  2. Remove the secret key and link it to the SECRET_KEY variable on Heroku.  
    > SECRET_KEY = os.environ.get('SECRET_KEY')

  3. Comment out the old database section. And paste a new database paragraph and link to the DATABASE_URL variable on Heroku.  
    > DATABASES = {
    >   'default': dj_database_url.parse(os.environ.get("DATABASE_URL"))
    >}

  4. Make the migrations.

- **Create the media files stored**  
Cloudinary is the service used to stored the media.   

  1. Need to create an account
  2. Copy the API Environment Variable available in the dashboard
  3. In the env.py file, paste the API previously copied

    > os.environ["CLOUDINARY_URL"] = "cloudinary://************************"

  4. Create a Config Vars in Heroku and to paste the API previously copied as a value
  5. Create a new Config Vars with *DISABLE_COLLECTSTATIC* as key and *1* as value. I will remove this new entry at the end of the project.
  6. Add Cloudinary libraries to the installed apps in settings.py :  

    > 'cloudinary_storage',
    > 'cloudinary',

  7. Specify to Django to use Cloudinary to store media and static files

    > STATICFILES_STORAGE = 'cloudinary_storage.storage.StaticHashedCloudinaryStorage'
    > STATICFILES_DIRS = [os.path.join(BASE_DIR, 'static')]
    > STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')
    > 
    > MEDIA_URL = '/media/'
    > DEFAULT_FILE_STORAGE = 'cloudinary_storage.storage.MediaCloudinaryStorage'

  8. Link with the templates directory :

    > TEMPLATES_DIR = os.path.join(BASE_DIR, 'templates')

  9. Change the templates directory :

    > 'DIRS': [TEMPLATES_DIR],

  10. Add Heroku Hostname to *ALLOWED_HOSTS*
  11. Create three new folders : media, static and templates
  12. Create a new file with the name Procfile
  13. In the Procfile file, add the code :

    > web: gunicorn outscape.wsgi

- **Deployment on Heroku**
  1. On Heroku, choose GitHub as the deployment method
  2. Connect Heroku with the project on GitHub
  3. Be sure to select the *main* branch on the Manual Deploy section
  4. Click on the *Deploy branch* button

The site is live here : [OUTscape website on Heroku](https://outscapebooking.herokuapp.com/)

## Technologies
1. **Languages**
- HTML
- CSS
- JAVASCRIPT
- PYTHON
- MARKDOWN

2. **Cloud Services, Frameworks...**  
- [GitHub](https://github.com/), service to store the project  
- [Gitpod](hhttps://www.gitpod.io/), IDE for building the project  
- [Heroku](https://www.heroku.com/), for deploying the project  
- [Cloudinary](https://cloudinary.com/), images cloud  
- [ElephantSQL](https://www.elephantsql.com/), PostgreSQL databases service  
- [Gunicorn](https://gunicorn.org/), server for Django on Heroku  
- [Django 3.2](https://www.djangoproject.com/), Python Framework  
- [Bootstrap 5](https://getbootstrap.com/docs/4.3/getting-started/introduction/), front-end Framework  
- [PostgreSQL](https://www.postgresql.org/), open source database  
- [BulkResize](https://bulkresizephotos.com/en), for resizing images

3. **Libraries, Packages, Applications**  
- [Font Awesome](https://fontawesome.com/), icons website  
- [Google Fonts](https://fonts.google.com/), fonts website  
- [allauth](https://django-allauth.readthedocs.io/en/latest/), user accounts management  
- [dj_database_url](https://pypi.org/project/dj-database-url/), PostgreSQL library  for Django  
- [pyscopg2](https://www.psycopg.org/docs/), Database adapter for Django  
- [dj3-cloudinary-storage](https://pypi.org/project/dj3-cloudinary-storage/), Cloudinary integration to Django  

4. **Softwares**  
- Illustrator[OUTscape website on Heroku](https://outscapebooking.herokuapp.com/)
The logo was created with Illustrator software in order to create a vector file capable of being printed in high resolution as well as being displayed on a website with a mini weight. In addition, the vector format allows for a responsive image, as it adapts to different screen sizes.

- InDesign[OUTscape website on Heroku](https://outscapebooking.herokuapp.com/)
The wireframes were made with InDesign software. This is not the software commonly used on this kind of file, but I know this software well because I've been using it for years, I feel at ease on it and I spend less time making the wireframes with this software than with a more common online solution.

## Credits  
### Thank you  
- A special thank you to my mentor Rory Patrick Sheridan who helped me a lot to understand my problems, who encourages me and gives me good advice throughout the project.  
- A special thank you to my man who believes in me all the time and who thinks that what I do is great.  
- Thanks to the tutorial support for their technical help and their insight.  
- Thanks to my friends on Slack who helped me to solve problems in a few clicks.  

### Content  
I helped myself a lot with the [Codemy YouTube channel](https://www.youtube.com/playlist?list=PLCC34OHNcOtr025c1kHSPrnP18YPB-NFi). His explanations allowed me to understand the logic of Django and to appreciate it.  


### Media
1. **Logo**
The logo is created by me.

2. **Pictures**  
- Home page picture : [Pexels.com](​​https://www.pexels.com/fr-fr/photo/photo-a-faible-angle-de-la-tour-de-grande-hauteur-513594/)  
- Game page picture : 
[Pexels.com](​​https://www.pexels.com/fr-fr/photo/la-nouvelle-eglise-de-berlin-3662115/)  

