from ctypes import *
import time
filename = './libmain.so'

clib = CDLL(filename)

def inv(mat):
    m=len(mat)
    r = clib.inv
    t = c_double*m
    t=t*m
    r.restype = None
    r.argtypes = [c_int, t,t]
    t1 = t()
    for i in range(m):
        for j in range(m):
            t1[i][j]=mat[i][j]
    ma = t()
    r(m,t1,ma)
    l1 = list(ma)
    for i in range(m):
        l1[i]=list(l1[i])
    return l1

a = inv([[2,3,1],[2,4,1],[3,7,2]])
print(a)


