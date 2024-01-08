from sqlalchemy import create_engine, Column, Integer, String, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, relationship
from sqlalchemy.sql import func
import random

# Create the SQLite database engine
engine = create_engine("sqlite:///db.db")

# Declare a base class for declarative models
Base = declarative_base()

# Define the Restaurant class
class Restaurant(Base):
    __tablename__ = "restaurants"

    id = Column(Integer, primary_key=True)
    name = Column(String)
    price = Column(Integer)
    reviews = relationship("Review", back_populates="restaurant")

    def __init__(self, name, price):
        self.name = name
        self.price = price
    def __repr__(self):
        return f"Restaurant: {self.name}, {self.price} dollars"
# Define the Customer class
class Customer(Base):
    __tablename__ = "customers"

    id = Column(Integer, primary_key=True)
    name = Column(String)
    reviews = relationship("Review", back_populates="customer")
    
    def __init__(self, name):
        self.name = name

    def __repr__(self):
        return f"Customer: {self.name}"
