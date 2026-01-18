
from fastapi import APIRouter, Depends, status
from uuid import UUID
from sqlalchemy.orm import Session
from app.application.orders.dto.orders_dto import  OrderCreateInputDTO, OrderResponseDTO
from app.application.orders.dto.paginated_orders_dto import PaginatedOrdersOResponseDTO
from app.application.orders.use_cases.confirm_order import ConfirmOrderUseCase
from app.application.orders.use_cases.create_order import CreateOrderUseCase
from app.application.orders.use_cases.get_by_id_order import GetByIdUseCase
from app.application.orders.use_cases.get_all_orders import GetAllOrderUseCase
from app.application.orders.use_cases.cancel_order import CancelOrderUseCase
from app.infrastructure.persistence.repositories.order_repository import OrderRepository
from app.infrastructure.persistence.database.connection import get_db

router = APIRouter(prefix="/orders",tags=["Orders"])


def get_repository(db:Session = Depends(get_db)) -> OrderRepository:
    return OrderRepository(db)


@router.get("/{order_id}",response_model=OrderResponseDTO, status_code=status.HTTP_200_OK)
def get_by_id(order_id:UUID, repository:OrderRepository=Depends(get_repository)) -> OrderResponseDTO:
    use_case = GetByIdUseCase(repository)
    return use_case.execute(order_id)


@router.get("/",response_model=PaginatedOrdersOResponseDTO, status_code=status.HTTP_200_OK)
def get_all(page:int=1, size:int=10,repository:OrderRepository = Depends(get_repository)) -> PaginatedOrdersOResponseDTO:
    use_case = GetAllOrderUseCase(repository)
    return use_case.execute(page,size)


@router.post("/",response_model=OrderResponseDTO, status_code=status.HTTP_201_CREATED)
def create(input_dto:OrderCreateInputDTO,repository:OrderRepository=Depends(get_repository)) -> OrderResponseDTO:
    use_case = CreateOrderUseCase(repository)
    return use_case.execute(input_dto)
    

@router.patch("/{order_id}/confirm", response_model=OrderResponseDTO, status_code=status.HTTP_200_OK)
def confirmed(order_id:UUID,repository:OrderRepository=Depends(get_repository)) -> OrderResponseDTO:
    use_case = ConfirmOrderUseCase(repository)
    return use_case.execute(order_id)


@router.patch("/{order_id}/cancel",response_model=OrderResponseDTO,status_code=status.HTTP_200_OK)
def cancel(order_id:UUID, repository:OrderRepository = Depends(get_repository)) -> OrderResponseDTO:
    use_case = CancelOrderUseCase(repository)
    return use_case.execute(order_id)