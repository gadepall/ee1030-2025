from ctypes import *

filename = './libmain.so'


# Load the shared object file (pgm.so)
clib = CDLL(filename)

def solve(A,x):
    m=len(A)
    r = clib.solve
    q = c_double*m
    r.restype =POINTER(q) 
    t = c_double*m*m
    r.argtypes = [c_int, t,q]

    t1 = c_double*m
    b = t1()
    a = t()
    for i in range(m):
        for j in range(m):
            a[i][j]=A[i][j]
    for i in range(m):
        b[i]=x[i]
    return list(r(m,a,b).contents)


print(solve([[2,3],
      [2,4]],[11,-24]
     ))

