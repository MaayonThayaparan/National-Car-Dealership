# Final Project Template

The final project for this course has several steps that you must complete. 
To give you an overview of the whole project, all the high-level steps are listed below. 
The project is then divided into several smaller labs that give the detailed instructions for each step. 
You must complete all the labs to successfully complete the project.

## Project Breakdown

This is full stack project that deploys a website which is a central database of dealership reviews across the country. The website allows new and existing customers to look up different branches by state and look at customer reviews of the various branches. Customers are able to create an account and add their review for any of the branches. User management is implemeneted via Django user authentication system. IBMs Watson Natural Language Understanding service is used to determine whether reviews are positive, negative or neutral in tone. The Django admin site is configured for this project to add/remove makes and models of cars across dealerships. 

This is full stack project that utilizes the following:
- IBM Cloud account
- Watson Natural Language Understanding (NLU) service to analyze the sentiment/tone of reviews and display a happy, sad, or neutral review emoji. 
- IBM Cloudant used as database for dealers and reviews.
     - Use this endpoint to get all dealers: https://us-east.functions.appdomain.cloud/api/v1/web/bf04fca2-7896-4254-9996-ca1dcf1b7359/dealership-package/get-dealership
     - Use this endpoint to get dealers in a specific state: https://us-east.functions.appdomain.cloud/api/v1/web/bf04fca2-7896-4254-9996-ca1dcf1b7359/dealership-package/get-dealership?st=TX
          - Currently this endpoint is looking for dealers in Texas (TX)
          - change st=TX to another state initials to change the query
     - Use this endpoint to get reviews fora  specific dealer: https://us-east.functions.appdomain.cloud/api/v1/web/bf04fca2-7896-4254-9996-ca1dcf1b7359/dealership-package/get-review?id=15
          - Currently this endpoint is looking for reviews for dealer with id=15
          - change id=15 to another state initials to change the query
- IBM Cloud Functions used to manage dealers and reviews
- Django models and views to manage card model and make. These are stores in SQLite. Can be managed in the Django admin site. 
- Django proxy services and views to integrate dealers, reviews, and cars together. 
- 

**Prework: Sign up for IBM Cloud account and create a Watson Natural language Understanding service**
1. Create an IBM cloud account if you don't have one already.
2. Create an instance of the Natural Language Understanding (NLU) service.

**Fork the project Github repository with a project then build and deploy the template project**
1. Fork the repository in your account
2. Clone the repository in the theia lab environment
3. Create static pages to finish the user stories
4. Deploy the application on IBM Cloud

**Add user management to the application**
1. Implement user management using the Django user authentication system.
2. Set up continuous integration and delivery

**Implement backend services**
1. Create cloud functions to manage dealers and reviews
2. Create Django models and views to manage car model and car make
3. Create Django proxy services and views to integrate dealers, reviews, and cars together
 
**Add dynamic pages with Django templates**
1. Create a page that shows all the dealers
2. Create a page that show reviews for a selected dealer
3. Create a page that let's the end user add a review for a selected dealer

**Containerize your application**
1. Add deployment artifacts to your application
2. Deploy your application
