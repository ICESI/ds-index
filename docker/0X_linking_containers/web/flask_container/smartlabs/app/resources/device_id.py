from app.database.db import session
from app.database.models import Device
from sqlalchemy import func

from flask_restful import Resource
from flask import Flask, jsonify, request
import json

class DeviceID(Resource):
	'''
	description: return a specific device
	input: 
	output: 
	test:
	'''
	def get(self,serial):
		print(serial)
		print('query one device:')
		smartlab_device = session.query(Device).filter_by(serial=serial).first()
		data = {}
		data['serial'] = smartlab_device.serial
		data['description'] = smartlab_device.description
		data['date'] = str(smartlab_device.date)
		json_data = json.dumps(data)
		return json_data

	'''
	description: if a device exist, update it
	input: 
	output: 
	test:
	'''
	def put(self,serial):
		print(serial)
		description = request.json['description']
		print(description)
		session.query(Device).filter_by(serial=serial).update({'description':description})
		session.commit()

		smartlab_device = session.query(Device).filter_by(serial=serial).first()
		data = {}
		data['serial'] = smartlab_device.serial
		data['description'] = smartlab_device.description
		data['date'] = str(smartlab_device.date)
		json_data = json.dumps(data)
		return json_data
		
	'''
	description: delete a device
	input: 
	output: 
	test:
	'''
	def delete(self,serial):
		print(serial)
		session.query(Device).filter_by(serial=serial).delete()
		session.commit()
		return serial