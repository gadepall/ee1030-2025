import os
import numpy as np 
import matplotlib.pyplot as plt 

#to save the figure in figs folder
figs_folder = os.path.join("..","figs")

#normal vector and c 
n = np.array([2,1,-1])
c = 5.0

#x intercept
x_intercept = c/n[0]

#writing the x_intercept as a numpy array 
point = np.array([x_intercept,0,0])

#creating a meshgrid for the plane
x = np.linspace(-10,10,100)
y = np.linspace(-10,10,100)

x,y = np.meshgrid(x,y)

#plane equation
z = (c - n[0]*x - n[1]*y)/n[2]

#plotting
fig=plt.figure(figsize=(8,6))
ax = fig.add_subplot(111,projection="3d")
ax.set_box_aspect([1,1,1])  # Fix aspect ratio : to enforce equal scaling across axes so that xintercept lies on x axis.

#plane
ax.plot_surface(x,y,z,alpha=0.5,color='blue',edgecolor='none')

#intercept point
ax.scatter(*point,color='red',s=2,label=f"P({x_intercept},0,0)")

#axes labels 
ax.set_xlabel("X Axis")
ax.set_ylabel("Y Axis")
ax.set_zlabel("Z Axis")
ax.set_title("Plane and X-intercept")

ax.legend()
ax.grid(True)

plt.tight_layout()
fig.savefig(os.path.join(figs_folder,"intercept.png"))
plt.show()

