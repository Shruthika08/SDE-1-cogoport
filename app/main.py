# app/main.py

from fastapi import FastAPI
from .database import engine, Base  # Updated import
from .endpoints import router as config_router

# Create a FastAPI instance
app = FastAPI()

# Include the router from endpoints
app.include_router(config_router)
