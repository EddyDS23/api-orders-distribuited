
from app.application.orders.dto.orders_dto import OrderResponseDTO

from app.infrastructure.persistence.repositories.order_repository import OrderRepository

class GetAllOrderUseCase:

    def __init__(self, orderRepository:OrderRepository):
        self._orderRepository = orderRepository

    
    def execute(self,page:int=1,size:int=10) -> list[OrderResponseDTO]:
        
        offset = (page - 1) * size

        orders = self._orderRepository.get_all(limit=size,offset=offset)

        return [OrderResponseDTO.from_domain(order) for order in orders]
