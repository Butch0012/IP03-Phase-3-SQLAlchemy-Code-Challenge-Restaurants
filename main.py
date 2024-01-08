from sqlalchemy import create_engine, Column, Integer, String, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, relationship
from sqlalchemy.sql import func
import random

# Create the SQLite database engine
engine = create_engine("sqlite:///db.db")

# Declare a base class for declarative models
Base = declarative_base()