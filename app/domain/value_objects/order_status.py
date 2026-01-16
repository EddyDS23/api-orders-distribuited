from enum import Enum

class OrderStatus(str,Enum):
    CREATED="CREATED"
    CONFIRMED = "CONFIRMED"
    CANCELED = "CANCELED"
    