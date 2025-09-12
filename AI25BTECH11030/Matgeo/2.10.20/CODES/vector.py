import matplotlib.pyplot as plt
import numpy as np

# Vectors u, v, w in 2D (using first two components)
u = np.array([2, 3])
v = np.array([4, 1])
w = np.array([0, 5])

# Origin point
origin = np.array([0, 0])

# Plotting the vectors
plt.figure(figsize=(7, 7))
plt.quiver(*origin, *u, angles='xy', scale_units='xy', scale=1, color='red', label='u = [2, 3]')
plt.quiver(*origin, *v, angles='xy', scale_units='xy', scale=1, color='green', label='v = [4, 1]')
plt.quiver(*origin, *w, angles='xy', scale_units='xy', scale=1, color='blue', label='w = [0, 5]')

# Setting the limits
plt.xlim(-1, 5)
plt.ylim(-1, 6)

# Adding labels and title
plt.xlabel('X')
plt.ylabel('Y')
plt.title('2D vectors: u, v, w')
plt.grid()
plt.legend()
plt.gca().set_aspect('equal')

# Save the figure as a PNG file
plt.savefig('2D_vectors.png')
plt.close()

