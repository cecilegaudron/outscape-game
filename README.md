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
