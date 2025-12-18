from dataclasses import dataclass


@dataclass(frozen=True) #()
class OrderLine:
    orderid: str
    sku: str
    qty: int
    
class Batch:
    def __init__(self, ref: str, sku: str, qty: int, Optional[date]):
        self.reference = ref
        self.sku = sku
        self.eta = eta
        self.available_quantity = qty
        
    def allocaate(self, line: Orderline):
        self.available_quantity -= line.qty
        