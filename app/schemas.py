from pydantic import BaseModel, ConfigDict

class ProductBase(BaseModel):
  name: str
  description: str
  stock_quantity: int
  low_stock_threshold: int

class StockChange(BaseModel):
  change: int

class ResponseBase(BaseModel):
  id: int
  name: str
  description: str
  stock_quantity: int
  low_stock_threshold: int

  model_config = ConfigDict(from_attributes=True)