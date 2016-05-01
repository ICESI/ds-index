# Distributed Systems www.icesi.edu.co/facultad_ingenieria/

# Docker - Introduction to Restrictions

### Build an image
```sh
$ docker build -t flask_image .
```

### Create a container and establish limits
Use the following command to limit CPU consumption of a container to 50%

```sh
$ docker run --rm -p 8080:5000 --cpu-quota=50000 flask_image
```

### Test the application 
```sh
$ curl 127.0.0.1:8080/greedy
```

### Check CPU consumption
```sh
$ top
```