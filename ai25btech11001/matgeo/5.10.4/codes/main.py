from ctypes import *

filename = './libmain.so'

clib = CDLL(filename)

def rref(arr):
    m=len(arr)
    n=len(arr[0])
    r = clib.rref
    t = c_double*n*m
    r.restype = POINTER(t)
    r.argtypes = [c_int, c_int , t]

    a = t()
    for i in range(m):
        for j in range(n):
            a[i][j]=arr[i][j]
    mat = list(r(m,n,a).contents)
    for i in range(m):
        mat[i] = list(mat[i]) 
    return mat


print(rref([[1, 0, -1, 0],[2,0,0,-1],[0,2,0,-1],[0,1,-1,0]]))


