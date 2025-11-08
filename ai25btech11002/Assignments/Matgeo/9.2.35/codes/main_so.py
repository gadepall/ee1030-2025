import math
#import sys   
import numpy as np
import numpy.linalg as LA
import matplotlib.pyplot as plt
import matplotlib.image as mpim
from mpl_toolkits.mplot3d import Axes3D
from line.funcs import *
import ctypes
#local imports
from line.funcs import *
from triangle.funcs import *
from conics.funcs import *

#if using termux
#import subprocess
#import shlex
#end if

#setting up plot
fig = plt.figure()
ax = fig.add_subplot(111, aspect='equal')
len = 100
x = np.linspace(-8,8,len)


# Load compiled library
lib = ctypes.CDLL("./conics_params.so")

# Define argument and return types
lib.conpara.argtypes = [
    np.ctypeslib.ndpointer(dtype=np.double, ndim=1, flags="C_CONTIGUOUS"), # F
    np.ctypeslib.ndpointer(dtype=np.double, ndim=1, flags="C_CONTIGUOUS"), # V0
    np.ctypeslib.ndpointer(dtype=np.double, ndim=1, flags="C_CONTIGUOUS"), # V (flat)
    np.ctypeslib.ndpointer(dtype=np.double, ndim=1, flags="C_CONTIGUOUS"), # u
    ctypes.POINTER(ctypes.c_double)                                        # f pointer
]
lib.conpara.restype = None

# Example input (focus below vertex → opens downward)
F = np.array([0.0, 2.0], dtype=np.double)
V0 = np.array([0.0, 4.0], dtype=np.double)

# Output arrays
V = np.zeros(4, dtype=np.double)
u = np.zeros(2, dtype=np.double)
f = ctypes.c_double()

# Call C function
lib.conpara(F, V0, V, u, ctypes.byref(f))

# Reshape V and unpack f
V = V.reshape(2, 2)
f = f.value

print("V =\n", V)
print("u =", u)
print("f =", f)
# Ensure data types are consistent for conic_param()
f=float(f);
u=u.reshape(2,1)
n,c,F,O,lam,P,e = conic_param(V,u,f)
#print(n,c,F)

#Eigenvalues and eigenvectors

flen = parab_param(lam,P,u)

#Standard parabola generation
y = parab_gen(x,flen)


#Directrix
k1 = -8
k2 = 8

#Latus rectum
cl = (n.T@F).flatten()

#Generating lines
y_A = line_norm(n,c,k1,k2)#directrix
y_B = line_norm(n,cl[0],k1,k2)#latus rectum
#print(n,c)
yStandard =np.block([[y],[x]])

#Affine conic generation
Of = O.flatten()
yActual = P@yStandard + Of[:,np.newaxis]

#plotting
plt.plot(yActual[0,:],yActual[1,:],label='Parabola',color='r')
plt.plot(y_A[0,:],y_A[1,:],label='Directrix')
plt.plot(y_B[0,:],y_B[1,:],label='Latus Rectum')
#
colors = np.arange(1,3)
#Labeling the coordinates
tri_coords = np.block([O,F])
plt.scatter(tri_coords[0,:], tri_coords[1,:], c=colors)
vert_labels = ['$\mathbf{O}$','$\mathbf{F}$']
for i, txt in enumerate(vert_labels):
#    plt.annotate(txt, # this is the text
    plt.annotate(f'{txt}\n({tri_coords[0,i]:.0f}, {tri_coords[1,i]:.0f})',
                 (tri_coords[0,i], tri_coords[1,i]), # this is the point to label
                 textcoords="offset points", # how to position the text
                 xytext=(-20,5), # distance from text to points (x,y)
                 ha='center') # horizontal alignment can be left, right or center

# use set_position
ax = plt.gca()
ax.spines['top'].set_color('none')
ax.spines['left'].set_position('zero')
ax.spines['right'].set_color('none')
ax.spines['bottom'].set_position('zero')
'''
ax.spines['left'].set_visible(False)
ax.spines['right'].set_visible(False)
ax.spines['top'].set_visible(False)
ax.spines['bottom'].set_visible(False)
plt.xlabel('$x$')
plt.ylabel('$y$')
'''
plt.legend(loc='best')
plt.grid() # minor
plt.axis('equal')

# Save to figs folder
plt.savefig("../Figs/plot.png")
plt.show()
