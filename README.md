# Mood API using Django Restframework run in a Docker container

About this App
================
This is a web REST application with a '/mood' endpoint, which allows authenticated users, to POST current mood and GET their posted mood,
together with post stats when compared to other users.
The GET method retrieves all POSTed mood by the current authenticated user, the user's current streak(number of cuncurrent days
till today which the user has posted a mood) and also the maximum streak percentile attained by the user when compared to other registered
users.

Requirements
=================
Please see requirements.txt file.

How to use
=====================
Install requirements.

Navigate to the project folder via command line.

Run the server on your local machine using 'manage.py runserver'.

Goto to link http://127.0.0.1:8000/api/v1/mood/

Login using the link on the top right corner.

Demo login details:
username: admin
password: admin

Recommendation for running in production environment
=====================================================
I used the default sqlite database which you get from django, but you can you a different database just change the datbase connection 
setting in setting.py and run migrations.

Use redis to store the list of all max streak of users, to allow for speed in calculating the streak percentile when your
users incresase.

Use enviroment variable in the setting file to avoid exposing sensitive info.

Its advisable to version the API endpoints, to avoid failure with clients app already using our this current API endpoint incase we 
need to change some things like data type. We create a new enpoint with the new data and clients are given option to update to the new
version.

For scaling you can create multiple containers and distribute the load using NGINX load balancer. 

