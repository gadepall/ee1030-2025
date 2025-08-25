import numpy as np
import matplotlib as mp
mp.use("TkAgg")  # must come before pyplot
import matplotlib.pyplot as plt

# Define vectors
A = np.array([2, 3, -4], dtype=np.int32)
B = np.array([3, -4, -5], dtype=np.int32)
C = np.array([3, 2, -3], dtype=np.int32)

# Sum of vectors
S = A + B + C
print("Sum of vectors:", S)

# Magnitude of sum vector
magnitude = np.linalg.norm(S)
print("Magnitude of sum vector: {:.3f}".format(magnitude))

# 3D Plot
origin = np.array([0, 0, 0])
fig = plt.figure(figsize=(8, 8))
ax = fig.add_subplot(111, projection='3d')

ax.quiver(*origin, *A, color='r', label='A')
ax.quiver(*origin, *B, color='g', label='B')
ax.quiver(*origin, *C, color='b', label='C')
ax.quiver(*origin, *S, color='k', linewidth=2, label='Sum (A+B+C)')

# Axis limits
max_val = max(np.abs(S)) + 2
ax.set_xlim([0, max_val])
ax.set_ylim([0, max_val])
ax.set_zlim([min(0, np.min(S)) - 2, max_val])

# Labels and title
ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Z')
ax.set_title('3D Vectors and their Sum')
ax.legend()

# Save and show
plt.savefig("/home/user/Matrix/Matgeo_assignments/1.9.15/figs/Figure_1.png",
            dpi=300, bbox_inches='tight')
plt.show()

