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


a,d,a2,d2=0,2*5,8,4
b,c,b2=0,5*5,10
rank([[a2-d2,a2,a2+d2],[b2-d2,b2,b2+d2],[a-b+c-d,a-b,a-b-c+d]])


