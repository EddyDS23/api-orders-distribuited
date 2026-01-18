from pydantic import BaseModel, ConfigDict
from uuid import UUID

from app.application.orders.dto.order_item_dto import OrderItemInputDTO, OrderItemOutputDTO

from app.domain.entities.order import Order

class OrderCreateInputDTO(BaseModel):
    user_id:UUID
    items:list[OrderItemInputDTO]

class OrderResponseDTO(BaseModel):
    order_id:UUID
    user_id:UUID
    status:str
    total:float
    items:list[OrderItemOutputDTO]

    @classmethod
    def from_domain(cls, order:Order):
        items_dto = [
            OrderItemOutputDTO(
                id=item.id,
                product_id=item.product_id,
                quantity=item.quantity,
                unit_price=item.unit_price.amount,
                subtotal=item.subtotal.amount
            ) 
            for item in order.items
        ]

        return cls(
            order_id=order.id,
            user_id=order.user_id,
            status=order.status.value,
            total=order.total.amount,
            items=items_dto
        )