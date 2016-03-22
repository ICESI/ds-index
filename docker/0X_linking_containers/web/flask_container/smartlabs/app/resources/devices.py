from app.database.db import session
from app.database.models import Device
from sqlalchemy import func

from flask_restful import Resource
from flask import Flask, jsonify, request
import json

class Devices(Resource):
	'''
	description: list devices
	input: nothing
	output: list of devices in json format
	test:
	'''
	def get(self):
		print('query all devices:')
		smartlab_devices = session.query(Device)
		device_array = []
		for device in smartlab_devices:
			device_array.append(device.serial)
		device_dict = {}
		device_dict["devices"] = device_array
		return json.dumps(device_dict)

	'''
	description: create a new device
	input: information of device in json format
	output: 
	'''
	def post(self):
		serial = request.json['serial']
		description = request.json['description']
		device = Device(serial,description)
		session.add(device)
		session.commit()
		return request.json