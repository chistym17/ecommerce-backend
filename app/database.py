import motor.motor_asyncio
from dotenv import load_dotenv
import os

load_dotenv()

#Get the MongoDB URL 
MONGO_URL = os.getenv("MONGO_URL")

# Connect to MongoDB
client = motor.motor_asyncio.AsyncIOMotorClient(MONGO_URL)
database = client.products_db
product_collection = database.get_collection("products")
