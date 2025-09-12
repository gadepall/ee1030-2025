import numpy as np
import matplotlib.pyplot as plt

# Given points A and B
A = np.array([3, 4, 5])
B = np.array([-1, 3, -7])
K = 20  # Adjustable constant

# Create a grid of points
x = np.linspace(-10, 10, 40)
y = np.linspace(-10, 10, 40)
z = np.linspace(-10, 10, 40)
X, Y, Z = np.meshgrid(x, y, z)

# Squared distances
dist_A2 = (X - A[0])**2 + (Y - A[1])**2 + (Z - A[2])**2
dist_B2 = (X - B[0])**2 + (Y - B[1])**2 + (Z - B[2])**2

# Where the sum of squares is close to K^2
values = dist_A2 + dist_B2
tolerance = 5
mask = np.abs(values - K**2) < tolerance

# Plot
fig = plt.figure(figsize=(8,6))
ax = fig.add_subplot(111, projection='3d')
ax.scatter(X[mask], Y[mask], Z[mask], color='blue', s=1)

ax.set_xlabel('X axis')
ax.set_ylabel('Y axis')
ax.set_zlabel('Z axis')
ax.set_title('Points satisfying $PA^2 + PB^2 = 20^2$')

plt.tight_layout()
plt.show()

