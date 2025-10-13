import ctypes as ct
import numpy as np
from numpy.lib import scimath as np_scimath

lib = ct.CDLL("./problem.so")

lib.give_data.argtypes = [
    ct.POINTER(ct.c_double), ct.POINTER(ct.c_double), ct.POINTER(ct.c_double),
    ct.POINTER(ct.c_double), ct.POINTER(ct.c_double), ct.POINTER(ct.c_double)
]

pointsA = ct.c_double * 4
pointsu = ct.c_double * 2
pointsc = ct.c_double * 1
pointsp = ct.c_double * 2
pointsm = ct.c_double * 2
points = ct.c_double * 5

A = pointsA()
u = pointsu()
c = pointsc()
p = pointsp()
m = pointsm()
data = points()

lib.give_data(A, u, c, p, m, data)

A = np.array([[A[0], A[1]], [A[2], A[3]]])
u = np.array([[u[0]], [u[1]]])
p = np.array([[p[0]], [p[1]]])
m = np.array([[m[0]], [m[1]]])
c = c[0]

a1 = float(m.T @ A @ m)
b1 = float(2 * (p.T @ A @ m + u.T @ m))
c1 = float(p.T @ A @ p + 2 * u.T @ p + c)

D = b1**2 - 4 * a1 * c1

t1 = (-b1 + np_scimath.sqrt(D)) / (2 * a1)
t2 = (-b1 - np_scimath.sqrt(D)) / (2 * a1)

x1 = p + t1 * m
x2 = p + t2 * m

print("Intersection 1:", x1)
print("Intersection 2:", x2)

def send_data():
    return data, x1[0,0], x1[1,0], x2[0,0], x2[1,0]

