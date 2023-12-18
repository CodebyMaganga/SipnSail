from db import Base
from sqlalchemy import Column, Integer, String, VARCHAR, DateTime

class Product(Base):
    __tablename__ = 'products'

    id = Column(Integer(), primary_key=True)
    name = Column(String())
    url = Column(VARCHAR())
    price = Column(String())
    created_at = Column(DateTime())

    def __repr__(self):
        return f"{self.name} created at {self.created_at}"
    


