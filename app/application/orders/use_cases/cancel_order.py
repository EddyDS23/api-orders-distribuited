
from app.infrastructure.persistence.repositories.order_repository import OrderRepository
from app.domain.exceptions.order_exceptions import OrderNotFoundException
from app.application.orders.dto.orders_dto import OrderResponseDTO

from uuid import UUID

class CancelOrderUseCase:

    def __init__(self,orderRepository:OrderRepository):
        self._orderRepository = orderRepository

    
    def execute(self,order_id:UUID) -> OrderResponseDTO | None:
        
        order = self._orderRepository.get_by_id(order_id)

        if not order:
            raise OrderNotFoundException(f"Order {order_id} not found")
        
        order.cancel()    

        self._orderRepository.save(order)

        return OrderResponseDTO.from_domain(order)
