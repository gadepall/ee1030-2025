import ctypes
import sys
import os
import numpy as np 
import matplotlib.pyplot as plt 

# for saving figure in figs folder
figs_folder = os.path.join("..","figs")

# loading the shared object
lib = ctypes.CDLL("./points.so")

# defining the return type and arg type 
lib.gaussian_elimination.restype = ctypes.POINTER(ctypes.c_double)
lib.gaussian_elimination.argtypes = [((ctypes.c_double*4)*3)]

# defining the augmented matrix 
aug_matrix = ((ctypes.c_double*4)*3)()
aug_matrix[0][:] = [1,1,1,6]
aug_matrix[1][:] = [1,4,6,20]
aug_matrix[2][:] = [1,4,6,21]

# calling the c function 
sol = lib.gaussian_elimination(aug_matrix)
solution = [sol[i] for i in range(3)]
x,y,z = solution
print("Solution from C:",solution)

# create meshgrid for plotting planes
x_vals = np.linspace(-10,10,100)
y_vals = np.linspace(-10,10,100)
X , Y = np.meshgrid(x_vals,y_vals)

# Plane 1 
Z1 = 6 - X - Y 

# Plane 2
Z2 = (20 - X - 4*Y)/6

# Plane 3 
Z3 = (21 - X - 4*Y)/6

# Plotting 
fig = plt.figure(figsize=(10,8))
ax = fig.add_subplot(111,projection="3d")

# Plot the planes 
ax.plot_surface(X,Y,Z1,alpha=0.5,color="red",label="Plane 1")
ax.plot_surface(X,Y,Z2,alpha=0.5,color="green",label="Plane 2")

# Plot Plane 3 as wireframe so it's visible separately
ax.plot_wireframe(X,Y,Z3,color="blue",alpha=0.7,label="Plane 3")

# Plot the solution point only if valid (not all zeros or unchanged)
if not all(abs(val) < 1e-9 for val in solution):  
    ax.scatter(x,y,z,color="black")
    ax.text(x+0.5,y+0.5,z+0.5,f"P({x:.2f},{y:.2f},{z:.2f})",fontsize=10,color="black")

# Axes 
ax.set_xlabel("X Axis")
ax.set_ylabel("Y Axis")
ax.set_zlabel("Z Axis")
ax.set_title(r"No solution for $\lambda = 6$ and $\mu \neq 20$")  # latex title

ax.grid(True)

# savefigure 
plt.tight_layout()
fig.savefig(os.path.join(figs_folder,"planes.png"))
plt.show()

