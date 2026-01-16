
from app.domain.entities.order import Order
from app.domain.value_objects.money import Money

from random import randrange

from app.application.orders.dto.orders_dto import (OrderCreateInputDTO, OrderResponseDTO)

from app.infrastructure.persistence.repositories.order_repository import OrderRepository

class CreateOrderUseCase:

    def __init__(self,orderRepository: OrderRepository):
        self._orderRepository = orderRepository


    def execute(self,input_dto:OrderCreateInputDTO) -> OrderResponseDTO:

        order = Order(user_id=input_dto.user_id)

        for item in input_dto.items:
            order.add_item(item, Money(randrange(10,100,5)))


        self._orderRepository.save(order)

        return OrderResponseDTO.model_validate(order)
    


    