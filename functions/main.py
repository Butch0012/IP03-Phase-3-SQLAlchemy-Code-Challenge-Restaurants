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
            # Sample restaurant data
            restaurants_data = [
                {"name": 'Shicken Wangs Place', "price": 15},
                {"name": 'Rib Shack', "price": 18},
                {"name": 'ExtraOrdinary Ugali', "price": 35},
                {"name": 'Poly Nyama Choma', "price": 12}
            ]
            # Loop through the restaurant data and add to the session
            for restaurant_data in restaurants_data:
                session.add(Restaurant(**restaurant_data))

        # Add customers if not present
        if not session.query(Customer).count():
            # Sample customer data
            customers_data = [
                {"name": 'John Mbaru'},
                {"name": 'Wangachi'},
                {"name": 'Mwangi Ace'},
                {"name": 'Sankofa King'},
                {"name": 'Sean Carter'},
                {"name": 'Kendrick Lamar'}
            ]
            # Loop through the customer data and add to the session
            for customer_data in customers_data:
                session.add(Customer(**customer_data))

        # Commit changes to the database
        session.commit()

        # Choose random restaurant and customer
        restaurant = session.query(Restaurant).order_by(func.random()).first()
        customer = session.query(Customer).order_by(func.random()).first()

        # Generate random star rating
        star_rating = random.randint(1, 5)

        try:
            # Create a new review
            review = Review(
                star_rating=star_rating,
                restaurant=restaurant,
                customer=customer
            )

            # Add the review to the session
            session.add(review)
            session.commit()

        except Exception as e:
            print(f"Error generating review: {e}")
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
            # Sample restaurant data
            restaurants_data = [
                {"name": 'Shicken Wangs Place', "price": 15},
                {"name": 'Rib Shack', "price": 18},
                {"name": 'ExtraOrdinary Ugali', "price": 35},
                {"name": 'Poly Nyama Choma', "price": 12}
            ]
            # Loop through the restaurant data and add to the session
            for restaurant_data in restaurants_data:
                session.add(Restaurant(**restaurant_data))

        # Add customers if not present
        if not session.query(Customer).count():
            # Sample customer data
            customers_data = [
                {"name": 'John Mbaru'},
                {"name": 'Wangachi'},
                {"name": 'Mwangi Ace'},
                {"name": 'Sankofa King'},
                {"name": 'Sean Carter'},
                {"name": 'Kendrick Lamar'}
            ]
            # Loop through the customer data and add to the session
            for customer_data in customers_data:
                session.add(Customer(**customer_data))

        # Commit changes to the database
        session.commit()

        # Choose random restaurant and customer
        restaurant = session.query(Restaurant).order_by(func.random()).first()
        customer = session.query(Customer).order_by(func.random()).first()

        # Generate random star rating
        star_rating = random.randint(1, 5)

        try:
            # Create a new review
            review = Review(
                star_rating=star_rating,
                restaurant=restaurant,
                customer=customer
            )

            # Add the review to the session
            session.add(review)
            session.commit()

        except Exception as e:
            print(f"Error generating review: {e}")

        # Print the updated data
        restaurants = session.query(Restaurant).all()
        print("Restaurants:", restaurants)

        customers = session.query(Customer).all()
        print("Customers:", customers)


        