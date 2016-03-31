import sys
sys.path.append("..") # Adds higher directory to python modules path.

from app.database.db import session
from app.database.db import engine
from app.database.models import Base
from app.database.models import Device
from sqlalchemy import func, join
import sys

#If there is just one argument exit, first argument is the script name
if len(sys.argv) == 1:
	print("usage: python dbmanage.py create/drop/truncate")
	sys.exit()

#Get the second argument
action = sys.argv[1]

if action == "create":
	Base.metadata.create_all(engine)

if action == "drop":
	Base.metadata.drop_all(engine)

if action == "truncate":
	Base.metadata.drop_all(engine)
	Base.metadata.create_all(engine)

if action == "insert":
	device = Device('SN0001','GPS Garmin')
	session.add(device)
	session.commit()

	device = Device('SN0002','Battery 3.3V')
	session.add(device)
	session.commit()

if action == "read":
	#query one device
	print('query one device:')
	smartlab_device = session.query(Device).filter_by(serial='SN0001').first()
	print(smartlab_device.serial,"-",smartlab_device.description)

	#query all devices
	print('query all devices:')
	smartlab_devices = session.query(Device)
	for device in smartlab_devices:
		print(device.serial,"-",device.description)

if action == "delete":
	session.query(Device).filter_by(serial='SN0001').delete()
	session.commit()

if action == "update":
	session.query(Device).filter_by(serial='SN0001').update({'description':'GPS Atmel'})
	session.commit()