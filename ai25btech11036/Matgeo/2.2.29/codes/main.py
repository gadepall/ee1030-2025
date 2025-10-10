import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# Define points in 3D (z=0 plane)
A = (0, 4, 0)
B = (0, 0, 0)
C = (3, 0, 0)

# Create 3D figure
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

# Plot points
ax.scatter(*A, color="red", s=50, label="A(0,4,0)")
ax.scatter(*B, color="blue", s=50, label="B(0,0,0)")
ax.scatter(*C, color="green", s=50, label="C(3,0,0)")

# Draw triangle edges
ax.plot([A[0], B[0]], [A[1], B[1]], [A[2], B[2]], 'k-')
ax.plot([B[0], C[0]], [B[1], C[1]], [B[2], C[2]], 'k-')
ax.plot([C[0], A[0]], [C[1], A[1]], [C[2], A[2]], 'k-')

# Labels
ax.text(*A, "A(0,4)", color="red")
ax.text(*B, "B(0,0)", color="blue")
ax.text(*C, "C(3,0)", color="green")

# Set axes labels
ax.set_xlabel("X-axis")
ax.set_ylabel("Y-axis")
ax.set_zlabel("Z-axis")

# Adjust view
ax.view_init(elev=20, azim=30)
plt.title("3D Representation of Triangle ABC (z=0 plane)")
plt.legend()
plt.show()
