### Instructions

Once you have logged into the mpi cluser as the user mpirun, go to the shared volume (/tmp) and
use the script get_ips.sh to get all the ip addresses from the cluster and export script output to a file called machinefile

```
chmod +x get_ips.sh
. get_ips.sh > machinefile
```

Use the command below in order to execute the helloworld.py example. np argument
is used to specify the number of process to use with mpi. machinefile argument is
use to specify a file where the ip machines of the cluster are stored. The number
of process is divide evenly between the available machines (you can change this 
behaviour specifying how to divide the processes inside the machinefile)

```
mpiexec -np 2 -machinefile machinefile python helloworld.py
```

### Assignment

Create a cluster of 5 nodes and try to launch 10 processes.
