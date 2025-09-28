from pydantic import BaseModel, ConfigDict

class ProductBase(BaseModel):
  name: str
  description: str
  stock_quantity: int
  low_stock_threshold: int

class ProductUpdate(BaseModel):
  name: str | None = None
  description: str | None = None
  stock_quantity: int | None = None
  low_stock_threshold: int | None = None

class StockChange(BaseModel):
  change: int

class ResponseBase(BaseModel):
  id: int
  name: str
  description: str
  stock_quantity: int
  low_stock_threshold: int

  model_config = ConfigDict(from_attributes=True)