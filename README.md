# CoRider Assignment

## Flask Application for CRUD operations on MongoDB.

This is a simple Flask application that implements CRUD (Create, Read, Update, Delete) operations on a MongoDB database. The application provides REST API endpoints for managing users with the following fields:
- `id` (auto-genereted by mongoDB 12 char)
- `name` (user's name)
- `email` (user's email address)
- `password` (hashed password)
## Features

- **GET /users** - Retrieve all users from the database.
- **GET /users/{id}** - Retrieve a specific user by ID.
- **POST /users** - Create a new user.
- **PUT /users/{id}** - Update a user's details by ID.
- **DELETE /users/{id}** - Delete a user by ID.
## Technologies Used

- **Backend Framework**: ---

    [![My Skills](https://skillicons.dev/icons?i=python,flask&perline=5)](https://skillicons.dev)
---
- **Database**: ---

    [![My Skills](https://skillicons.dev/icons?i=mongodb&perline=5)](https://skillicons.dev)
---
- **Development Tools**:  ---

    [![My Skills](https://skillicons.dev/icons?i=git,github,postman&perline=5)](https://skillicons.dev)
---


## **Project Structure**
```bash
flask-mongo-crud/
│
├── app/
│   ├── __init__.py           # Initialize Flask app and MongoDB connection
│   ├── config.py             # Configuration file for app settings (e.g., MongoDB URI)
│   ├── models/
│   │   └── user.py           # User model for MongoDB
│   ├── routes/
│   │   └── user_routes.py    # REST API endpoints for user CRUD operations
│   ├── services/
│   │   └── user_service.py   # Logic for CRUD operations on the User resource
│  
│
├── .dockerignore             # Docker ignore file
├── Dockerfile                # Docker configuration file for containerization
├── requirements.txt          # Python dependencies
├── run.py                    # Entry point for the Flask app
├── vercel.json               # Vercel configuration for deployment
├── README.md                 # Project description and instructions
├── .gitignore                # Git ignore file

```

## Installation
1. Make Virtual ENV:
```bash
# In Linux
python3 -m vevn .venv
. .venv/bin/actiavte   # To activate virtual env
# In windows
python -m venv .venv
./.venv/Scripts/activate
```
2. Clone the repository:
   ```bash
   git clone https://github.com/AshishP-armar/CORider.git
   cd CORider
   ```

3. Install dependencies:
   ```bash
   pip install -r requirements.txt  # For Flask
   ```

