from fastapi import APIRouter, HTTPException, status
from database.database import product_collection 
from bson import ObjectId
from utils import converter

router = APIRouter()

@router.get("/products")
async def get_all_products():
    products = await product_collection.find().to_list(100)
    print(products)
    return [{"id": str(product["_id"]), "name": product["name"], "description": product["description"], "price": product["price"]} for product in products]

@router.get("/products/{product_id}")
async def get_product_by_id(product_id: str):
    product = await product_collection.find_one({"_id": ObjectId(product_id)})

    if not product:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Product not found")
    
    return converter(product)
