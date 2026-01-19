
from uuid import UUID

from app.application.orders.dto.order_item_dto import UpdateItemInputDTO
from app.application.orders.dto.orders_dto import OrderResponseDTO

from app.domain.exceptions.item_exceptions import ItemNotExistingInOrder
from app.domain.exceptions.order_exceptions import OrderNotFoundException

from app.infrastructure.persistence.repositories.order_repository import OrderRepository

class UpdateItemToOrder:

    def __init__(self, orderRepository:OrderRepository):
        self._orderRepository = orderRepository


    def execute(self, order_id:UUID, item_id:UUID, input_dto:UpdateItemInputDTO) -> OrderResponseDTO:

        order = self._orderRepository.get_by_id(order_id)   

        if not order:
            raise OrderNotFoundException(f"Order {order_id} not found")
    
        
        order.update_item_quantity(item_id, input_dto.quantity)

        self._orderRepository.save(order)

        return OrderResponseDTO.from_domain(order)
    

    
        

