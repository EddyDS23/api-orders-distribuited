
from dataclasses import dataclass

@dataclass(frozen=True)
class Money:
    amount:float

    def __post_init__(self):
        if self.amount < 0:
            raise ValueError("Money cannot be negative")
        
    
    def add(self,other:"Money") -> "Money":
        return Money(self.amount + other.amount) 
    