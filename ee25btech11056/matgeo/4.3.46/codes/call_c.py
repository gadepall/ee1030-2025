import sys
import ctypes
import numpy as np
import matplotlib.pyplot as plt
import os

#for generating figure in figs folder
figs_folder= os.path.join("..","figs")


#loading shared object , load the file into lib which is an objedt

lib = ctypes.CDLL("./points.so")              #ctypes constructor to load a shared c library
lib.intersection.restype = ctypes.c_double    #to tell the return type is a c double
lib.intersection.argtypes=[]                  # to tell that function takes no arguments

#call the c function , by using attributes for lib
k_val = lib.intersection()

if (k_val == -1) :
    print("no solution found")
    sys.exit(0)

print(f"solution found k = {k_val}")

#writing points in the form of array for line

#parametric form of the given line
t = np.linspace(-5,5,200)

p = 2 + (-1)*t
q = (-3) + t
r = 1 + 6*t

#for plane

#coefficients for plane equation
a,b,c,d=2,1,1,7


l = np.linspace(-10,10,100)
m = np.linspace(-10,10,100)
l,m = np.meshgrid(l,m)

n = (d - a*l -b*m)/c

#plot

fig = plt.figure(figsize=(8,6))

ax = fig.add_subplot(111,projection="3d")

#line 
ax.plot(p,q,r,label='line',color='red',linewidth=2)

ax.scatter(1,-2,7,color='black',s=5,label='P(1,-2,7)')
ax.scatter(3,-4,-5,color='green',s=5,label='A(3,-4,-5)')
ax.scatter(2,-3,1,color='yellow',s=5,label='B(2,-3,1)')

#plane 
ax.plot_surface(l,m,n,alpha=0.5,color='blue',edgecolor='none')  #edgecolor='none' means edges are not drawn for the mesh and hence surface appears smooth without grid lines.

ax.set_xlabel("X Axis")
ax.set_ylabel("Y Axis")
ax.set_zlabel("Z Axis")
ax.set_title("Line and Plane")
ax.grid(True)
ax.legend()

plt.tight_layout()
fig.savefig(os.path.join(figs_folder,"intersection.png"))    #savingfig using figure object
plt.show()





