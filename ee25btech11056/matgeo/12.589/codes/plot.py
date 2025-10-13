import os
import numpy as np 
import matplotlib.pyplot as plt 

# for saving figure in figs folder
figs_folder = os.path.join("..","figs")

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

