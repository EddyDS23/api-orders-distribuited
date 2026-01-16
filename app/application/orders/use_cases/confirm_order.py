from app.application.orders.dto.orders_dto import (OrderResponseDTO)

from app.domain.exceptions.order_exceptions import (EmptyOrderError, InvalidOperationOrderError)

from app.infrastructure.persistence.repositories.order_repository import OrderRepository

from uuid import UUID


class ConfirmOrderUseCase:
    
    def __init__(self,orderRepository:OrderRepository):
        self._orderRepository = orderRepository

    
    def execute(self,order_id:UUID) -> OrderResponseDTO:

        order = self._orderRepository.get_by_id(order_id)

        if not order:
            raise ValueError(f"Order {order_id} not found")
        

        try:
            order.confirm()
        except EmptyOrderError as e:
            raise e
        except InvalidOperationOrderError as e:
            raise e
        

        self._orderRepository.save(order)

        return OrderResponseDTO.model_validate(order)


