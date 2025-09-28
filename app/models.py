from sqlalchemy import Integer, String
from sqlalchemy.orm import Mapped, mapped_column
from app.database import Base

class Product(Base):
  __tablename__ = "products"

  id: Mapped[int] = mapped_column(Integer, primary_key=True)
  name: Mapped[str] = mapped_column(String, nullable=False)
  description: Mapped[str] = mapped_column(String, nullable=False)
  stock_quantity: Mapped[int] = mapped_column(Integer, nullable=False)
  low_stock_threshold: Mapped[int] = mapped_column(Integer, nullable=False)

  def __repr__(self):
    return f"<Product(product_id:{self.id}, name:{self.name}, description:{self.description}, stock_quantity:{self.stock_quantity})>"