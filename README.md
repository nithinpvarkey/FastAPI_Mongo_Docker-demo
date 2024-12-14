### FastAPI MongoDB DEMO Application
This project demonstrates a simple FastAPI application that serves an HTML page and interacts with a MongoDB database for managing a user profile. The application includes endpoints for fetching and updating the user profile, as well as serving static files (such as profile images).

##### features
1. Serve an index.html page with user profile details.
2. Fetch user profile from a MongoDB database.
3. Update user profile in the MongoDB database.
4. CORS enabled for cross-origin requests (for local development).

```
my_fastapi_app/
│
├── main.py                  # FastAPI application
├── index.html               # HTML page displaying the user profile
├── images/                  # Folder containing profile images
│   └── profile-1.jpg
└── Dockerfile               # Dockerfile to run MongoDB
└── docker-compose.yml       # Docker Compose configuration for MongoDB
```

#### Requirements
Python 3.8+
FastAPI
Uvicorn (ASGI server)
MongoDB (running locally or via Docker)
pymongo (MongoDB client)

### With Docker Compose

To start the application

Step 1: start mongodb and mongo-express

``` docker-compose -f docker-compose.yaml up```

You can access the mongo-express under localhost:8080 from your browser

Step 2: in mongo-express UI - create a new database "my-db"
Step 3: in mongo-express UI - create a new collection "users" in the database "my-db"
Step 4: start fastapi server
``` 
uvicorn main:app --reload 
```
Step 5: access the fastapi application from browser

      http://localhost:3000

