import ctypes
import sys
import os
import numpy as np 
import matplotlib.pyplot as plt 

#save the figure in figs folder 
figs_folder = os.path.join("..","figs")

#loading the shared object 
lib = ctypes.CDLL("./points.so") 

#return type and argument type 
lib.inverse_solve.restype = ctypes.POINTER(ctypes.c_double)
lib.inverse_solve.argtypes = [ctypes.c_int,(ctypes.c_double*3)*3,ctypes.POINTER(ctypes.c_double)]

#defining A matrix 
A = ((ctypes.c_double*3)*3)()  #we can  use it as an object because of ()

A[0][:] = [1.0,1.0,1.0]
A[1][:] = [0.0,1.0,3.0]
A[2][:] = [1.0,-2.0,1.0]

#b matrix 
b = (ctypes.c_double*3)(6.0,11.0,0.0)

sol = lib.inverse_solve(3,A,b) 

solution = [sol[i] for i in range(3)]
x,y,z = solution 
print("Solution from c :",solution) 

#creating mesh grid 
x_vals = np.linspace(-10,10,100)
y_vals = np.linspace(-10,10,100) 
X , Y = np.meshgrid(x_vals,y_vals) 

#Plane equation 
Z1 = 6.0 - X - Y 
Z2 = (11.0 - Y)/(3.0) 
Z3 = - X + (2.0)*Y 

#Plotting 
fig = plt.figure(figsize=(10,8))
ax = fig.add_subplot(111,projection="3d")

#Planes 
ax.plot_surface(X,Y,Z1,alpha = 0.5,color="red")
ax.plot_surface(X,Y,Z2,alpha = 0.5,color="blue")
ax.plot_surface(X,Y,Z3,alpha = 0.5,color="green")

#Plot the solution point 
ax.scatter(x,y,z,color="black",label="P(1.0,2.0,3.0)")
ax.text(x+0.5,y+0.5,z+0.5,f"P({x:.2f},{y:.2f},{z:.2f})",fontsize=10,color="black")

#Axes 
ax.set_xlabel("X Axes")
ax.set_ylabel("Y Axes")
ax.set_zlabel("Z Axes")
ax.set_title("Intersection of Three Planes and Solution Point P")
ax.legend()
ax.grid(True)

#savefigure 
plt.tight_layout()
fig.savefig(os.path.join(figs_folder,"solution.png"))
plt.show()


