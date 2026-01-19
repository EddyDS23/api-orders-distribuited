from pydantic import BaseModel, Field

from uuid import UUID

class OrderItemInputDTO(BaseModel):
    product_id:str = Field(...,min_length=1)
    quantity:int = Field(...,gt=0,le=100)
    unit_price:float = Field(...,gt=0)


class OrderItemOutputDTO(BaseModel):
    id:UUID
    product_id:str
    quantity:int
    unit_price:float
    subtotal:float


class UpdateItemInputDTO(BaseModel):
    quantity:int
    

