
from fastapi import APIRouter, Depends, status
from sqlalchemy.orm import Session
from app.application.orders.dto.orders_dto import  OrderCreateInputDTO, OrderResponseDTO
from app.application.orders.use_cases.confirm_order import ConfirmOrderUseCase
from app.application.orders.use_cases.create_order import CreateOrderUseCase
from app.infrastructure.persistence.repositories.order_repository import OrderRepository
from app.infrastructure.persistence.database.connection import get_db

router = APIRouter(prefix="/orders",tags=["Orders"])


def get_repository(db:Session = Depends(get_db)) -> OrderRepository:
    return OrderRepository(db)

@router.post("/",response_model=OrderResponseDTO, status_code=status.HTTP_201_CREATED)
def create(repository:OrderRepository=Depends(get_repository)) -> OrderResponseDTO:
    use_case = CreateOrderUseCase(repository)
    return use_case.execute()
    

@router.patch("/{order_id}/confirm", response_model=OrderResponseDTO, status_code=status.HTTP_200_OK)
def confirmed(order_id:str,repository:OrderRepository=Depends(get_repository)) -> OrderResponseDTO:
    use_case = ConfirmOrderUseCase(repository)
    return use_case.execute(order_id)