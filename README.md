# National Car Dealership

## Description

This is full stack project that deploys a website which is a central database of dealership reviews across the country. The website allows new and existing customers to look up different branches by state and look at customer reviews of the various branches. Customers are able to create an account and add their review for any of the branches. User management is implemeneted via Django user authentication system. IBMs Watson Natural Language Understanding (NLU) service is used to determine whether reviews are positive, negative or neutral in tone. The Django admin site is configured for this project to add/remove makes and models of cars across dealerships. 

This is full stack project that utilizes the following:
- IBM Cloud account
- Watson Natural Language Understanding (NLU) service to analyze the sentiment/tone of reviews and display a happy, sad, or neutral review emoji. 
- IBM Cloudant used as database for dealers and reviews.
- IBM Cloud Functions used to manage dealers and reviews
     - Use this endpoint to get all dealers: https://us-east.functions.appdomain.cloud/api/v1/web/bf04fca2-7896-4254-9996-ca1dcf1b7359/dealership-package/get-dealership
     - Use this endpoint to get dealers in a specific state: https://us-east.functions.appdomain.cloud/api/v1/web/bf04fca2-7896-4254-9996-ca1dcf1b7359/dealership-package/get-dealership?st=TX
          - Currently this endpoint is looking for dealers in Texas (TX)
          - change st=TX to another state initials to change the query
     - Use this endpoint to get reviews fora  specific dealer: https://us-east.functions.appdomain.cloud/api/v1/web/bf04fca2-7896-4254-9996-ca1dcf1b7359/dealership-package/get-review?id=15
          - Currently this endpoint is looking for reviews for dealer with id=15
          - change id=15 to another state initials to change the query
- Django models and views to manage car model and make for different dealerships. These are stores in SQLite. Can be managed in the Django admin site. 
- Django proxy services and views to integrate dealers, reviews, and cars together.

![image](https://github.com/MaayonThayaparan/National-Car-Dealership/assets/43158629/0834dba8-df40-4752-95ab-fa045714daa6)


## Getting Started

### Dependencies
- Tested on Windows 10
- Tested on Python 3.12.0
- Download Python from: https://www.python.org/downloads/
- Requires Python packages: Django, Pillow, distro-info, virtualenv, Django psycopg2-binary

### Installation
- Download Python from: https://www.python.org/downloads/
- Download project from GitHub
- Open a new terminal and run following commands:
     - pip install django
     - python -m pip install Pillow
     - pip install --upgrade distro-info
     - pip install virtualenv
     - pip install Django psycopg2-binary
     - pip install ibm_cloud_sdk_core
     - pip install ibm_watson
     - pip install aiohttp
     - virtualenv djangoenv
     - source djangoenv/bin/activate
  
### Executing the Program
- Open terminal
- Navigate to the project folder then open the server folder
- Run the following commands:
     - python -m pip install -U -r requirements.txt
     - python manage.py makemigrations
          - If prompted to 'Please select a fix', select option '1-Provide a one-odd default now...'
          - Enter an integer value
     - python manage.py migrate
     - python manage.py runserver
- Last commmand will run the server. Open web browser and enter URL: http://localhost:8000/djangoapp

- Without being logged in, you can do the following:
     - View 'About Us' page
       ![image](https://github.com/MaayonThayaparan/National-Car-Dealership/assets/43158629/204ea253-14b0-4743-b8be-28b593ee0520)
     - View 'Contact Us' page
       ![image](https://github.com/MaayonThayaparan/National-Car-Dealership/assets/43158629/50746a1c-5dce-4457-a7fa-6fc9b9c69ed9)
     - View all dealers
       ![image](https://github.com/MaayonThayaparan/National-Car-Dealership/assets/43158629/7d6abb7b-2203-49cf-a8c9-e0dee4c5f069)
     - Filter dealers by State
       ![image](https://github.com/MaayonThayaparan/National-Car-Dealership/assets/43158629/824f6725-4e00-4f1f-9a1c-185b6a7fe71a)
     - Click on dealer to view reviews. NLU will display an emoji after analyzing the review tone. (NOTE: Alot of dealers don't have much data, look at 'Tempsoft Car Dealership' as I have populated data)
       ![image](https://github.com/MaayonThayaparan/National-Car-Dealership/assets/43158629/effab6b2-36b7-4c26-9e1f-36daacbb2ef5)
 
- Sign Up as new user.
     - Click the 'Sign Up' button in the top right.
     - Input values for all fields and click 'Sign Up'
       ![image](https://github.com/MaayonThayaparan/National-Car-Dealership/assets/43158629/a01e3423-0972-492f-8cff-a3535dce074f)
     - You are now signed in. You can logout by clicking the 'Logout' button.
       ![image](https://github.com/MaayonThayaparan/National-Car-Dealership/assets/43158629/ccce69d6-a978-4a9b-8473-d2b0b44fa5e0)

- Authorized user, you can do the following:
     - Go to a dealer and you will now have access to the 'Add Review' button
       ![image](https://github.com/MaayonThayaparan/National-Car-Dealership/assets/43158629/2dea4a39-374f-4c81-901e-fb9c85ee75fa)
     - Fill out review fields and click 'Submit'. (this will post to the review database)
       ![image](https://github.com/MaayonThayaparan/National-Car-Dealership/assets/43158629/dc92f8a8-8f43-4208-a978-4944fdac3f3f)
     - You will see the review added to the dealer page, and NLU will do the tone analysis
       ![image](https://github.com/MaayonThayaparan/National-Car-Dealership/assets/43158629/a39672f1-aea9-4f2e-afd1-576d299da493)


### Customize the Webpage
- Django admin site has been configured for this project.
- You can acces the admin site at: http://localhost:8000/admin
- A superuser has already been created, you can login as an admin using the below credentials:
     - username: root
     - password: root
- If the above superuser does not work, do the following:
     - Stop the server (Ctrl+c in terminal).
     - Run the following command in the project directory in terminal: python manage.py createsuperuser
     - Follow the onscreen prompts.
     - Run the server and login to the admin site using your newly created superuser.
- From the admin site, you can add/delete makes and models for different dealerships
- ![image](https://github.com/MaayonThayaparan/National-Car-Dealership/assets/43158629/2564d4e4-921d-40bb-973c-06f0994ae5c4)

- If you want to start from scratch, delete the db.sqlite3 file in the project folder.
- If you are going to change the models, ensure you run the following two commands before restarting the server:
     - python manage.py makemigrations
     - python manage.py migrate








 


