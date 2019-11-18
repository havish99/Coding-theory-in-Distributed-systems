from mpi4py import MPI
import numpy as np

comm = MPI.COMM_WORLD
rank = comm.Get_rank()

N = 10000

if rank==0:
    x = np.random.rand(N)
    comm.Send(x,dest=1)
    y = np.empty(N)
    comm.Recv(y,source=1)

if rank==1:
    
    x = np.empty(N)
    comm.Recv(x,source=0)
    y = np.random.rand(N)
    comm.Send(y,dest=0)
