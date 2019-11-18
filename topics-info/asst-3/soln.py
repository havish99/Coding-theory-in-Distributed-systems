import os 
import time 

os.environ["OPENBLAS_NUM_THREADS"] = '1'

import numpy as np 
from mpi4py import MPI 

np.random.seed(42)
comm = MPI.COMM_WORLD
rank = comm.Get_rank()
num_workers = comm.Get_size()-1
# number of workers are 4 and 1 master node
N = (9000,9000)
N1 = (9000,1)
beta = 0
for i in range(20):
	if rank==0:
		A = np.random.normal(0,1,N)
		x = np.random.normal(0,1,N1)
		for i in range(0,num_workers):
			comm.Send(A[(i)*N[0]/num_workers:(i+1)*N[0]/num_workers,:],dest = i+1)
		start = time.time()
		comm.Bcast(x,root=0)
		y=np.empty((0,1))
		for i in range(0,num_workers):
			y1=np.empty((N[0]/num_workers,1))
			comm.Recv(y1,source=i+1)
    		np.vstack((y,y1))
 		end = time.time()
		print(end-start)
	else:
		A1 = np.empty((N[0]/num_workers,N[1]))
		x1 = np.empty(N1)
		comm.Recv(A1,source=0)
		comm.Bcast(x1, root=0)
		y = A1.dot(x1)
		wait = np.random.exponential(beta)
		time.sleep(wait)
		comm.Send(y,dest=0)
	time.sleep(0.5)
