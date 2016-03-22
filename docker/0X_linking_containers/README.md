
Following are the execution instructions

#Build the image postgresql_base
docker build -t postgresql_base .

#Build the image flask_base
docker build -t flask_base .

#Create a postgresql container with an active service
docker run -p 5432:5432 --name postgresql_database postgresql_base 

#Run script dbmanage.py script from /web/flask_container/smartlabs/scripts
python dbmanage.py create
python dbmanage.py insert

#Create a container linked with a postregsql container
docker run -p 5000:5000 -d -e "SMARTLABS_SETTINGS=production_settings.py" --name flask_web --link postgresql_database:pg flask_base
