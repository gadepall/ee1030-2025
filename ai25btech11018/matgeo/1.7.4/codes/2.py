import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import numpy as np

# Points
A = np.array([2, -1, 3])
B = np.array([3, -5, 1])
C = np.array([-1, 11, 9])

# Check collinearity (print for reference)
AB = B - A
AC = C - A

print("Vector AB:", AB)
print("Vector AC:", AC)



# Verify if AC is a scalar multiple of AB
if np.allclose(AC, (AC[0]/AB[0]) * AB):
    print("Points are collinear")
else:
    print("Points are not collinear")

# 3D Plot
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

# Plot points
ax.scatter(*A, color='red', label='A(2, -1, 3)')
ax.scatter(*B, color='green', label='B(3, -5, 1)')
ax.scatter(*C, color='blue', label='C(-1, 11, 9)')

# Plot line through A in direction of AB (which also passes through B and C)


t = np.linspace(-2, 2, 100)
line = A[:, None] + np.outer(AB, t)

ax.plot(line[0], line[1], line[2], 'k--', label='Line through A, B, and C')

# Labels and legend
ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Z')
ax.legend()
ax.set_title('Collinear Points in 3D')

# Save figure as PNG
plt.savefig("collinear_points.png")

# Show plot
plt.show()
