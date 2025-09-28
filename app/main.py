from fastapi import FastAPI
from app.database import engine
from app import models, routers

app = FastAPI()

# Auto Creates Tables (if Not Already Present)
models.Base.metadata.create_all(bind=engine)

# Routes/Endpoints from different Files
app.include_router(routers.router)

# Root Endpoint
@app.get("/")
def root():
  return {"Detail": "FastAPI works!"}