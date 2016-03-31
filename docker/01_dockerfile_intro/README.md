# Operating Systems www.icesi.edu.co/facultad_ingenieria/

# Docker - Introduction to Dockerfiles

### Extracting sources.list 

The following commands allow to extract the sources.list file from an ubuntu container

```sh
$ docker run --rm -it -v $(pwd):/mirror --name apache2_container ubuntu /bin/bash
# cp /etc/apt/sources.list /temporal
# exit
$ vi /mirror/sources.list
:%s/archive.ubuntu.com/192.168.131.253
```

### Build apache2 docker image

Use the following command to create apache2 image from Dockerfile

```sh
$ docker build -t apache2 .
docker run -d -v $(pwd)/html:/var/www/html/ -p 8080:80 --name apache2_container apache2
```