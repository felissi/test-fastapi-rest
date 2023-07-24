from sqlalchemy.orm import Session
try:
    from . import models, schemas
except ImportError:
    import models, schemas

def get_customer(db: Session, customer_number: int):
    return db.query(models.Customer).filter(models.Customer.customer_number==customer_number).first()

def get_customer_by_phone_number(db: Session, phone_number: str):
    return db.query(models.Customer).filter(models.Customer.phone==phone_number).first()

def get_customers(db: Session, skip=0, limit=100):
    return db.query(models.Customer).offset(skip).limit(limit).all()

def create_customer(db: Session, customer: schemas.CustomerCreate):
    db_customer = models.Customer(**customer.dict())
    db.add(db_customer)
    db.commit()
    db.refresh(db_customer)
    return db_customer

if __name__ == '__main__':
    from database import SessionLocal
    db = SessionLocal()
    print(get_customer(db, 127))