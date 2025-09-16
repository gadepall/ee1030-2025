import ctypes
import numpy as np
import sympy as sp

lib = ctypes.CDLL("./problem.so")

lpoint=[0, 0, 0]
lvec=[0, 0, 0]

for i in range(0,3):
    lpoint[i] = lib.get_lpoint1(i)

for i in range(0,3):
    lvec[i] = lib.get_lpoint1(i) - lib.get_lpoint2(i)

print("Line equation is: ",lpoint,"+ k",lvec)

A = sp.Matrix([[2,0,3,1],
              [1,1,5,1],
              [3,2,4,1]])

rref, pivots = A.rref()

e = (rref[0,3],rref[1,3], rref[2,2])

print("Plane equation is: ", e[0],"x+",e[1],"y+",e[2],"/5z=",rref[0,0])

