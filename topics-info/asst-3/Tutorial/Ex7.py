from mpi4py import MPI
import numpy

comm = MPI.COMM_WORLD
rank = comm.Get_rank()

N = 3

if rank==1:
    x = numpy.random.rand(N)
    comm.Send(x,dest=0,tag=1)
    print 'Sending x=',x

if rank==2:
    y = numpy.random.rand(N)
    comm.Send(y,dest=0,tag=2)
    print 'Sending y=',y

if rank==0:
    info = MPI.Status()
    temp = numpy.empty(N)
    for i in range(2):
        comm.Recv(temp,source=MPI.ANY_SOURCE,tag=MPI.ANY_TAG,status=info)
        if info.Get_source()==1:
            x = temp.copy()
        else:
            y = temp.copy()
    print 'x is ',x
    print 'y is ',y


