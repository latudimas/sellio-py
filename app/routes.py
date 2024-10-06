from fastapi import APIRouter
from pydantic import BaseModel

router = APIRouter()


class Product(BaseModel):
    id: str
    barcode: str
    name: str
    price: str
    stock: int


def create_routes():
    @router.post("/product")
    def create_product()
