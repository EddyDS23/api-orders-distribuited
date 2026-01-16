import pytest
from app.domain.entities.order import Order
from app.domain.value_objects.money import Money
from app.domain.exceptions.order_exceptions import (EmptyOrderError,InvalidOperationOrderError)



def test_order_add_item():
    order = Order()
    order.add_item("Item 1", Money(100))
    assert order.total.amount == 100
    assert len(order.items) == 1

def test_order_confirm_empty_raises():
    order = Order()
    with pytest.raises(EmptyOrderError):
        order.confirm()

def test_order_cancel_confirm_raises():
    order = Order()
    order.add_item("Item 1", Money(100))
    order.confirm()
    with pytest.raises(InvalidOperationOrderError):
        order.cancel()




