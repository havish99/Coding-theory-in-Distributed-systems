import os 
import time 

os.environ["OPENBLAS_NUM_THREADS"] = '1'

import numpy as np 
from mpi4py import MPI 

np.random.seed(42)
A = np.random.normal(0,1,(9000,45000))
x = np.random.normal(0,1,(45000,1))

start = time.time()
y = A.dot(x)
end = time.time()
print(end-start)
