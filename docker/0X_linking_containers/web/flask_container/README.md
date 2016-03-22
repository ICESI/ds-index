#Warning
The container must be rebuild once smartlabs sources is modified, this can be avoid
configurating the sources as an external volume

#Build image
docker build -t flask_base .

#Create a container with an environment variable
docker run --rm -itp 8080:5000 -e "SMARTLABS_SETTINGS=production_settings.py" --name flask_web flask_base /bin/bash

#Create a temporary container
docker run --rm -itp 8080:5000 --name flask_web flask_base /bin/bash

#Create a temporary container with a modified entrypoint
docker run --rm -itp 8080:5000 --entrypoint=/bin/bash --name flask_web flask_base

#Create a container linked with a postregsql container
docker run -p 5000:5000 -d -e "SMARTLABS_SETTINGS=production_settings.py" --name flask_web --link postgresql_database:pg flask_base

##Others
#How to modify parameters of the machine
https://docs.docker.com/engine/reference/run/

#Create a temporary container with an attached volume
docker run --rm -itp 5000:5000 -v $(pwd)/smartlabs:/src/smartlabs --name flask_web ubuntu /bin/bash
