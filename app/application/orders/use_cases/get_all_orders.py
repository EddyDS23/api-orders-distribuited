
from app.application.orders.dto.orders_dto import OrderResponseDTO
from app.application.orders.dto.paginated_orders_dto import PaginatedOrdersOResponseDTO

from app.infrastructure.persistence.repositories.order_repository import OrderRepository

class GetAllOrderUseCase:

    def __init__(self, orderRepository:OrderRepository):
        self._orderRepository = orderRepository

    
    def execute(self,page:int=1,size:int=10) -> PaginatedOrdersOResponseDTO:
        
        if page < 1:
            raise ValueError("Page must be >= 1")
        if size < 1 or size > 100:
            raise ValueError("Size must be between 1 and 100")

        offset = (page - 1) * size

        orders = self._orderRepository.get_all(limit=size,offset=offset)
        total = self._orderRepository.count()

        return PaginatedOrdersOResponseDTO(
            orders=[OrderResponseDTO.from_domain(order) for order in orders],
            page=page,
            size=size,
            total=total
        )
