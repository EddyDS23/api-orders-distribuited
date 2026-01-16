from sqlalchemy import Column, String, Float, JSON
from sqlalchemy.dialects.postgresql import UUID
import uuid

from app.domain.entities.order import Order
from app.domain.value_objects.order_status import OrderStatus
from app.domain.value_objects.money import Money


from app.infrastructure.persistence.database.connection import Base 

class OrderModel(Base):
    __tablename__ = "orders"

    id = Column(UUID(as_uuid=True),primary_key=True,default=uuid.uuid4)
    status = Column(String, nullable=False)
    total = Column(Float, nullable=False)
    items = Column(JSON, nullable=False, default=list)


    @classmethod
    def from_domain(cls, order:Order) -> "OrderModel":
        return cls(
            id=order.id,
            status = order.status.value,
            total = order.total.amount,
            items = order.items
        )
    

    def to_domain(self) -> Order:
        return Order(
            id=self.id,
            status=OrderStatus(self.status),
            total = Money(self.total),
            items = self.items
        )
