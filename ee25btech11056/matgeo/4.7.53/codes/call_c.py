import ctypes
import sys
import os
import numpy as np
import matplotlib.pyplot as plt

#for generating figure in figs folder
figs_folder= os.path.join("..","figs")

#loading shared object 
lib = ctypes.CDLL("./points.so")

#tell ctypes about the function signature
lib.normal.restype = ctypes.POINTER(ctypes.c_double)       #returns pointer to double
lib.normal.argtypes = [ctypes.POINTER(ctypes.c_double)]    #takes pointer to array

#defining point P as a list(array) to pass it as input to c function
P = (ctypes.c_double * 3)(1,2,-3)

#calling c function
n_ptr = lib.normal(P)  #storing the return value in n_ptr that points to memory location of [1,2,-3]

#extracting values into a python list using for loop
n = [n_ptr[i] for i in range(3)] 

#conveting to numpy for plotting

n = np.array(n)
point = np.array([1,2,-3])  #point P that lies on the plane

#Plane equation
x = np.linspace(-10,10,100)
y = np.linspace(-10,10,100)

x,y = np.meshgrid(x,y)

d = n[0]*point[0] + n[1]*point[1] + n[2]*point[2]

z = (d - n[0]*x -n[1]*y)/n[2]

#plotting

fig = plt.figure(figsize=(8,6))

ax = fig.add_subplot(111,projection="3d")

ax.plot_surface(x,y,z,alpha=0.5,color='blue',edgecolor='none')

ax.scatter(*point,color='red',s=2,label="P(1,2,-3)")


#plotting normal vector OP 
ax.quiver(0,0,0,n[0],n[1],n[2],color='yellow', arrow_length_ratio=0.2,label="Normal Vector")

ax.set_xlabel("X Axis")
ax.set_ylabel("Y Axis")
ax.set_zlabel("Z Axis")
ax.set_title("Plane")
ax.legend()
ax.grid(True)

plt.tight_layout()

#saving the figure in figs folder
fig.savefig(os.path.join(figs_folder,"plane.png"))

plt.show()
