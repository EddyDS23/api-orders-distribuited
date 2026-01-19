from app.infrastructure.persistence.repositories.order_repository import OrderRepository

from app.application.orders.dto.order_item_dto import OrderItemInputDTO
from app.application.orders.dto.orders_dto import OrderResponseDTO

from app.domain.value_objects.money import Money
from app.domain.exceptions.order_exceptions import OrderNotFoundException
from app.domain.exceptions.item_exceptions import ItemExistingInOrder

from uuid import UUID

class AddItemToOrderUseCase:
    
    def __init__(self,orderRepository:OrderRepository):
        self._orderRepository = orderRepository

    def execute(self,order_id:UUID,input_dto:OrderItemInputDTO)-> OrderResponseDTO:

        order = self._orderRepository.get_by_id(order_id)

        if not order:
            raise OrderNotFoundException(f"Order {order_id} not found")

        for item in order.items:
            if item.product_id == input_dto.product_id:
               raise ItemExistingInOrder(f"Product {item.id} already exists in order ")
        
        order.add_item(product_id=input_dto.product_id,
                        unit_price=Money(input_dto.unit_price),
                        quantity=input_dto.quantity
                        )
        

        self._orderRepository.save(order)

        return OrderResponseDTO.from_domain(order)
    
        