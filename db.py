from sqlalchemy import create_engine
from sqlalchemy.orm import DeclarativeBase


engine = create_engine(
    'postgresql://admin:oQpfu6lfN0g6hBtOCjC6gwOBsxekjPRS@dpg-cluf91md3nmc7383oro0-a.frankfurt-postgres.render.com/grabbo'
)

class Base(DeclarativeBase):
    pass