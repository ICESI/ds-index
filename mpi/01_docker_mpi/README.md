## Docker and MPI

This repository is a copy of Ole Weidner <ole.weidner@ed.ac.uk> repository with some modifications.

### Create the base image

With the code in **01_base_image** folder, you can build a Docker container that provides 
the OpenMPI runtime and tools along with various supporting libraries, 
including the MPI4Py Python bindings. The container also runs an OpenSSH server
so that multiple containers can be linked together and used via the user **mpirun**.

```
docker build -t openmpi .
```

### Create the cluster

With the code in **02_create_cluster** folder you can create a cluster of containers.
In this folder there is a file called 'docker-compose.yml' which is used by docker-compose
for deploying a mpi cluster based on docker containers 

```
mpi_head:
  image: openmpi
  ports: 
   - "22"
  links: 
   - mpi_node

mpi_node: 
  image: openmpi
```

The file defines an `mpi_head` and an `mpi_node`. Both containers run the same `openmpi` image. 
The only difference is, that the `mpi_head` container exposes its SHH server to 
the host system, so you can log into it to start your MPI applications.

The following command will start one `mpi_head` container and three `mpi_node` containers: 

```
$> docker-compose scale mpi_head=1 mpi_node=3
```

Once all containers are running, figure out the host port on which Docker exposes the  SSH server of the `mpi_head` container: 

```
$> docker ps | grep head
6d7fa452b951        openmpi:latest      "/usr/sbin/sshd -D"   7 minutes ago       Up 7 minutes        0.0.0.0:32769->22/tcp   03dockercompose_mpi_head_1  
```

Now you know the port, you can login to the `mpi_head` container. The username is **mpirun** and passwod is **mpirun**:

```
$> ssh -p 32769 mpirun@localhost
```

### DEMO

http://showterm.io/d97fe96c53c1a089f79ec

### Assignment

1. Propose and implement an strategy in order to self-create the machinefile once mpirun is logged into the cluster.

2. Instead of using a volume for sharing data among containers, do the necessary modifications among the deployment files to use a datacontainer. The datacontainer must have the helloworld.py, the get_ips.sh script and the machinefile.

###Troubleshooting

If you get this error: `ERROR: client and server don't have same version (client : 1.21, server: 1.18)
`. Run the following command:

```
export COMPOSE_API_VERSION=1.18
```
