#the product model for the db

from pydantic import BaseModel, Field
from typing import Optional

class Product(BaseModel):
    name: str = Field(..., title="Name", max_length=100)
    description: str = Field(..., title="Description")
    price: float = Field(..., gt=0)
    
class UpdateProduct(BaseModel):
    name: Optional[str]
    description: Optional[str]
    price: Optional[float]
