from mpi4py import MPI
import numpy

comm = MPI.COMM_WORLD
rank = comm.Get_rank()

N = 100

if rank==0:
    x = numpy.random.rand(N)
    comm.Send(x,dest=1,tag=0)

if rank==1:
    x = numpy.empty(N)
    info = MPI.Status()
    comm.Recv(x,source=0,tag=0,status=info)

    print info.Get_source(), info.Get_tag(), info.Get_count()
