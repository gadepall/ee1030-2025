import numpy as np
import matplotlib.pyplot as plt

# Define points
A = np.array([-4.0, 0.0])
B = np.array([4.0, 0.0])
C = np.array([0.0, 3.0])

# Plot the triangle in red
points = np.array([A, B, C, A])
plt.plot(points[:,0], points[:,1], 'r--o')
plt.text(A[0], A[1], "A")
plt.text(B[0], B[1], "B")
plt.text(C[0], C[1], "C")
plt.axis("equal")
plt.grid(True)
plt.show()

