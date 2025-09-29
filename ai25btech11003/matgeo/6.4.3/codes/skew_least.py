#Code by GVV Sharma

#September 21, 2012

#Revised July 26, 2024

#Released under GNU/GPL

import numpy as np

import matplotlib.pyplot as plt

from numpy.linalg import inv

from numpy import linalg as LA

#Creating matrices

m1 = np.array(([3,2,6])).reshape(-1,1) # direction of first line
m2 = np.array(([1,2,2])).reshape(-1,1) # direction of second line
P1 = np.array(([2,-5,1])).reshape(-1,1) # point on first line
P2 = np.array(([7,0,-6])).reshape(-1,1) # point on second line

b = P2-P1 # B - A

A = np.block([m1,-m2]) # use [m1, -m2] so A @ [λ, μ] ≈ b

ans = (1/80)*np.array(([ -2107, -372])).reshape(-1,1) # optional: expected scaled params for reference

#Least squares solution

x_ls = LA.lstsq(A,b,rcond=None)

print(x_ls)
