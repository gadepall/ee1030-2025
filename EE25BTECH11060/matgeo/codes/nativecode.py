 
# Plotting points A(1, -2, -8), B(5, 0, -2), and C(11, 3, 7)
 
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# Define the points as numpy arrays
A = np.array([1, -2, -8])
B = np.array([5, 0, -2])
C = np.array([11, 3, 7])

# Create a 3D plot
fig = plt.figure(figsize=(8, 6))
ax = fig.add_subplot(111, projection='3d')

# Plot the points
ax.scatter(*A, color='red', s=100, label='A(1, -2, -8)')
ax.scatter(*B, color='green', s=100, label='B(5, 0, -2)')
ax.scatter(*C, color='blue', s=100, label='C(11, 3, 7)')

# Plot line AC
ax.plot([A[0], C[0]], [A[1], C[1]], [A[2], C[2]], color='purple', label='Line AC')

# Annotate points
ax.text(*A, ' A', color='red', fontsize=10)
ax.text(*B, ' B', color='green', fontsize=10)
ax.text(*C, ' C', color='blue', fontsize=10)

# Set axes labels
ax.set_xlabel('X-axis')
ax.set_ylabel('Y-axis')
ax.set_zlabel('Z-axis')
ax.set_title('3D Plot of Points A, B, C and Line AC')
ax.legend()
ax.grid(True)

# Show the plot
plt.show()
