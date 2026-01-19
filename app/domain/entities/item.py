

from uuid import UUID, uuid4
from dataclasses import dataclass, field

from app.domain.value_objects.money import Money

@dataclass
class OrderItem:
    
    product_id:str 
    quantity:int
    unit_price:Money
    id:UUID = field(default_factory=uuid4)
    order_id:UUID = field(default=None)

    def __post_init__(self):
        if self.quantity<=0:
            raise ValueError("Quantity must be greater than 0")
        if self.unit_price.amount < 0:
            raise ValueError("Price cannot be negative")

    @property
    def subtotal(self) -> Money:
        '''Calculate subtotal a item'''
        return Money(self.unit_price.amount * self.quantity)

    def update_quantity_in_order(self, new_quantity:int) -> None:
        '''Update the quantity(Now is mutable)'''
        if new_quantity <= 0:
            raise ValueError("Quantity must be greater than 0")
        self.quantity = new_quantity 


    def update_unit_price(self,new_price:Money) -> None:
        if new_price <= 0:
            raise ValueError("New price cannot negative or zero") 
        self.unit_price = new_price  
    

