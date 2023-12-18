from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base


engine = create_engine(
    'postgresql://admin:w2hM8G0hNZjSlYRyokDTfG7WpavszfEH@dpg-cm05b9ug1b2c73cn6arg-a.frankfurt-postgres.render.com/sipnsail',
    echo=True
)

Base = declarative_base()

local_session = sessionmaker(bind=engine)