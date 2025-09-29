from ctypes import *

filename = './libmain.so'

clib = CDLL(filename)

def rank(arr):
    m=len(arr)
    n=len(arr[0])
    r = clib.rank
    r.restype = c_int
    t = c_double*n*m
    r.argtypes = [c_int, c_int , t]

    t1 = c_double*n

    a = t(t1(),t1())
    for i in range(m):
        for j in range(n):
            a[i][j]=arr[i][j]

    print(r(m,n,a))


rank([[-240,360,120],
      [-2,2,1],
      [-1,1,.5]]
     )


