import numpy as np
import numpy.linalg as LA
import scipy.linalg as SA
import matplotlib.pyplot as plt
import matplotlib.image as mpimg

#local imports
from line.funcs import *
from triangle.funcs import *
from conics.funcs import circ_gen

#if using termux
#import subprocess
#import shlex
#end if

#Triangle vertices
A = np.array([5, 0]).reshape(-1, 1)
B = np.array([0, 0]).reshape(-1, 1) 
C = np.array([6 * np.cos(np.deg2rad(60)), 6 * np.sin(np.deg2rad(60))]).reshape(-1, 1) 

#Triangle sides
c = LA.norm(A - B)
a = LA.norm(B - C)
b = LA.norm(C - A)

#Direction Vectors
m1 = dir_vec(A, B)
m2 = dir_vec(B, C)
m3 = dir_vec(C, A)

#Line parameters
n1 = norm_vec(A, B)
c1 = n1.T @ A
n2 = norm_vec(B, C)
c2 = n2.T @ B
n3 = norm_vec(C, A)
c3 = n3.T @ C

#Area
arvec = np.cross(m1[:, 0], m3[:, 0])
area = 1 / 2 * LA.norm(arvec)

#Angles
angA = np.degrees(np.arccos((-m1.T @ m3) / (c * b)))
angB = np.degrees(np.arccos((-m1.T @ m2) / (c * a)))
angC = np.degrees(np.arccos((-m2.T @ m3) / (a * b)))

#Writing sides to excel (unchanged)
sides = np.array([a, b, c]).reshape(-1, 1)
columns = ['a', 'b', 'c']

#Generating all lines
x_AB = line_gen(A, B)
x_BC = line_gen(B, C)
x_CA = line_gen(C, A)

#Plotting all lines
plt.plot(x_AB[0, :], x_AB[1, :], label='$c$')
plt.plot(x_BC[0, :], x_BC[1, :], label='$a$')
plt.plot(x_CA[0, :], x_CA[1, :], label='$b$')

#Labeling the coordinates (removed vertex labels)
tri_coords = np.block([[A, B, C]])
plt.scatter(tri_coords[0, :], tri_coords[1, :])

plt.xlabel('$x$')
plt.ylabel('$y$')
plt.legend(loc='best')
plt.grid() # minor
plt.axis('equal')

#if using termux
plt.savefig('../Figs/plot.png')
plt.show()
