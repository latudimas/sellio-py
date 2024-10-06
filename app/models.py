from sqlalchemy import Column, DateTime, Float, ForeignKey, Integer, String
from sqlalchemy.orm import relationship

from .database import Base


class Product(Base):
    __tablename__ = "products"

    product_id = Column(Integer, primary_key=True)
    name = Column(String(100), nullable=False)
    barcode = Column(String(50), unique=True)
    price = Column(Float, nullable=False)
    description = Column(String(255))
    category_id = Column(Integer, ForeignKey("categories.category_id"))

    category = relationship("Category", back_populates="products")
    inventory = relationship("Inventory", back_populates="product", uselist=False)
    order_items = relationship("OrderItem", back_populates="product")


class Category(Base):
    __tablename__ = "categories"

    cateogory_id = Column(Integer, primary_key=True)
    name = Column(String(50), nullable=False)
    description = Column(String(255))

    products = relationship("Product", back_populates="category")


class Inventory(Base):
    __tablename__ = "inventory"

    inventory_id = Column(Integer, primary_key=True)
    product_id = Column(Integer, ForeignKey("producst.product_id"))
    quantity = Column(Integer)
    last_updated = Column(DateTime)

    product = relationship("Product", back_populates="inventory")


class Order(Base):
    __tablename__ = "orders"

    order_id = Column(Integer, primary_key=True)
    order_date = Column(DateTime)
    total_amount = Column(Float)
    status = Column(String(20))

    order_items = relationship("OrderItem", back_populates="order")
    payment = relationship("Payment", back_populates="order", uselist=False)


class OrderItem(Base):
    __tablename__ = "order_items"

    order_item_id = Column(Integer, primary_key=True)
    order_id = Column(Integer, ForeignKey("orders.order_id"))
    product_id = Column(Integer, ForeignKey("products.product_id"))
    quantity = Column(Integer)
    unit_price = Column(Float)
    sub_total = Column(Float)

    order = relationship("Order", back_populates="order_items")
    product = relationship("Product", back_populates="order_items")


class Payment(Base):
    __tablename__ = "payments"

    id = Column(Integer, primary_key=True)
    order_id = Column(Integer, ForeignKey("orders.order_id"))
    amount = Column(Float)
    payment_method = Column(String(50))
    payment_date = Column(DateTime)

    order = relationship("Order", back_populates="payment")
