#Build image
docker build -t postgresql_base .

#Create a postgresql container with an active service
docker run -p 5432:5432 --name postgresql_database postgresql_base 

#Create a temporary container. Take into account the entrypoint is changing so you have to start postgresql manually
docker run --rm -itp 5432:5432 --name postgresql_database postgresql_base /bin/bash
