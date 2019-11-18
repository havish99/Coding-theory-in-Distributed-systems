import os 
import time 

os.environ["OPENBLAS_NUM_THREADS"] = '1'

import numpy as np 
from mpi4py import MPI 


comm = MPI.COMM_WORLD
rank = comm.Get_rank()
num_workers = comm.Get_size()-1
# number of workers are 5 and 1 master node
num_splits = 4
N = (9000,9000)
N1 = (9000,1)
beta = 0.02
G = [[1,0,0,0,1],[0,1,0,0,1],[0,0,1,0,1],[0,0,0,1,1]]
for i in range(20):
	if rank==0:
		
		G = np.array(G)
		A = np.random.normal(0,1,N)
		x = np.random.normal(0,1,N1)
		split = []
		for i in range(0,num_splits):
			split.append(A[(i)*N[0]/num_splits:(i+1)*N[0]/num_splits,:])
		lst = []
		for i in range(5):
			temp = G[0][i]*split[0] + G[1][i]*split[1] + G[2][i]*split[2] + G[3][i]*split[3]
			lst.append(temp)
		workers_send = np.array(lst)
		for i in range(0,num_workers):
			comm.Send(workers_send[i],dest = i+1)
		
		start = time.time()
		# print(i)
		comm.Bcast(x,root=0)
		info = MPI.Status()
		y = []
		indices = []
		# #### the decoding part ####
		y = np.empty((num_splits,(N1[0]/num_splits)))
		for i in range(4):
			comm.Recv(y[i],source=MPI.ANY_SOURCE,status=info)
			indices.append(info.Get_source()-1)
		G1 = [G[:,indices[0]],G[:,indices[1]],G[:,indices[2]],G[:,indices[3]]]
		G1 = np.array(G1)
		ans = np.matmul(y.T,np.linalg.inv(G1.T))
		ans = ans.reshape(N1)
 		end = time.time()
		print(end-start)
		for i in range(1):
			comm.Recv(temp,source=MPI.ANY_SOURCE,status=info)
	else:

		A1 = np.empty((N[0]/num_splits,N[1]))
		x1 = np.empty(N1)
		comm.Recv(A1,source=0)
		comm.Bcast(x1, root=0)
		y = A1.dot(x1)
		wait = np.random.exponential(beta)
		time.sleep(wait)
		comm.Send(y,dest=0)
	time.sleep(0.5)
