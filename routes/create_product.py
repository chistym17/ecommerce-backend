from fastapi import APIRouter, HTTPException, status
from model.model import Product 
from database.database import product_collection
from utils import converter
router = APIRouter()

@router.post("/products", response_model=Product, status_code=status.HTTP_201_CREATED)
async def create_new_product(product: Product):
    product_data = product.dict()
    print(product_data)

    try:
        new_product = await product_collection.insert_one(product_data)
        created_product = await product_collection.find_one({"_id": new_product.inserted_id})

        if created_product is None:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Product not found after creation")
        
        return converter(created_product)
    except Exception:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Error while creating product")


