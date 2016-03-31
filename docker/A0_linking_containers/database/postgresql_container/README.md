# Operating Systems www.icesi.edu.co/facultad_ingenieria/

# Docker - Postgresql base container

## Useful commands

###Build image
Build postgresql_base image from Dockerfile

```sh
docker build -t postgresql_base .
```

###Create a postgresql container
Create a postgresql container with an active service

```sh
docker run -p 5432:5432 --name postgresql_database postgresql_base 
```

###Create a temporary container
Create a temporary container in interactive mode, take into account the entrypoint is changing so you have to start postgresql manually

```sh
docker run --rm -itp 5432:5432 --name postgresql_database postgresql_base /bin/bash
```