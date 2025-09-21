import numpy as np
import matplotlib.pyplot as plt


a = np.array([2, 2, -5])
b = np.array([2, 1, 3])


c = a + b


c_norm = np.linalg.norm(c)
unit_c = c / c_norm

print("Vector a:", a)
print("Vector b:", b)
print("a + b:", c)
print("Unit vector in direction of (a+b):", unit_c)


fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')


origin = np.zeros(3)


ax.quiver(*origin, *a, color='r', label='a', arrow_length_ratio=0.1)
ax.quiver(*origin, *b, color='g', label='b', arrow_length_ratio=0.1)
ax.quiver(*origin, *c, color='b', label='a+b', arrow_length_ratio=0.1)
ax.quiver(*origin, *unit_c, color='m', label='Unit vector of (a+b)', arrow_length_ratio=0.2)


ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Z')
ax.set_title('Vectors a, b, a+b, and unit vector of (a+b)')
ax.legend()


ax.set_box_aspect([1,1,1])
plt.savefig("../figs/plot2.png")
plt.show()

