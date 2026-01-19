from uuid import UUID

from app.domain.exceptions.order_exceptions import OrderNotFoundException

from app.application.orders.dto.orders_dto import OrderResponseDTO

from app.infrastructure.persistence.repositories.order_repository import OrderRepository

class RemoveItemFromOrderUseCase:

    def __init__(self,orderRepository:OrderRepository):
        self._orderRepository = orderRepository

    
    def execute(self,order_id:UUID, item_id:UUID) -> OrderResponseDTO:

        order = self._orderRepository.get_by_id(order_id)

        if not order:
            raise OrderNotFoundException(f"Order {order_id} not found")
        
        order.remove_item(item_id)

        self._orderRepository.save(order)

        return OrderResponseDTO.from_domain(order)
    




