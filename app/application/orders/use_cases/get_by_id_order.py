

from app.application.orders.dto.orders_dto import OrderResponseDTO

from app.infrastructure.persistence.repositories.order_repository import OrderRepository

from uuid import UUID

class GetByIdUseCase:

    def __init__(self, orderRepository:OrderRepository):
        self._orderRepository = orderRepository

    def execute(self,order_id:UUID) -> OrderResponseDTO | None:

        order = self._orderRepository.get_by_id(order_id)

        return OrderResponseDTO.from_domain(order) if order else None