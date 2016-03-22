#
# example Dockerfile for flask service
# Read this please: https://glyph.twistedmatrix.com/2015/03/docker-deploy-double-dutch.html
# Read this please: https://caremad.io/2013/07/setup-vs-requirement/
# Read this please: http://flask.pocoo.org/docs/0.10/patterns/distribute/#distribute-deployment
# Explain this command: pip wheel . , Can setup.py be self-generated?
# 

FROM ubuntu
MAINTAINER daniel.barragan@correo.icesi.edu.co

#The lastest image of ubuntu already have python
RUN apt-get update && apt-get install -y python python-pip python-dev libpq-dev
RUN pip install virtualenv

#Create user flask
RUN useradd -ms /bin/bash flask

# Run the rest of the commands as the ``flask`` user 
USER flask

#Change directory
WORKDIR /home/flask

#Create virtualenvironment for flask
RUN virtualenv flask_env

#Copy source code into container
ADD smartlabs /home/flask/smartlabs

#Change directory
WORKDIR /home/flask/smartlabs

# #Activate virtualenvironment and install dependencies
RUN . /home/flask/flask_env/bin/activate; pip install -r requirements.txt  

# Expose the 8080 port
EXPOSE 8080

ENTRYPOINT . /home/flask/flask_env/bin/activate; \
           cd /home/flask/smartlabs; \
           python runserver.py

