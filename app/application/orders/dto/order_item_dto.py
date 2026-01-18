from pydantic import BaseModel, ConfigDict

from uuid import UUID

class OrderItemInputDTO(BaseModel):
    product_id:str
    quantity:int
    unit_price:float


class OrderItemOutputDTO(BaseModel):
    id:UUID
    product_id:str
    quantity:int
    unit_price:float
    subtotal:float

    