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

## Development
TO BE COMPLETED

### Database
TO BE COMPLETED

### Page Construction
- **Django Templates**
I used Django templates to build my pages. The head, logo, navigation bar, navigation if the user is connected and the footer are filled in the base.html document. 
The stylesheet is called by the link {% static 'css/style.css' %} so that all pages regardless of their location. The pages for logging in, registering or logging out of the user account are not in the same folder as the Home page for example.  
The different content pages use this document to load common elements such as the footer or the navigation, among others. The content pages only contain their own content.

TO BE COMPLETED

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

2. **If the user is logged in :**
- Book the game
- Your booking
- Log out

A small icon of a man is displayed as well as the user name is displayed at the login.
TO BE COMPLETED avec un screenshot

### Features
-__Header__
The header is composed of the OUTscape game logo, the navigation menu (collapsed for mobile and bar for computer) and the menu for connected users.
-__Footer__
The footer is composed of links to the game's social networks, Facebook and Instagram.   
There are also links to my GitHub as well as the copyright with the current year.

TO BE COMPLETED

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
TO BE COMPETED

### Softwares
- **Illustrator**
The logo was created with Illustrator software in order to create a vector file capable of being printed in high resolution as well as being displayed on a website with a mini weight. In addition, the vector format allows for a responsive image, as it adapts to different screen sizes.

- **InDesign**
The wireframes were made with InDesign software. This is not the software commonly used on this kind of file, but I know this software well because I've been using it for years, I feel at ease on it and I spend less time making the wireframes with this software than with a more common online solution.

### Django Libraries
TO BE COMPLETED

## Credits
TO BE COMPLETED

### Content
TO BE COMPLETED

### Media
1. **Logo**
The logo is created by me.

2. **Pictures**
- Home page picture : [Pexels.com](​​https://www.pexels.com/fr-fr/photo/photo-a-faible-angle-de-la-tour-de-grande-hauteur-513594/)
- Game page picture : 
[Pexels.com](​​https://www.pexels.com/fr-fr/photo/la-nouvelle-eglise-de-berlin-3662115/)

### Special thanks
TO BE COMPLETED
