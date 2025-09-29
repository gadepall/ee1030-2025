import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# Given points
A = np.array([3, 6, 9])
B = np.array([10, 20, 30])
C = np.array([24, -41, 5])

# Compute dot products directly
dot1 = np.dot(B-A, C-A)
dot2 = np.dot(B-A, C-B)
dot3 = np.dot(C-A, C-B)

# Check for right-angled triangle
if dot1 == 0 or dot2 == 0 or dot3 == 0:
    print("The points form a right-angled triangle.")
else:
    print("The points do NOT form a right-angled triangle.")

# Plotting the triangle
fig = plt.figure(figsize=(8,6))
ax = fig.add_subplot(111, projection='3d')

# Points
ax.scatter(*A, color='black', s=80)
ax.text(A[0]+0.5, A[1]+0.5, A[2]+0.5, "A(3,6,9)", fontsize=12)

ax.scatter(*B, color='blue', s=80)
ax.text(B[0]+0.5, B[1]+0.5, B[2]+0.5, "B(10,20,30)", fontsize=12, color='blue')

ax.scatter(*C, color='red', s=80)
ax.text(C[0]+0.5, C[1]+0.5, C[2]+0.5, "C(24,-41,5)", fontsize=12, color='red')

# Lines connecting points
ax.plot([A[0], B[0]], [A[1], B[1]], [A[2], B[2]], color='blue', linewidth=2, label="Line AB")
ax.plot([A[0], C[0]], [A[1], C[1]], [A[2], C[2]], color='green', linewidth=2, label="Line AC")
ax.plot([B[0], C[0]], [B[1], C[1]], [B[2], C[2]], color='red', linewidth=2, linestyle='--', label="Line BC")

# Labels and title
ax.set_xlabel("X-axis")
ax.set_ylabel("Y-axis")
ax.set_zlabel("Z-axis")
ax.set_title("Triangle formed by points A, B, C in 3D")
ax.legend()
plt.show()
