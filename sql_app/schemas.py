from pydantic import BaseModel

class CustomerBase(BaseModel):
    customer_name: str
    contact_last_name: str
    contact_first_name:str
    phone: str
    address_line_1: str
    address_line_2 : str
    city: str
    state: str
    postal_code: str
    country: str

class CustomerCreate(CustomerBase):
    pass

class Customer(CustomerBase):
    customer_number: int
    sales_rep_employee_number: int
    credit_limit: int
    class Config:
        orm_mode = True