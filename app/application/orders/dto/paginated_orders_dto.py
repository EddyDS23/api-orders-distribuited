from pydantic import BaseModel,Field

from app.application.orders.dto.orders_dto import OrderResponseDTO

class PaginatedOrdersOResponseDTO(BaseModel):
    orders: list[OrderResponseDTO]
    page:int
    size:int
    total:int