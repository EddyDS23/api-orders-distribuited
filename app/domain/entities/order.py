from uuid import UUID, uuid4
from dataclasses import dataclass, field

from app.domain.exceptions.order_exceptions import (
    EmptyOrderError,InvalidOperationOrderError
)

from app.domain.entities.item import OrderItem

from app.domain.value_objects.order_status import OrderStatus
from app.domain.value_objects.money import Money


@dataclass
class Order:

    id:UUID = field(default_factory=uuid4)
    user_id:UUID = field(default=None)
    status:OrderStatus = OrderStatus.CREATED
    items:list[OrderItem] = field(default_factory=list)


    @property
    def total(self) -> Money:

        if not self.items:
            return Money(0)

        return Money(sum(item.subtotal.amount for item in self.items))



    def add_item(self, product_id:str, unit_price:Money, quantity:int = 1) -> OrderItem:
        if self.status != OrderStatus.CREATED:
            raise InvalidOperationOrderError("" \
            "Cannot modify an order that is not in CREATED status"
            )

        item = OrderItem(
            product_id=product_id,
            quantity=quantity,
            unit_price=unit_price,
            order_id= self.id
        )

        self.items.append(item)
        return item
    

    def remove_item(self,item_id:UUID) -> None:
        '''Remove item by ID'''
        if self.status != OrderStatus.CREATED:
            raise InvalidOperationOrderError("Cannot modify an order that is not in CREATED status")
        
        self.items = [item for item in self.items if item.id != item_id]



    def get_item(self,item_id:UUID) -> OrderItem | None:
        '''Get item by ID'''
        for item in self.items:
            if item.id == item_id:
                return item
        return None
    

    def update_item_quantity(self, item_id:UUID, new_quantity:int) -> None:
        '''Update quantity from order'''
        if self.status != OrderStatus.CREATED:
            raise InvalidOperationOrderError(
                "Cannot modify an order that is not in CREATED status"
            )
        
        item = self.get_item(item_id)
        if not item:
            raise ValueError(f"Item {item_id} not found in order")

        item.update_quantity_in_order(new_quantity)


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

    



