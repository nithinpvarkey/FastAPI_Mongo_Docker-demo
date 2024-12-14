from fastapi.middleware.cors import CORSMiddleware
from fastapi import FastAPI, Request, Response
from fastapi.responses import HTMLResponse, FileResponse, JSONResponse
from pathlib import Path
from pymongo import MongoClient
import os

app = FastAPI()

# Add CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Allow all origins for testing; restrict this in production
    allow_credentials=True,
    allow_methods=["*"],  # Allow all methods (GET, POST, etc.)
    allow_headers=["*"],  # Allow all headers
)

# MongoDB Configuration
MONGO_URL_LOCAL = "mongodb://admin:password@localhost:27017"
DATABASE_NAME = "my-db"

client = MongoClient(MONGO_URL_LOCAL)
db = client[DATABASE_NAME]

# Serve index.html
@app.get("/", response_class=HTMLResponse)
async def get_index():
    return FileResponse(Path(__file__).parent / "index.html")

# Serve profile picture
@app.get("/profile-picture")
async def get_profile_picture():
    return FileResponse(Path(__file__).parent / "images/profile-1.jpeg")

# Get user profile
@app.get("/get-profile")
async def get_profile():
    user = db.users.find_one({"userid": 1}, {"_id": 0})
    if user:
        return JSONResponse(content=user)
    return JSONResponse(content={})


# Update user profile
@app.post("/update-profile")
async def update_profile(request: Request):
    user_data = await request.json()
    user_data["userid"] = 1

    db.users.update_one({"userid": 1}, {"$set": user_data}, upsert=True)
    return JSONResponse(content=user_data)