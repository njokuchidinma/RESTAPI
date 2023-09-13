RESTAPI Documentation

    This API documentation provides comprehensive information on how to set up, run, and use the API. The API allows you to manage and retrieve information about persons in the API.

--------------------------------------------------------------------------------  

Table of Contents:

1.   Request and Response Formats
2.   Sample Usage
3.   Known Limitations
4.   Local Setup and Deployment

-----------------------------------------------------------------------------------

1. Request and Response Formats:

  i.  Request Format:
        All requests to the API should follow the standard JSON format. Each endpoint may have specific data requirements in the request body.
        
   ii. Response Format :
        The API responses adhere to the following format:

                json

                {
                "status": "success",
                "data": { 
                    "name":"Peter",
                    "age":"43",
                    "place_of_birth":"LA"
                }
                }
        In case of an error, the response format will be:

            json

                {
                   "status": "error",
                   "data": {
                       "name":"Peter",
                       "age":43,
                       "place_of_birth":"LA"
                   }
                }
                

2. Sample Usage

    To illustrate how to use the API, here are some sample requests and expected responses:

   i.  Create a New Person & Using RUD(Other crud operations)
        - Request:
        You can use curl to make requests;
        ie using curl;
            POST:
                curl -X POST -H "Content-Type: application/json" http://localhost/api/user_id/ -d '{...data...}'
                example of this in use:
                curl -X POST -H "Content-Type: application/json" http://localhost/api/user_id/ -d '{"name":"Peter","age":43,"place_of_birth":"LA"}'
            GET:
                curl -X GET http://localhost/api/user_id/
            
            PUT:
                curl -X PUT -H "Content-Type: application/json" http://localhost/api/user_id/ -d '{...data...}' 
                example of this in use:
                curl -X PUT -H "Content-Type: application/json" http://localhost/api/user_id/ -d '{"name":"Updated Name","age":35,"place_of_birth":"New York"}'
            
            DELETE:
                curl -X DELETE http://localhost/api/user_id/
        
        ie using postman:
            POST:
                select POST:
                then put your endpoint:  http://localhost/api/user_id/
                select your format; ie Json;
                finally put your information;
                {
                    "name":"Peter",
                    "age":43,
                    "place_of_birth":"LA"
                }
                Then hit the SEND button.
            GET:
                select GET:
                then put your endpoint:  http://localhost/api/user_id/
                Then hit the SEND button.
            
            PUT:
                select PUT:
                then put your endpoint:  http://localhost/api/user_id/
                select your format; ie Json;
                finally put your information;
                {
                    "name":"Updated name",
                    "age":43,
                    "place_of_birth":"LA"
                }
                Then hit the SEND button.
            
            DELETE:
                select DELETE:
                then put your endpoint:  http://localhost/api/user_id/{id}
                Then hit the SEND button.
        Response:
            POST RESPONSE:
                json

                {
                    "status": "success",
                    "data": {
                        "name":"Peter",
                        "age":43,
                        "place_of_birth":"LA"
                    }
                }

            GET RESPONSE:
                {
                    "status": "success",
                    "data": [
                        {
                            "id": 1,
                            "name": "John",
                            "age": "30",
                            "place_of_birth": "London"
                        },
                        {
                            "id": 2,
                            "name": "Peter",
                            "age": "43",
                            "place_of_birth": "LA"
                        },
                        {
                            "id": 3,
                            "name": "dera21",
                            "age": "12",
                            "place_of_birth": "jabi"
                        },
                    ]
                  }

3.  Known Limitations

    Data Validation: 
        Though Django RestFramework offers various serializers for data validation, logic might require additional effort. Writing these logics turned out to be my biggest issue.

4.  Local Setup and Deployment:
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
        pip install --upgrade pip
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



This Documentation.md file provides comprehensive documentation for the RESTAPI, including details on endpoints, request and response formats, sample usage, known limitations, and setup instructions.
