from fastapi import APIRouter, HTTPException, status
from database.database import product_collection  
from bson import ObjectId
from model.model import Product  

router = APIRouter()

@router.put("/products/{product_id}", response_model=Product)
async def update_product(product_id: str, product: Product):
    updated_product = await product_collection.update_one(
        {"_id": ObjectId(product_id)}, {"$set": product.dict()}
    )

    if updated_product.modified_count == 0:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Product not found or no changes made")

    return await product_collection.find_one({"_id": ObjectId(product_id)})
