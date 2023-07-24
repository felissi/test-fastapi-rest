try:
    from .database import Base
except ImportError:
    from database import Base
from sqlalchemy import DECIMAL, Boolean, Column, ForeignKey, Integer,  String
from sqlalchemy.orm import relationship

class Customer(Base):
    __tablename__             = 'customers'
    customer_number           = Column('customerNumber'        , Integer      , primary_key= True, autoincrement = True,unique = True,nullable = False)
    customer_name             = Column('customerName'          , String(50)   , nullable   = True)
    contact_last_name         = Column('contactLastName'       , String(50)   , nullable   = True)
    contact_first_name        = Column('contactFirstName'      , String(50)   , nullable   = True)
    phone                     = Column('phone'                 , String(50)   , nullable   = True, unique = True)
    address_line_1            = Column('addressLine1'          , String(50)   , nullable   = True)
    address_line_2            = Column('addressLine2'          , String(50)   , nullable   = True)
    city                      = Column('city'                  , String(50)   , nullable   = True)
    state                     = Column('state'                 , String(50)   , nullable   = True)
    postal_code               = Column('postalCode'            , String(50)   , nullable   = True)
    country                   = Column('country'               , String(50)   , nullable   = True)
    sales_rep_employee_number = Column('salesRepEmployeeNumber', Integer      , nullable   = True)
    credit_limit              = Column('creditLimit'           , DECIMAL(2,10), nullable   = True)

class Test(Base):
    __tablename__ = 'test'
    snake_name = Column('snake_name', Integer, primary_key=True)