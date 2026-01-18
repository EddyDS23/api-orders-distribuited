from sqlalchemy import Column, String, Integer, Float, ForeignKey
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import relationship
import uuid

from app.infrastructure.persistence.database.connection import Base
from app.domain.entities.item import OrderItem
from app.domain.value_objects.money import Money

class OrderItemModel(Base):
    __tablename__="order_items"

    id = Column(UUID(as_uuid=True),primary_key=True, default=uuid.uuid4)
    order_id = Column(UUID(as_uuid=True),ForeignKey("orders.id"), nullable=False)
    product_id = Column(String, nullable=False)
    quantity = Column(Integer, nullable=False)
    unit_price = Column(Float, nullable=False)

    order = relationship("OrderModel", back_populates="items")

    @classmethod
    def from_domain(cls, order_item:OrderItem) -> "OrderItemModel":
        return cls(
            id=order_item.id,
            order_id=order_item.order_id,
            product_id=order_item.product_id,
            quantity=order_item.quantity,
            unit_price=order_item.unit_price.amount
        )
    
    def to_domain(self) -> OrderItem:
        return OrderItem(
            id=self.id,
            order_id=self.order_id,
            product_id=self.product_id,
            quantity=self.quantity,
            unit_price=Money(self.unit_price)
        )