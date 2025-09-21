import ctypes
import sys
import os
import numpy as np 
import matplotlib.pyplot as plt 

#for saving figure in figs folder
figs_folder = os.path.join("..","figs")

#loading the shared object
lib = ctypes.CDLL("./points.so")

#defining the return type and arg type 
lib.gaussian_elimination.restype = ctypes.POINTER(ctypes.c_double)
lib.gaussian_elimination.argtypes = [((ctypes.c_double*4)*3)]

#defining the augmented matrix 
aug_matrix = ((ctypes.c_double*4)*3)()
aug_matrix[0][:] = [1,-1,1,4]
aug_matrix[1][:] = [2,1,-3,0]
aug_matrix[2][:] = [1,1,1,2]

#calling the c function 
sol = lib.gaussian_elimination(aug_matrix)
solution = [sol[i] for i in range(3)]
x,y,z = solution
print("Solution from C:",solution)

#create meshgrid for plotting planes
x_vals = np.linspace(-10,10,100)
y_vals = np.linspace(-10,10,100)
X , Y = np.meshgrid(x_vals,y_vals)

#Plane 1 
Z1 = 4 - X + Y 

#Plane 2
Z2 = (2*X + Y)/3

#Plane 3 
Z3 = 2 - X - Y 

#Plotting 
fig = plt.figure(figsize=(10,8))

ax = fig.add_subplot(111,projection="3d")

#Plot the planes 
ax.plot_surface(X,Y,Z1,alpha=0.5,color = "red",label="Plane 1")
ax.plot_surface(X,Y,Z2,alpha=0.5,color = "green",label="Plane 2")
ax.plot_surface(X,Y,Z3,alpha=0.5,color = "blue",label="Plane 3")

#Plot the solution point 
ax.scatter(x,y,z,color="black")
ax.text(x+0.5,y+0.5,z+0.5,f"P({x:.2f},{y:.2f},{z:.2f})",fontsize=10,color="black")

#Axes 
ax.set_xlabel("X Axes")
ax.set_ylabel("Y Axes")
ax.set_zlabel("Z Axes")
ax.set_title("Intersection of Three Planes and Solution Point P")

ax.grid(True)

#savefigure 
plt.tight_layout()
fig.savefig(os.path.join(figs_folder,"solution.png"))
plt.show()




