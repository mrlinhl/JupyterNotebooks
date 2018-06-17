import time
import numpy as np
from scipy import sparse, io
from scipy.sparse.linalg import dsolve
mtx = io.mmread('viscoplastic1.mtx')
rhs = io.mmread('viscoplastic1_b.mtx')
mtx = mtx.tocsr()

time_start=time.time()
dsolve.spsolve(mtx, rhs)
time_end=time.time()
print('viscoplastic1,csr,use_umfpack  time cost',time_end-time_start,'s')

time_start=time.time()
dsolve.spsolve(mtx, rhs, use_umfpack=True)
time_end=time.time()
print('viscoplastic1,csr,use_umfpack=True  time cost',time_end-time_start,'s')

time_start=time.time()
dsolve.spsolve(mtx, rhs, use_umfpack=False)
time_end=time.time()
print('viscoplastic1,csr,use_umfpack=False  time cost',time_end-time_start,'s')

mtx = mtx.tocsc()

time_start=time.time()
dsolve.spsolve(mtx, rhs)
time_end=time.time()
print('viscoplastic1,csc,use_umfpack  time cost',time_end-time_start,'s')

time_start=time.time()
dsolve.spsolve(mtx, rhs, use_umfpack=True)
time_end=time.time()
print('viscoplastic1,csc,use_umfpack=True  time cost',time_end-time_start,'s')

time_start=time.time()
dsolve.spsolve(mtx, rhs, use_umfpack=False)
time_end=time.time()
print('viscoplastic1,csc,use_umfpack=False  time cost',time_end-time_start,'s')


mtx = io.mmread('viscoplastic2.mtx')
rhs = io.mmread('viscoplastic2_b.mtx')
mtx = mtx.tocsr()

time_start=time.time()
dsolve.spsolve(mtx, rhs)
time_end=time.time()
print('viscoplastic2,use_umfpack  time cost',time_end-time_start,'s')

time_start=time.time()
dsolve.spsolve(mtx, rhs, use_umfpack=True)
time_end=time.time()
print('viscoplastic2,use_umfpack=True  time cost',time_end-time_start,'s')

time_start=time.time()
dsolve.spsolve(mtx, rhs, use_umfpack=False)
time_end=time.time()
print('viscoplastic2,use_umfpack=False  time cost',time_end-time_start,'s')