from sqlalchemy import Column, String, Float, JSON
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import relationship
import uuid

from app.domain.entities.order import Order
from app.domain.value_objects.order_status import OrderStatus
from app.domain.value_objects.money import Money


from app.infrastructure.persistence.database.connection import Base 

class OrderModel(Base):
    __tablename__ = "orders"

    id = Column(UUID(as_uuid=True),primary_key=True,default=uuid.uuid4)
    user_id=Column(UUID(as_uuid=True),nullable=False)
    status = Column(String, nullable=False)
    
    items = relationship("OrderItemModel",
                        cascade="all, delete-orphan", 
                        lazy="joined",
                        back_populates="order"
                        )

    @classmethod
    def from_domain(cls, order:Order) -> "OrderModel":
        return cls(
            id=order.id,
            user_id=order.user_id,
            status = order.status.value,
        )
    

    def to_domain(self) -> Order:

        domain_items = [item.to_domain() for item in self.items]

        return Order(
            id=self.id,
            status=OrderStatus(self.status),
            total = Money(self.total),
            items = domain_items
        )
