import numpy as np
import matplotlib.pyplot as plt
from call import get_points_and_line

# Extract from .so file
A, B, n, k = get_points_and_line()

# Direction vector of the line (B - A)
d = B - A

# Parameter range for the line
t_vals = np.linspace(-1, 2, 100)
line_points = np.array([A + t * d for t in t_vals])

# Plot
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

# Plot the two points
ax.scatter(A[0], A[1], A[2], color='red', label='A (3,4,-7)', s=50)
ax.scatter(B[0], B[1], B[2], color='green', label='B (1,-1,6)', s=50)

# Plot the line passing through A and B
ax.plot(line_points[:,0], line_points[:,1], line_points[:,2], color='blue', label='Line through A and B')

ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Z')
ax.legend()
ax.set_title("Line Through 3D Points A and B")
plt.tight_layout()
plt.show()

