# RESTAPI
 API README

This API documentation explains how to set up, run, and use the REST API. The API allows you to manage and retrieve information about persons in this system.
Table of Contents

1 Requirements
2   Setup
3   Running the API
4   Using the API
    i.  Create a New Person
    ii. Retrieve All Persons
    iii.Retrieve a Specific Person
    iv. Update a Person
    v.  Delete a Person
    vi. Filter Persons by Name
5   API Endpoints
6   Response Format

----------------------------------------------------------------------------------------------

1. Requirements

    - Python 3.11.4
    - Django 4.2.5
    - Django REST framework (latest version)

2. Setup

    - Clone this repository to your local machine:
    
    terminal:
        git clone https://github.com/njokuchidinma/restapi.git
        cd restapi

    - Install the required Python packages:

    terminal:
        pip install --upgrade pip //if you are using linux(debian distro)
        pip install django
        pip install djangorestframework

    - Apply database migrations to create the database tables:

    terminal:
        python manage.py makemigrations
        python manage.py migrate


3. Running the API

    - Start the development server:

    terminal:
        python manage.py runserver

    - The API will be available at http://localhost:8000/.


4. Using the API

    - Create a New Person
    To create a new person, send a POST request to the /user_id/ endpoint with the following data:

        json
        {
        "name": "Ode Roller",
        "age": "23"
        "place of birth": "yola"
        }

    - Retrieve All Persons
    To retrieve a list of all persons, send a GET request to the /user_id/ endpoint.
    
    - Retrieve a Specific Person
    To retrieve information about a specific person, send a GET request to the /user_id/{id}/ endpoint, where {id} is the person's unique identifier.

    - Update a Person
    To update information about a specific person, send a PATCH request to the /user_id/{id}/ endpoint with the data you want to update:

        json

        {
        "name": "Updated Name"
        }

    - Delete a Person
    To delete a specific person, send a DELETE request to the /user_id/{id}/ endpoint.

    - Filter Persons by Name
    You can filter persons by name by sending a GET request to the /user_id/?name={name} endpoint, where {name} is the name you want to filter by.

6. API Endpoints
    - http://localhost/api/user_id/

    POST /api/user_id/: Create a new person.
    GET /api/: Retrieve a list of all persons or filter by name.
    GET /api/user_id/{id}/: Retrieve information about a specific person.
    PATCH /api/user_id/{id}/: Update information about a specific person.
    DELETE /api/user_id/{id}/: Delete a specific person.

7. Response Format
    The API responses adhere to the following format:

        json

        {
        "status": "success",
        "data": { ... }
        }

    In case of an error, the response format will be:

        json

        {
        "status": "error",
        "data": { ... }
        }

This README.md provides an overview of setting up, running, and using the RESTAPI based on the provided code. 

