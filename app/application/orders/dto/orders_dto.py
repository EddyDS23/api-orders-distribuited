from pydantic import BaseModel, ConfigDict
from uuid import UUID

class OrderCreateInputDTO(BaseModel):
    user_id:UUID
    items:list[str]

class OrderResponseDTO(BaseModel):
    order_id:UUID
    status:str
    total:float
    items:list[str]

    model_config = ConfigDict(from_attributes=True)
    