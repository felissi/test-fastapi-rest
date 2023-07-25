from pydantic import BaseModel
from typing import Optional

class CustomerBase(BaseModel):
    customer_name: str
    contact_last_name: str
    contact_first_name:str
    phone: str
    address_line_1: str
    address_line_2: Optional[str]
    city: str
    state: Optional[str]
    postal_code: Optional[str]
    country: str

class CustomerCreate(CustomerBase):
    pass

class Customer(CustomerBase):
    customer_number: int
    sales_rep_employee_number: Optional[int]
    credit_limit: Optional[int]
    class Config:
        orm_mode = True