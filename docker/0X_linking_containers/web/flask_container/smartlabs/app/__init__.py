from flask import Flask
from flask_restful import Api
from app.resources.devices import Devices
from app.resources.device_id import DeviceID
from app.resources.root import Root

# Declares app
app = Flask(__name__)
#Load default configurations, usually from developer environment
app.config.from_object('app.default_settings')
print("Database before " + app.config['DATABASE'])
#Overide configurations with the production server ones
app.config.from_envvar('SMARTLABS_SETTINGS', silent=True)
print("Database after " + app.config['DATABASE'])

# CORS
@app.after_request
def after_request(response):
	response.headers.add('Access-Control-Allow-Origin', '*')
	response.headers.add('Access-Control-Allow-Headers', 'Content-Type,Authorization')
	response.headers.add('Access-Control-Allow-Methods', 'GET,PUT,POST,DELETE')
	return response

# Routes
# API REST
#http://flask-restful-cn.readthedocs.org/en/0.3.5/reqparse.html
api = Api(app)
api.add_resource(Root, '/','/smartlabs','/smartlabs/api','/smartlabs/api/v1.0')
api.add_resource(Devices, '/smartlabs/api/v1.0/devices')
api.add_resource(DeviceID, '/smartlabs/api/v1.0/devices/<serial>')
