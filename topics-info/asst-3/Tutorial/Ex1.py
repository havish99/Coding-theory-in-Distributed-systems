import os 

os.environ["OPENBLAS_NUM_THREADS"] = '1'

from mpi4py import MPI

comm = MPI.COMM_WORLD

rank = comm.Get_rank()
size = comm.Get_size()

x = rank

print 'My rank is ', rank, ' out of ', size, x
