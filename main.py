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

# Define the Review class
class Review(Base):
    __tablename__ = "reviews"

    id = Column(Integer, primary_key=True)
    star_rating = Column(Integer)
    restaurant_id = Column(Integer, ForeignKey("restaurants.id"))
    customer_id = Column(Integer, ForeignKey("customers.id"))
    restaurant = relationship("Restaurant", back_populates="reviews")
    customer = relationship("Customer", back_populates="reviews")

    def __init__(self, star_rating, restaurant, customer):
        self.star_rating = star_rating
        self.restaurant = restaurant
        self.customer = customer

    def review_customer(self):
        # Get the Customer instance for this review
        return Customer.query.get(self.customer_id)

    def review_restaurant(self):
        # Get the Restaurant instance for this review
        return Restaurant.query.get(self.restaurant_id)

if __name__ == "__main__":
    # Create all tables in the engine
    Base.metadata.create_all(engine)

    # Create a session to interact with the database
    with sessionmaker(bind=engine)() as session:
        # Add restaurants if not present
        if not session.query(Restaurant).count():
            restaurants_data = [
                {"name": 'Shicken Wangs Place', "price": 15},
                {"name": 'Rib Shack', "price": 18},
                {"name": 'ExtraOrdinary Ugali', "price": 35},
                {"name": 'Poly Nyama Choma', "price": 12}
            ]