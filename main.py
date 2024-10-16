from fastapi import FastAPI, Depends, UploadFile, HTTPException  # Make sure Depends is imported
from auth import get_current_user, login_user  # Import functions from auth.py
from model import model_pipeline  # Assuming this is where your model code is
from typing import Union
import io
from PIL import Image

app = FastAPI()

# Root route for testing
@app.get("/")
def read_root():
    return {"Hello": "World"}

# Login route to get access token
@app.post("/login")
def login(username: str, password: str):
    return login_user(username, password)

# A protected route that requires authentication
@app.get("/secure-data")
def secure_data(user_info: dict = Depends(get_current_user)):
    return {"message": "Secure data access granted", "user": user_info}

# Your existing image and text processing route
@app.post("/ask")
def ask(text: str, image: UploadFile, user_info: dict = Depends(get_current_user)):
    content = image.file.read()
    image = Image.open(io.BytesIO(content))
    result = model_pipeline(text, image)
    return {"answer": result}
