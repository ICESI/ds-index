from app.default_settings import DATABASE

from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine

# Establish a connection with the database
engine = create_engine(DATABASE)
Session = sessionmaker(bind=engine)
session = Session()
