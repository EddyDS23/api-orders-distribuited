
from app.infrastructure.persistence.repositories.order_repository import OrderRepository

from uuid import UUID

class CancelOrderUseCase:

    def __init__(self,orderRepository:OrderRepository):
        self._orderRepository = orderRepository

    
    def execute(self,order_id:UUID) -> None:
        
        order = self._orderRepository.get_by_id(order_id)

        if not order:
            raise ValueError(f"Order {order_id} not found")
        
        order.cancel()

        self._orderRepository.save(order)
