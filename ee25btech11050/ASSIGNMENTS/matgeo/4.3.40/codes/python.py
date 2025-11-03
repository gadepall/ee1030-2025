import numpy as np
import matplotlib.pyplot as plt

# Given vectors
a = np.array([2, -1, 4])      # point vector
d = np.array([1, 2, -1])      # direction vector

# Parameter lambda values
lambdas = np.linspace(-10, 10, 400)

# Calculate points on the line for each lambda
points = np.array([a + l * d for l in lambdas])

# Plotting the line in 3D
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

ax.plot(points[:, 0], points[:, 1], points[:, 2], label='Line: r = a + λd', color='blue')

# Plot the given point 'a'
ax.scatter(a[0], a[1], a[2], color='red', label='Point a (2, -1, 4)')

ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Z')
ax.legend()
plt.title('3D Line plot')
plt.show()

