#Operating Systems www.icesi.edu.co/facultad_ingenieria/

#Docker Containers

#Linking Containers

In order to execute this example you must follow the instructions above

##Build the base images

*Build the base image for postgresql
$docker build -t postgresql_base .

*Build the base image for flask
$docker build -t flask_base .

##Create a postgresql container from base image

*Create a postgresql container from base image with a postgresql active service
$docker run -p 5432:5432 --name postgresql_database postgresql_base 

##Create a schema and populate the database

*Run script dbmanage.py from /web/flask_container/smartlabs/scripts
$python dbmanage.py create
$python dbmanage.py insert

##Create a flask container linked with the previous created postgresql container

*Create a flask container linked with the previous created postregsql container
docker run -p 5000:5000 -d -e "SMARTLABS_SETTINGS=production_settings.py" --name flask_web --link postgresql_database:pg flask_base
