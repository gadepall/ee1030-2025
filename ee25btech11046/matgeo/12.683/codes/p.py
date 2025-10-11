import numpy as np
import matplotlib.pyplot as plt

def calculate_unit_normal(point):
    normal_vector = 2 * np.array(point)
    magnitude = np.linalg.norm(normal_vector)
    unit_normal = normal_vector / magnitude
    return unit_normal

p = (4, 4, 4)

n = calculate_unit_normal(p)

radius = np.sqrt(48)
u, v = np.mgrid[0:2*np.pi:40j, 0:np.pi:20j]
x_sphere = radius * np.cos(u) * np.sin(v)
y_sphere = radius * np.sin(u) * np.sin(v)
z_sphere = radius * np.cos(v)

fig = plt.figure(figsize=(10, 10))
ax = fig.add_subplot(111, projection='3d')

ax.plot_surface(x_sphere, y_sphere, z_sphere, color='lightblue', alpha=0.6)
ax.scatter(*p, color='red', s=100, label='P (4,4,4)')
ax.text(*p, '   P (4, 4, 4)', color='r')
ax.quiver(0, 0, 0, *n, length=2, color='red', label=r'$\hat\vec{n}$')

axis_length = 16
ax.plot([-axis_length, axis_length], [0, 0], [0, 0], color='k')
ax.plot([0, 0], [-axis_length, axis_length], [0, 0], color='k')
ax.plot([0, 0], [0, 0], [-axis_length, axis_length], color='k')
ax.set_xlim(-16, 16)
ax.set_ylim(-16, 16)
ax.set_zlim(-16, 16)

ax.set_title('Unit Normal Vector to a Sphere')
ax.set_xlabel('$x$')
ax.set_ylabel('$y$')
ax.set_zlabel('$z$')
ax.view_init(9, -53)
ax.legend()
ax.set_box_aspect([1,1,1])
plt.savefig("../figs/plot_p.jpg")
plt.show()
