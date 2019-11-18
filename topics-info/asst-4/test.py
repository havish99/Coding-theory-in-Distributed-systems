from mpi4py import MPI
import sys
import time
import os
os.environ["OPENBLAS_NUM_THREADS"] = '1'
import numpy as np
sum1=0
r=9000
c=9000
for i in range(50):
 t1=0
 comm=MPI.COMM_WORLD
 size=comm.Get_size()
 rank=comm.Get_rank()
 if size==1:
	 m=r
 else:
	 m=r/(size-1)
 assert m>=1
 comm.Barrier()
 if rank==0:
	 a=np.random.rand(r,c)
	 x=np.random.rand(c,1)
	 for j in range(1,size):
		  comm.Send(a[(j-1)*m:m*j,:],dest=j,tag=j)
	 ts=MPI.Wtime()
	 comm.Bcast(x,root=0)
	 res1=np.empty(m)
	 for j in range(1,size):
		 row=np.empty(m)
		 comm.Recv(row,source=j,tag=j)
		 res1=np.hstack((res1,row))
	 t2=MPI.Wtime()-ts
	 sum1=sum1+t2
	 #print sum1
 
 if rank!=0:
	 x=np.empty(c)
	 recv1=np.empty((m,c))
	 comm.Recv(recv1,source=0,tag=rank)	 
	 comm.Bcast(x,root=0)
	 recvd=(recv1.dot(x))
	 wait = np.random.exponential(0.01)
	 time.sleep(wait)
	 comm.Send(recvd,dest=0,tag=rank)
 time.sleep(0.5)
print (sum1/50)
		
		
