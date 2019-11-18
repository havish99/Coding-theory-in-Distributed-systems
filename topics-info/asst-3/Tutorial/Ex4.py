from mpi4py import MPI
import numpy as np

comm = MPI.COMM_WORLD
rank = comm.Get_rank()

N = 5

if rank==0:
    x = np.random.rand(N)
    comm.Send(x,dest=1)
    print x

if rank==1:
    x = np.empty(N)
    comm.Recv(x,source=0)
    print x
