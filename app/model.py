from typing import List, Dict, Optional
from datetime import datetime


class Product:
    def __init__(self, id: str, barcode: str, name: str, price: float, stock: int):
        self.id: str = id
        self.barcode: str = barcode
        self.name: str = name
        self.price: float = price
        self.stock: int = stock


class OrderItem:
    def __init__(self, product: Product, quantity: int):
        self.product: Product = product
        self.quantity: int = quantity

    def get_subtotal(self) -> float:
        return self.product.price * self.quantity


class Order:
    def __init__(self, id: str):
        self.id: str = id
        self.items: List[OrderItem] = []
        self.timestamp: datetime = datetime.now()
        self.total: float = 0.0

    def add_time(self, item: OrderItem) -> None:
        self.items.append(item)
        self.total += item.get_subtotal()

    def remove_item(self, item: OrderItem) -> None:
        if item in self.items:
            self.items.remove(item)
            self.total -= item.get_subtotal()


class Payment:
    def __init__(self, amount: float, method: str):
        self.amount: float = amount
        self.method: str = method
        self.timestamp: datetime = datetime.now()
