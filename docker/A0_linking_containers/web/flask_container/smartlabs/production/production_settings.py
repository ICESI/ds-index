import os

DEBUG=False,
PORT=os.environ["PG_PORT_5432_TCP_PORT"],
ADDRESS=os.environ["PG_PORT_5432_TCP_ADDR"],
DATABASE='postgresql://smartlabs:smartlabspass@'+ADDRESS+':'+PORT+'/smartlabs'
