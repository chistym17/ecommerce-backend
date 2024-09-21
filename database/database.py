import motor.motor_asyncio
from dotenv import load_dotenv
import os
import logging

# Load environment variables
load_dotenv()

# Get the MongoDB URL from environment
MONGO_URL = os.getenv("MONGO_URI")

# Connect to MongoDB
client = motor.motor_asyncio.AsyncIOMotorClient(MONGO_URL)

async def check_db_connection():
    try:
        # List databases to verify the connection
        databases = await client.list_database_names()
        logging.info(f"Connected to MongoDB! Available databases: {databases}")
        return True
    except Exception as e:
        logging.error(f"Failed to connect to MongoDB: {str(e)}")
        return False

database = client.products_db
product_collection = database.get_collection("products")
