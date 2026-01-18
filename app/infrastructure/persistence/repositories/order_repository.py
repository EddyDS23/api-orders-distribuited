from sqlalchemy import select
from sqlalchemy.orm import Session

from app.infrastructure.persistence.models.order_model import OrderModel
from app.domain.entities.order import Order
from app.domain.entities.item import OrderItem
from app.infrastructure.persistence.models.item_model import OrderItemModel

from uuid import UUID

class OrderRepository:

    def __init__(self, session:Session):
        self._session = session


    def save(self, order:Order)-> None:
        
        model = OrderModel.from_domain(order)
        self._session.merge(model)

        self._session.query(OrderItemModel).filter(OrderItemModel.order_id == order.id).delete()    

        for item in order.items:
            item_model = OrderItemModel.from_domain(item)
            self._session.add(item_model)


        self._session.commit()

    
    def get_by_id(self, order_id:UUID) -> Order | None:
        
        model = self._session.get(OrderModel,order_id)

        if not model:
            return None

        return model.to_domain()
    

    def get_all(self,limit:int,offset:int) -> list[Order]:
        
        models = self._session.query(OrderModel).limit(limit).offset(offset)

        return [OrderModel.to_domain(order) for order in models]


    def count(self) -> int:
        return self._session.query(OrderModel).count()



        
    

    

