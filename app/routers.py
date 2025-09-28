from fastapi import APIRouter, status, HTTPException, Depends, Response
from sqlalchemy.orm import Session
from app.database import get_db
from app import schemas, models
from typing import List

router = APIRouter(
  prefix="/products",
  tags=["Routers"]
)

# Create a new Product
@router.post("/", response_model=schemas.ResponseBase)
def create_product(product: schemas.ProductBase, db:Session = Depends(get_db)):
  new_product = models.Product(**product.model_dump())
  db.add(new_product)
  db.commit()
  db.refresh(new_product)
  return new_product

# Get products with stock below requirement
@router.get("/below_requirement", response_model = List[schemas.ResponseBase])
def products_below_requirement(db:Session = Depends(get_db)):
  db_q = db.query(models.Product).filter(models.Product.stock_quantity <= models.Product.low_stock_threshold).all()
  return db_q

# Get all Products
@router.get("/", response_model=List[schemas.ResponseBase])
def get_all_products(db:Session = Depends(get_db)):
  products = db.query(models.Product).all()
  return products

# Get A Single Product by ID
@router.get("/{id}", response_model=schemas.ResponseBase)
def get_product_by_id(id: int, db:Session = Depends(get_db)):
  product = db.get(models.Product, id)
  if not product:
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Product ID Doesn't Exist!")
  return product

# Delete a Product
@router.delete("/{id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_product(id: int, db:Session = Depends(get_db)):
  product = db.get(models.Product, id)
  if not product:
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Product ID Doesn't Exist!")
  db.delete(product)
  db.commit()
  return Response(status_code=status.HTTP_204_NO_CONTENT)

# Update a Product (replace fields)
@router.patch("/{id}", response_model=schemas.ResponseBase)
def update_product(id: int, product: schemas.ProductUpdate, db:Session = Depends(get_db)):
  pd_q = db.get(models.Product, id)
  if not pd_q:
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Product ID Doesn't Exist!")
  product_update = product.model_dump(exclude_unset=True)
  for k, v in product_update.items():
    setattr(pd_q, k, v)
  db.commit()
  db.refresh(pd_q)
  return pd_q

# Increment stock
@router.patch("/increment/{id}", response_model=schemas.ResponseBase)
def increment_stocks(id: int, payload: schemas.StockChange, db:Session = Depends(get_db)):
  if payload.change <=0:
    raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Enter Valid (Positive) Values!")
  with db.begin():
    product = db.get(models.Product, id, with_for_update=True)
    if not product:
      raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Product ID Doesn't Exist!")
    product.stock_quantity += payload.change
    return product
  
# Decrement stock
@router.patch("/decrement/{id}", response_model=schemas.ResponseBase)
def decrement_stocks(id: int, payload: schemas.StockChange, db:Session = Depends(get_db)):
  if payload.change <=0:
    raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Enter Valid (Positive) Values!")
  with db.begin():
    product = db.get(models.Product, id, with_for_update=True)
    if not product:
      raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Product ID Doesn't Exist!")
    if payload.change>product.stock_quantity:
      raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST,  detail="Insufficient Stock!")
    product.stock_quantity -= payload.change
    return product