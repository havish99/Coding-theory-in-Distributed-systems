from mpi4py import MPI
import numpy

comm = MPI.COMM_WORLD
rank = comm.Get_rank()

N = 3
if rank==0:
    x = numpy.random.rand(N)

if rank!=0:
    x = numpy.empty(N)

comm.Bcast(x,root=0)

print x, rank
