from fastapi import APIRouter, Depends, HTTPException

from ..database import get_db

router = APIRouter(
    prefix="/product",
    tags=["product"],
    dependencies=[Depends(get_db)],
)


@router.get("/")
async def get_products():
    return
