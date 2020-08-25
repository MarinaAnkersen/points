# Expected points REST API project
## Description
This project is implemented using Flask and is a REST API for expected and
actual points in Premier League current season. The application is
containerised using Docker. There is no ETL yet and project is using static
data files.
## Installation
Start by ensuring that you have Docker:
```
docker -v
```
and Docker Compose:
```
docker-compose -v
```
Build the image:
```
docker-compose build
```
Once the build is done, fire up the container:
```
docker-compose up -d
```
Run the following commands to create database and seed it with initial data:
```
docker-compose exec goals python3 manage.py recreate_db
docker-compose exec goals python manage.py seed_db
```
Try one of the endpoints out locally:
http://localhost:5001/users
## Running the tests
Run the tests using:
```
docker-compose exec goals python -m pytest "project/tests"
```
disable warnings:
```
docker-compose exec goals python -m pytest "project/tests" -p no:warnings
```
run with coverage report generation:
```
docker-compose exec goals python3 -m pytest "project/tests" -p no:warnings --cov="project" --cov-report html
```
## Flask Admin
Open the following to update local environment data on the go:
http://localhost:5001/admin/

Make sure container is up if not run the following command:
```
docker-compose up -d
```
## Swagger
API documentation can be found here (when the above completed and
  local environment is up and running):
http://localhost:5001/doc/
## Deployment
The application has been deployed to heroku. Here are the steps:
* Sign up for a Heroku account (if you don’t already have one)
* Create new application using Heroku UI
* Provision a new Postgres database with the hobby-dev plan
* Go to the Deploy tab and Select the Deployment method - GitHub
* Create git heroku remote using Terminal:
```
heroku git:remote -a <your heroku app name>
```
* Make a git push:
```
git push heroku master
```
* Go to the Deploy tab in Heroku UI again and click Deploy Branch in
Manual Deploy section
* Run the following in your Terminal window in order to seed the database
with some data:
```
heroku run python manage.py recreate_db --app <your heroku app name>
heroku run python manage.py seed_db --app <your heroku app name>
```
* Open an app clicking the button in the right top corner
## Demo
Heroku deployed app:
* https://vast-mountain-75503.herokuapp.com/matches
* https://vast-mountain-75503.herokuapp.com/teams
* https://vast-mountain-75503.herokuapp.com/users
