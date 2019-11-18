from mpi4py import MPI

comm = MPI.COMM_WORLD
rank = comm.Get_rank()

if rank==0:
    x = 42
    comm.send(x,dest=1,tag=1)

if rank==1:
    x = comm.recv(source=0,tag=1)
    print x
