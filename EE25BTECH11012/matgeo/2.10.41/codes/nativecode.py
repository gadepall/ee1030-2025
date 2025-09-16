import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

#Example vectors that satisfy (a×b)×(c×d)=0
a = np.array([1, 0, 0])
b = np.array([0, 1, 0])
c = np.array([2, 0, 0])
d = np.array([0, 2, 0])
#Normals of planes A and B
n1 = np.cross(a, b)
n2 = np.cross(c, d)
print("n1:", n1, " n2:", n2)          # normals
print("Cross of normals:", np.cross(n1, n2))  # should be zero
#Mesh grid for plotting
xx, yy = np.meshgrid(np.linspace(-2, 2, 20), np.linspace(-2, 2, 20))
def plane_z(normal, X, Y):
# n·(x,y,z) = 0  => z = (-n_x X - n_y Y)/n_z  if n_z != 0
return (-normal[0]*X - normal[1]*Y)/normal[2] if normal[2] != 0 else np.zeros_like(X)
z1 = plane_z(n1, xx, yy)
z2 = plane_z(n2, xx, yy)
fig = plt.figure(figsize=(9,7))
ax = fig.add_subplot(111, projection='3d')
#Plot planes

surf1 = ax.plot_surface(xx, yy, z1, color='cyan', alpha=0.5)
surf2 = ax.plot_surface(xx, yy, z2 + 0.1, color='magenta', alpha=0.5)  # small offset for visibility

#Mark plane names

ax.text(0, 0, 0.05, "Plane A", color='blue', fontsize=12, ha='center')
ax.text(0, 0, 0.15, "Plane B", color='purple', fontsize=12, ha='center')

#Plot and label normals

origin = np.array([0, 0, 0])
ax.quiver(*origin, *n1, color='blue', length=1.0, arrow_length_ratio=0.1)
ax.quiver(*origin, *n2, color='red',  length=1.0, arrow_length_ratio=0.1)

#Add text at the arrow tips for normals

ax.text((n11.1), "n₁", color='blue', fontsize=12)
ax.text((n21.1), "n₂", color='red',  fontsize=12)

ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Z')
ax.set_title('Planes A & B with Normals Marked')

#Make the axes equal for a better view

ax.set_box_aspect([1,1,0.5])
plt.show()