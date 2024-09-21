from fastapi import APIRouter, HTTPException, status
from database.database import product_collection  
from bson import ObjectId

router = APIRouter()

@router.delete("/products/{product_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_product(product_id: str):
    delete_result = await product_collection.delete_one({"_id": ObjectId(product_id)})

    if delete_result.deleted_count == 0:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Product not found")
    
    return {"detail": "Product deleted successfully"}
