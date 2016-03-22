from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, DateTime
import datetime

Base = declarative_base()

class Device(Base):
	__tablename__ = 'device'
	id = Column(Integer, primary_key=True)
	serial = Column(String(64), index=True, unique=True)
	description = Column(String(64), index=True)
	date = Column(DateTime, default=datetime.datetime.utcnow) # unique=True
	
	def __init__(self, serial, description):
		self.serial = serial
		self.description = description

	def __repr__(self):
		return '<serial %r>' % self.serial
