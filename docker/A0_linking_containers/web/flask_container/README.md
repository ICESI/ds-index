# Operating Systems www.icesi.edu.co/facultad_ingenieria/

# Docker - Flask base container

## Useful commands

### Caution!
The container must be rebuild once smartlabs sources is modified, this can be avoid
configurating the sources as an external volume

###Build image
Build flask_base image from Dockerfile

```sh
docker build -t flask_base .
```

###Create a container with an environment variable

```sh
docker run --rm -itp 8080:5000 -e "SMARTLABS_SETTINGS=production_settings.py" --name flask_web flask_base /bin/bash
```

###Create a temporary container

```sh
docker run --rm -itp 8080:5000 --name flask_web flask_base /bin/bash
```

###Create a temporary container with an attached volume

```sh
docker run --rm -itp 5000:5000 -v $(pwd)/smartlabs:/src/smartlabs --name flask_web ubuntu /bin/bash
```

###Create a temporary container with a modified entrypoint

```sh
docker run --rm -itp 8080:5000 --entrypoint=/bin/bash --name flask_web flask_base
```

###Create a container linked with a postregsql container

```sh
docker run -p 5000:5000 -d -e "SMARTLABS_SETTINGS=production_settings.py" --name flask_web --link postgresql_database:pg flask_base
```

