from fastapi import Depends, FastAPI, HTTPException
from fastapi.responses import JSONResponse
# from fastapi.exceptions import HTTPException as HTTPExceptionError
from sqlalchemy.orm import Session

from . import crud, models, schemas
from .database import SessionLocal, engine

app = FastAPI()


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@app.post("/customers/", response_model=schemas.Customer)
def create_customer(customer: schemas.CustomerCreate, db: Session = Depends(get_db)):
    db_customer = crud.get_customer_by_phone_number(db, customer.phone)
    if db_customer:
        raise HTTPException(
            400, 'Customer with same phone number already exists')
    return crud.create_customer(db, customer)


@app.get("/customers/", response_model=list[schemas.Customer])
def read_customers(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    customers = crud.get_customers(db, skip, limit)
    return customers


@app.get("/customers/{customer_number}", response_model=schemas.Customer)
def read_customer(customer_number: int, db: Session = Depends(get_db)):
    print(customer_number)
    customer = crud.get_customer(db, customer_number)
    if customer is None:
        raise HTTPException(404, 'Customer not found')
    return customer
