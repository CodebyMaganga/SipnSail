from sqlalchemy import Column, Integer, String, VARCHAR, Boolean
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class Product(Base):
    __tablename__ = 'products'

    id = Column(Integer(), primary_key=True)
    name = Column(String(), nullable=False, unique=True)
    url = Column(VARCHAR(), nullable=False)
    price = Column(String(), nullable=False)
    on_offer = Column(Boolean(), default=False)


    def __repr__(self):
        return f"{self.name} is in Database"
    


