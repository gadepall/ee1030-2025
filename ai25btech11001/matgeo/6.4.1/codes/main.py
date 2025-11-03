from ctypes import *

filename = './libmain.so'

clib = CDLL(filename)

def linreg(X,D):
    m=len(X)
    r = clib.linearreg
    r.restype = None
    t = (c_double*m)*1
    l = c_double*1*2
    r.argtypes = [c_int, t,t,POINTER(l)]

    a = t()
    for i in range(m):
            a[0][i]=X[i]
    b = t()
    for i in range(m):
            b[0][i]=D[i]
    c = l()

    r(m,a,b,pointer(c))
    return [list(i) for i in c]
def value(N,x):
    r = clib.value
    r.restype = c_double
    l = c_double*1*2
    r.argtypes = [l,c_double]
    
    a = l()
    a[0][0] = N[0][0]
    a[1][0] = N[1][0]

    return r(a,x)

X = [2001 ,2002 ,2003,2004,2005,2006]
print(X)

D = [30,35,36,32,37,40]
N = linreg(X,D)
print(N)
print(value(N,2008))


