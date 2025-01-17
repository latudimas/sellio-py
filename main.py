import logging
from typing import List, Dict, Optional
from datetime import datetime
from fasthtml import common as fh

from config import config

app, rt = fh.fast_app()
db = fh.database(config.database_url)
logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)
logger = logging.getLogger(__name__)

if len(db.t) == 0:
    logger.info("DB is empty, create")
    product = db.t.product.create(
        id=str, barcode=str, name=str, price=float, stock=int, pk="id"
    )
    # order_item = db.t.order_item.creat(id=str, product)


class Product:
    def __init__(self, id: str, barcode: str, name: str, price: float, stock: int):
        self.id: str = id
        self.barcode: str = barcode
        self.name: str = name
        self.price: float = price
        self.stock: int = stock


class OrderItem:
    def __init__(self, id: str, product: Product, quantity: int):
        self.id: str = id
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
    def __init__(self, id: str, amount: float, method: str):
        self.id: str = id
        self.amount: float = amount
        self.method: str = method
        self.timestamp: datetime = datetime.now()


@rt("/")
def getIndex():
    return fh.Div(fh.P("Hello World"), hx_get="/change")


@rt("/change")
def getChange():
    return fh.P("Nice to be here!")


if __name__ == "__main__":
    fh.serve()
