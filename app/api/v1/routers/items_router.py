from fastapi import APIRouter, Depends, status

from uuid import UUID
from sqlalchemy.orm import Session

from app.application.orders.use_cases.add_item_to_order import AddItemToOrderUseCase
from app.application.orders.use_cases.update_item_to_order import UpdateItemFromOrderUseCase
from app.application.orders.use_cases.remove_item_to_order import RemoveItemFromOrderUseCase

from app.application.orders.dto.order_item_dto import OrderItemInputDTO, UpdateItemInputDTO
from app.application.orders.dto.orders_dto import OrderResponseDTO

from app.infrastructure.persistence.repositories.order_repository import OrderRepository
from app.infrastructure.persistence.database.connection import get_db

router = APIRouter(prefix="/{order_id}/items", tags=["Items"])


def get_repository(db:Session = Depends(get_db)) -> OrderRepository:
    return OrderRepository(db)

@router.post("/", response_model=OrderResponseDTO, status_code=status.HTTP_201_CREATED)
def add_item(order_id:UUID, input_dto:OrderItemInputDTO, repository:OrderRepository = Depends(get_repository)) -> OrderResponseDTO:
    use_case = AddItemToOrderUseCase(repository)
    return use_case.execute(order_id,input_dto)


@router.patch("/{item_id}", response_model=OrderResponseDTO, status_code=status.HTTP_200_OK)
def update_item(order_id:UUID, item_id:UUID, input_dto:UpdateItemInputDTO, repository:OrderRepository=Depends(get_repository)) -> OrderResponseDTO:
    use_case = UpdateItemFromOrderUseCase(repository)
    return use_case.execute(order_id, item_id, input_dto)


@router.delete("/{item_id}", response_model=OrderResponseDTO, status_code=status.HTTP_200_OK)
def remove_item(order_id:UUID, item_id:UUID,repository:OrderRepository=Depends(get_repository)) -> OrderResponseDTO:
    use_case = RemoveItemFromOrderUseCase(repository)
    return use_case.execute(order_id, item_id)