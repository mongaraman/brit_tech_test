# brit_tech_test
Brit Insurance Technical Test

This is how I have setup this application.
> Database : PostgreSQL
> Backend (Python, Flask)
> Code Repo: Git
> Deployment on Heroku


Step-by-Step Guide

1. Setup project directory as brit_insurance_test
2. Setup a git repo at github as: brit_tech_test
3. Setup Heroku app as: brit_tech
4. Create a virtual environment:
> python3 -m venv venv
> source venv/bin/activate

Install necessary packages using requirements.txt:
> pip install -r requirements.txt

5. My project structure is:
brit_tech_test/
├── app/
│   ├── __init__.py
│   ├── db.py
│   ├── models/
│   │   ├── __init__.py
│   │   ├── user.py
│   │   └── product.py
│   ├── routes.py
│   └── templates/
│       ├── register.html
│       ├── login.html
│       └── products.html
├── venv/
├── manage.py
├── requirements.txt
├── .env
├── .gitignore
└── runtime.txt

6. Change .env > SQLALCHEMY_DATABASE_URI and DATABASE_URI to Heroku PostgreSQL URI
e.g 
SECRET_KEY=your_secret_key
SQLALCHEMY_DATABASE_URI=postgresql://username:password@localhost/dbname
DATABASE_URI=postgresql://username:password@localhost/dbname

These will be overridden by Heroku's environment variables later.


7. app/__init__.py is used to load the environment variables and initialize the app with the database.
8. In app/db.py am doing database initialization.
9. app/models/ contains models which contains db tables settings.
10. I have setup api routes in app/routes.py 
11. Specify the Python runtime version in runtime.txt:
12. requirements.txt includes the necessary packages.

How to Set Up Heroku?:
1. Login to Heroku and create a new app, in my case I created brit-tech

commands used:
> heroku login
> heroku create brit-tech

2. I added PostgreSQL add-on:

Command used:
> heroku addons:create heroku-postgresql:brit-dev

3. Set env variables (Optional):

Command used:
> heroku config:set SECRET_KEY=your_secret_key

4. Deploy code to Heroku

Commands used:

>git init
> heroku git:remote -a your-app-name
> git add .
> git commit -m "Your commit message"
> git push heroku main

5. Run database migrations on Heroku:

Command used:

> heroku run python manage.py db upgrade

My application was now deployed and accessible on Heroku, connected to the PostgreSQL database.

Notes

. Ensure your DATABASE_URL environment variable is correctly set by Heroku, which will override the local database URI.
. Secure your application by encrypting information such as username/passwords.
. Adjust your frontend templates as needed for better UX and styling.


Shortcuts and Assumptions:

. User input validation and error handling are minimal.
. Password reset and email verification are not implemented.
. No client-side form validation.
. The front end uses plain HTML without any SPA framework like React for simplicity.
. The app runs in debug mode on Heroku which is not recommended for production.

Conclusion

This setup provides a simple yet functional system with user registration,
login, and product summary functionalities, deployed on Heroku's free tier.
The backend handles all calculations, and data persistence is managed through PostgreSQL.






