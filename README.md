Project Name: corporate asset tracker

App name: asset tracker

Project Description:

1.To track corporate assets such as phones, tablets, laptops and other gears handed out to employees.

2.The application might be used by several companies

3.Each company might add all or some of its employees

4.Each company and its staff might delegate one or more devices to employees for a certain period of time

5.Each company should be able to see when a Device was checked out and returned

6.Each device should have a log of what condition it was handed out and returned

Project Features:

I have Created a new virtual environment for this project and installed the required packages, which i have shared in 

requirements.txt file.

I have used Django Rest Framework for creating the API's.

I have used SQLITE3 database for this project.


I have used Django ORM for database operations.


I have used Django Admin for creating the admin panel.

I have used Django Serializer for creating the serializers.

I have used Django Rest Framework Spectacular for creating the API documentation.

I have used Django Rest Framework Simple JWT for creating the token based authentication.

I have used Pytest for creating the tests.

I have used Postman & swagger for testing the API's.


Steps to run the project:

1.Clone the project from the git repository. Even you can download the zip file from the git repository. (For your ease: I have 

included .env file)

git clone https://github.com/sazzadhossain881/corporate-asset-tracker.git

2.Create a virtual environment and activate it.

3.Install the required packages from requirements.txt file.

4.Run the following commands:

py manage.py makemigrations

py manage.py migrate

py manage.py createsuperuser

py manage.py runserver

Open the browser and hit the following url for performing API testing in swagger:

url: http://127.0.0.1:8000/api/docs/

Now, you have to authenticate yourself before doing any operation. To do that, hit the login endpoint and pass the email and 

password in the body. You will get a refresh token & access token in the response. Copy the access token and paste it in the 

authorize section of swagger. Now, you can perform any operation.

url: http://127.0.0.1:8000/api/users/login

You can also see the admin dashboard using the following url:

url: http://127.0.0.1:8000/admin/


Also, you can login to the admin panel using the following / superuser credentials & perform any database operation using my 

cool 

admin dashboard panel:

username: sajjad

password: s123

email: sajjadhossain342@gmail.com

You can also run the tests using the following command:

python manage.py test


Database Schema:

This implementation has 4 main models: Company, Device, Employee, and DeviceAssignment.


Company stores information about the companies using the app.

Device represents the corporate assets, with information such as their name, description, serial number, condition, and which 

company they belong to.

Employee represents the company's staff, with a one-to-one relationship to a Django user and a many-to-many relationship with 

the Device model, through the DeviceAssignment model.

DeviceAssignment represents the assignments of devices to employees, with a foreign key to both the Device and Employee models, 

as well as the assignment and return dates.
