import numpy as np
import matplotlib.pyplot as plt
import os

#for generating figure in figs folder
figs_folder= os.path.join("..","figs")

#normal vector (same as returned by C code)
n = np.array([1,2,-3])
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

