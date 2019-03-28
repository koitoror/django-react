# CLOTHE-STORE
[![Build Status](https://travis-ci.org/koitoror/django-react.svg?branch=ch-setup-continuous-coverage)](https://travis-ci.org/koitoror/django-react) [![Coverage Status](https://coveralls.io/repos/github/koitoror/django-react/badge.svg?branch=ch-setup-continuous-coverage)](https://coveralls.io/github/koitoror/django-react?branch=ch-setup-continuous-coverage) [![Codacy Badge](https://api.codacy.com/project/badge/Grade/7a80a9487009409896d40951636ff8aa)](https://www.codacy.com/app/koitoror/django-react?utm_source=github.com&amp;utm_medium=referral&amp;utm_content=koitoror/django-react&amp;utm_campaign=Badge_Grade)
### Prerequisites
the development process utilized the postgres database
install pipenv using pip
```
pip install pipenv
```

**set up the database with a user who has the privileges**
```
- psql postgres
- CREATE DATABASE your_database;
- CREATE USER your_user WITH ENCRYPTED PASSWORD 'your_password';
- ALTER ROLE your_user CREATEDB;
- GRANT ALL PRIVILEGES ON DATABASE your_database TO your_user;
```
### Insatallation
clone the repository
```
git clone https://github.com/koitoror/django-react.git
``` 
cd into the django-react directory and run the command to install all requirements from Pipfile.lock
```
pipenv install
```
Activate the virtual environment
```
pipenv shell
```
Run the tests
```
python manage.py test
```
To activate the server
```
python manage.py runserver
```
## API endpoints
```
POST /api/v1/clothes
GET /api/v1/clothes
GET /api/v1/clothes/<int:id>
PUT /api/v1/clothes/<int:id>
DELETE /api/v1/clothes/<int:id>
```
## Built with

[Django Rest Framework](https://www.django-rest-framework.org/) - Django