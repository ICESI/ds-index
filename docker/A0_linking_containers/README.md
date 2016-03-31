# Operating Systems www.icesi.edu.co/facultad_ingenieria/

# Docker - Linking Containers


This example allows developer to run the application in a development environment and a production
environment without making any changes to the source code. This is done through environment variables of the
operating system. In the following piece of code the application checks if SMARTLABS_SETTINGS environment 
variable exist, if the variable do not exist, default settings at default_settings.py are employed.

**__init__.py**
```python
# Declares app
app = Flask(__name__)
#Load default configurations, usually from developer environment
app.config.from_object('app.default_settings')
#Overide configurations with the production server ones
app.config.from_envvar('SMARTLABS_SETTINGS', silent=True)
```

In the sections below, instructions for executing linking container example are presented

### Clone the repository

Clone distributed system repository and go to ***docker/0X_linking_containers*** folder

```sh
git clone https://github.com/ICESI/distributed-systems.git
```

### Build the base images

Go to ***database/postgresql_container/*** and build the base image for postgresql

```sh
$ docker build -t postgresql_base .
```

Go to ***web/flask/container/*** and build the base image for flask
```sh
$ docker build -t flask_base .
```

### Create a postgresql container from base image

Create a postgresql container from base image. The container starts with the postgresql service activated
```sh
$ docker run -p 5432:5432 --name postgresql_database postgresql_base 
```

### Create a schema and populate the database

You must write down the ip of *docker0* interface and edit the file
***web/flask_container/smartlabs/app/default_settings.py*** 

**default_settings.py**
```python
DEBUG=True,
DATABASE='postgresql://smartlabs:smartlabspass@192.168.99.100:5432/smartlabs'
```

Then run the script dbmanage.py from ***web/flask_container/smartlabs/scripts***
to create the schema for the test application and populate the tables

```sh
$ python dbmanage.py create
$ python dbmanage.py insert
```

### Check environment variables between containers

Create a temporary container linked with the previous postresql_database created container. This
is done just to show that some environment variables are created. pg is an alias for the connection

```sh
$ docker run --rm -it --name temporary_client --link postgresql_database:pg ubuntu bash
# env
```

From the output of the ***env*** command you can check that PG_PORT_5432_TCP_PORT and 
PG_PORT_5432_TCP_ADDR variables were created. You can type exit to leave the container and it will
be self-destroyed due to the --rm docker parameter


### Link flask container and previous created postgresql container

First step is to check the contents at ***web/flask_container/smartlabs/app/production_settings.py***

**production_settings.py**
```python
import os

DEBUG=False,
PORT=os.getenv("PG_PORT_5432_TCP_PORT"),
ADDRESS= os.getenv("PG_PORT_5432_TCP_ADDR"),
if PORT[0] != None and ADDRESS[0] != None:
	DATABASE='postgresql://smartlabs:smartlabspass@'+ADDRESS[0]+':'+PORT[0]+'/smartlabs'
```

Second step is to create SMARTLABS_SETTINGS environment variable in your production environment, this is done with the docker -e parameter. It substitutes the following command in an operating system.

```sh
export SMARTLABS_SETTINGS=production_settings.py
```

When flask server starts, its relative path is inside app folder ***web/flask_container/smartlabs/app*** so it is expected that production_settings.py reside in this folder  

Finally create a flask container linked with the previous created postregsql container. 

```sh
$ docker run -p 5000:5000 -d -e "SMARTLABS_SETTINGS=production_settings.py" --name flask_web --link postgresql_database:pg flask_base
```

### Activity
Linking docker containers is now deprecated, use docker networking for linking containers as show in [**Docker Networking**][container-networking]

### References
[**Link environment variables reference**][container-environment] <br/>
[**Modify container parameters**][container-settings] <br/>
[**Docker Networking**][container-networking]

[container-environment]: https://docs.docker.com/compose/link-env-deprecated/
[container-settings]: https://docs.docker.com/engine/reference/run/
[container-networking]: https://www.rethinkdb.com/blog/docker-networking/
