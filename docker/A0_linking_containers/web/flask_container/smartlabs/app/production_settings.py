import os

DEBUG=False,
PORT=os.getenv("PG_PORT_5432_TCP_PORT"),
ADDRESS= os.getenv("PG_PORT_5432_TCP_ADDR"),
print("PORT",PORT[0])
print("ADDRESS",ADDRESS[0])
if PORT[0] != None and ADDRESS[0] != None:
	DATABASE='postgresql://smartlabs:smartlabspass@'+ADDRESS[0]+':'+PORT[0]+'/smartlabs'