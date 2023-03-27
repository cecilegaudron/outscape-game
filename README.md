# OUTscape Game Berlin
TO BE COMPLETED

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
Admins also need to log in to the site in order to 
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
To BE COMPLETED

## VISUAL DESIGN
### Wireframes
TO BE COMPLETED avec les wireframes

### Graphic Charter
A graphic charter was created for the project. It contains all the information concerning the visual identity of the project, such as the multiple variations of the logo, the fonts used and the predominant colors. This graphic charter is the foundation of the OUTscape's visual identity and will be used on all communication media (business cards, flyers, stickers...), social networks and of course the website as well as various communications such as booking emails, confirmation emails, etc.
The graphic charter is available here : 
LINK TO THE HOSTED DOCUMENT - TO BE COMPLETED

### Logo
The logo was created by me. It represents a key, which is one of the symbols of escape games, along with the padlock. As the game is played outside, a skyline of the most representative buildings of the city of Berlin are arranged on the key. 
The punchline "The great escape" can be added to the logo on some communication supports to bring an added value.

### Fonts
The fonts used for the logo are not available for the web. I looked for other fonts that look like the ones used in the graphic.
TO BE COMPLETED

### Visual elements
- **Pictograms**
The pictograms on the home page were made by me. They make it possible to synthesize an idea such as the game takes place in the streets of the city or that the game can be played with several players.

- **Pictures**
The pictures on the homepage and on the Game page do not give any particular information about the activity offered for sale on the website, except the fact that the game takes place in Berlin. The Fernsehturm is the symbol of the city of Berlin. The other picture represents Gendarmenmarkt which is a tourist place where the players will have to go. The intention is to illustrate the website simply, to give a concrete visual to the Internet user.
In the future, photos will be taken by the organizers in a real situation in the city of Berlin with elements of the game in the hands of players.








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
