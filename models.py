from sqlalchemy import Column, Integer, String, Float, ForeignKey,DateTime
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base
from datetime import datetime

# creates a base class for the declarative class definitions
Base = declarative_base()

# product model that maps to the products table
class Product(Base):
    #naming the table in the database
    __tablename__ = "products"

# defining the columns of the products table
    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    price = Column(Float, nullable=False)

# A one-to many relationship with the sales table which references this product
    sales = relationship('Sale', back_populates='product')

# validation of price
    @property
    def valid_price(self):
        if self.price < 0:
            raise ValueError("price cannot be a negative")

 
#  sales model which maps to the sales table
class Sale(Base):
    # name of the table in the database
    __tablename__ = 'sales'

# columns of the sales table
    id = Column(Integer, primary_key=True)
    product_id = Column(Integer, ForeignKey('products.id'), nullable=False)# Foreign key referencing 'products' table
    quantity = Column(Integer, nullable=False)
    total_price = Column(Float, nullable=False)
    date_created = Column(DateTime, default=datetime.pytznow) # automatic setting of the current pytz time when a sale is created

# Many-to-one relationship with the 'products' table
    product = relationship('Product', back_populates='sales')

# quantity validation
    @property
    def valid_quantity(self):
        if self.quantity <= 0:
            raise ValueError('quantity must be more than 0')