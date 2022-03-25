**Inspect HOA backend challenge**

This is a simple flask repository with some endpoints and requires
a few more endpoints.

It follows a simple MVP (model-view-presenter) architecture with an additional data layer(repository) to access the data.

The view layer should only contain flask specific logic

The presenter layer should contain all the business logic

The model layer contains the business-models

Please fork this repository and add your solution to your new fork

The endpoints for users for this application already exist and follow the required architecture.

Please look at the code and following the same pattern, add an endpoint for the users where a user id is
taken in the url and the endpoint returns the user with that user ID

Also, create a new `hoas.py` file in the view and presenter directories and create
the endpoints which can get all the HOAs and add another HOA following the same pattern as the users endpoints

NOTE: The repositories and models for HOAs and users have been finished and should not require any change, if you do need to change it,
feel free and let us know why you chose to change it.

---

## Base URL: http://localhost:5100

## Request-1:

Create New User:
Endpoint: /create-user
Method: POST
Body:
{
"user_name": "Pradeep Suthar"
}

Response:
{
"msg": "User created successfully",
"responseCode": 201
}

---

## Request-2:

Get All Users:
Endpoint: /get-all-users
Method: GET

Response:
{
"data": [
{
"id": 1,
"username": "Ishan Kapoor"
},
{
"id": 2,
"username": "Atin Hindocha"
},
{
"id": 3,
"username": "Vishrut Malhotra"
},
{
"id": 4,
"username": "John Hancock"
},
{
"id": 5,
"username": "Jill Hancock"
},
{
"id": 6,
"username": "Pradeep Suthar"
},
{
"id": 7,
"username": "Pradeep Suthar"
}
],
"msg": "Users fetch successfully!",
"responseCode": 200
}

---

## Request-3:

Get User By ID:
Endpoint: /get-user?userId=6
Method: GET
Query Params: userId

Response:
{
"data": {
"id": 6,
"username": "Pradeep Suthar"
},
"mas": "User fetch successfully!",
"responseCode": 200
}

---

## Request-4:

Create New HOA:
Endpoint: /create-hoas
Method: POST
Body:
{
"name":"Pradeep",
"address":"Panjab Mohali"
}

Response:
{
"msg": "HOA created successfully",
"responseCode": 201
}

---

## Request-5:

Get All HOAS:
Endpoint: /get-all-hoas
Method: GET

Response:
{
"data": [
{
"address": "123 Main Street",
"id": 1,
"name": "United HOAs Limited"
},
{
"address": "123 Second Ave",
"id": 2,
"name": "HOAs R us"
},
{
"address": "999 Easy Street",
"id": 3,
"name": "Best HOA"
},
{
"address": "1 King St",
"id": 4,
"name": "Star HOA"
},
{
"address": "4 Third Ave",
"id": 5,
"name": "iHOA"
},
{
"address": "Panjab Mohali",
"id": 6,
"name": "Pradeep"
}
],
"msg": "HOAS fetch successfully!",
"responseCode": 200
}

---

## Request-6:

Get HOA By ID:
Endpoint: /get-hoas?hoasId=6
Method: GET
Query Params: hoasId

Response:
{
"data": {
"address": "Panjab Mohali",
"id": 6,
"name": "Pradeep"
},
"mas": "HOA fetch successfully!",
"responseCode": 200
}

---

## Step to set-up and run:

1. Extract this zip file in the directory.
2. Type the command for running the project in terminal or cmd. "sh startup.sh"
