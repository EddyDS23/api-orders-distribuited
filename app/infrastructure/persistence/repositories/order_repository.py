from sqlalchemy.orm import Session

from app.infrastructure.persistence.models.order_model import OrderModel
from app.domain.entities.order import Order

from uuid import UUID

class OrderRepository:

    def __init__(self, session:Session):
        self._session = session


        def save(self, order:Order)-> None:
            model = OrderModel.from_domain(order)
            self._session.merge(model)
            self._session.commit()

    
    def get_by_id(self, order_id:UUID) -> Order | None:
        model = self._session.get(OrderModel,order_id)
        return model.to_domain() if model else None
    

    

