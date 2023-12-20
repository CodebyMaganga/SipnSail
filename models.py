from sqlalchemy import Column, Integer, String, VARCHAR, Table, Boolean, TIMESTAMP, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship

Base = declarative_base()

product_cart_association = Table(
    'product_cart_association',
    Base.metadata,
    Column('product_id',Integer, ForeignKey('products.id')),
    Column('cart_item_id',Integer, ForeignKey('cart_items.id'))

)

product_order_association = Table(
    'product_order_association',
    Base.metadata,
    Column('product_id', Integer, ForeignKey('products.id')),
    Column('order_id', Integer, ForeignKey('orderitems.id') )
)

order_detail_item_association = Table(
    'order_detail_item_association',
    Base.metadata,
    Column('order_details', Integer, ForeignKey('order_details.id')),
    Column('order_id', Integer, ForeignKey('orderitems.id'))
)

class Product(Base):
    __tablename__ = 'products'

    id = Column(Integer(), primary_key=True)
    name = Column(String(), nullable=False, unique=True)
    url = Column(VARCHAR(), nullable=False)
    price = Column(String(), nullable=False)
    on_offer = Column(Boolean(), default=False)
    category = Column(String()) 


    def __repr__(self):
        return f"{self.name} is in Database"

class Cart_item(Base):
    __tablename__ = "cart_items"

    id = Column(Integer(), primary_key=True)
    session_id = Column(Integer(), ForeignKey('sessions.id'))
    product_id = Column(Integer(), ForeignKey('products.id'))
    quantity = Column(Integer())
    created_at = Column(TIMESTAMP)
    modified_at = Column(TIMESTAMP)

    products = relationship('Product', secondary=product_cart_association,
                           backref='cart_items')
    
    session = relationship('Session', backref='cart_items') 

    def __repr__(self):
        return f"{self.id} is in Database"

class Session(Base):
    __tablename__ = 'sessions'

    id = Column(Integer(), primary_key=True)
    user_id = Column(Integer(), ForeignKey('users.id'))
    total = Column(Integer())
    created_at = Column(TIMESTAMP)
    modified_at = Column(TIMESTAMP)

    user = relationship('User', backref='sessions')

    def __repr__(self):
        return f"{self.id} is active"
    

class PaymentDetail(Base):
    __tablename__ = "paymentdetails"

    id = Column(Integer(), primary_key=True)
    order_id = Column(VARCHAR)
    amount = Column(Integer())
    provider = Column(VARCHAR)
    status = Column(VARCHAR)
    created_at = Column(TIMESTAMP)

    def __repr__(self):
        return f"{self.id} is in Database"
    
class OrderDetail(Base):
    __tablename__ = "orderdetails"

    id = Column(Integer(), primary_key=True)
    user_id = Column(Integer(), ForeignKey('users.id'))
    total = Column(Integer())
    payment_id = Column(Integer(), ForeignKey('paymentdetails.id'))
    created_at = Column(TIMESTAMP)
    modified_at = Column(TIMESTAMP)

    user = relationship('User', backref='orderdetails')
    payment = relationship('PaymentDetails', backref='orderdetails')

    def __repr__(self):
        return f"{self.id} is in Database"


class OrderItem(Base):
    __tablename__ = 'orderitems'

    id = Column(Integer(), primary_key=True)
    order_id = Column(Integer(), ForeignKey('orderdetails.id'))
    product_id = Column(Integer(), ForeignKey('products.id'))
    quantity = Column(Integer())
    created_at = Column(TIMESTAMP)
    modified_at = Column(TIMESTAMP)

    product = relationship('Product',
                           secondary=product_order_association,
                           backref='orderitems'
                           )
    
    orderdetail = relationship('OrderDetail', secondary=order_detail_item_association ,backref='orderitems')

    def __repr__(self):
        return f"{self.id} is in Database"
    
class User(Base):
    __tablename__ = 'users'

    id = Column(Integer(), primary_key=True)
    first_name = Column(String(), nullable=False)
    last_name = Column(String(), nullable=False)
    email = Column(VARCHAR, nullable=False)
    address = Column(VARCHAR)
    phone_number = Column(Integer())
    created_at = Column(TIMESTAMP)

    def __repr__(self):
        return f"{self.first_name}  {self.last_name} is in Database"













    
    
    


