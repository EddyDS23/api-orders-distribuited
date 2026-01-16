from uuid import UUID, uuid4
from dataclasses import dataclass, field

from app.domain.exceptions.order_exceptions import (
    EmptyOrderError,InvalidOperationOrderError
)

from app.domain.value_objects.order_status import OrderStatus
from app.domain.value_objects.money import Money


@dataclass
class Order:

    id:UUID = field(default_factory=uuid4)
    status:OrderStatus = OrderStatus.CREATED
    total:Money = field(default_factory=lambda:Money(0))
    items:list[str] = field(default_factory=list)


    def add_item(self, item:str, price:Money) -> None:
        if self.status != OrderStatus.CREATED:
            raise InvalidOperationOrderError("" \
            "Cannot modify an order that is not in CREATED status"
            )

        self.items.append(item)
        self.total = self.total.add(price)


    def confirm(self) -> None:
        if not self.items:
            raise EmptyOrderError("Cannot confirm an empty order")
        

        if self.status != OrderStatus.CREATED:
            raise InvalidOperationOrderError("Only orders in CREATED status can be confirmed")


        self.status = OrderStatus.CONFIRMED

    
    def cancel(self) -> None:
        if self.status == OrderStatus.CONFIRMED:
            raise InvalidOperationOrderError("Cannot cancel a confirmed status")
        
        self.status = OrderStatus.CANCELED

    



