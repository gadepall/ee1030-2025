import numpy as np
import matplotlib.pyplot as plt

# Given points
A = np.array([-2, 4, -5])
B = np.array([1, 2, 3])

# Direction ratios
AB = B - A
print("Direction ratios:", AB)

# Direction cosines
magnitude = np.linalg.norm(AB)
direction_cosines = AB / magnitude
print("Direction cosines:", direction_cosines)

# Plotting
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

# Plot points A and B
ax.scatter(*A, color='red', label='A(-2,4,-5)')
ax.scatter(*B, color='blue', label='B(1,2,3)')

# Plot line passing through A and B
t = np.linspace(-1, 2, 100)  # parameter for line
line = A.reshape(3,1) + np.outer(AB, t)
ax.plot(line[0], line[1], line[2], color='green', label='Line AB')

# Labels
ax.set_xlabel('X-axis')
ax.set_ylabel('Y-axis')
ax.set_zlabel('Z-axis')
ax.legend()
ax.set_title("Line passing through A and B with direction cosines")

plt.savefig("../figs/fig_vector.png")

plt.show()

