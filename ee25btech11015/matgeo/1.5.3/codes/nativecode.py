import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# Define points in 3D (z=0 since they are in XY plane)
A = (3, 6, 0)
B = (-12, -3, 0)
X = (-7, 0, 0)

# Create a 3D plot
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

# Plot line AB
ax.plot([A[0], B[0]], [A[1], B[1]], [A[2], B[2]], 
        label='Line AB', color='black', linestyle='--')

# Plot points
ax.scatter(*A, color='red', s=50, label='A(3,6,0)')
ax.scatter(*B, color='blue', s=50, label='B(-12,-3,0)')
ax.scatter(*X, color='green', s=50, label='X(-7,0,0)')

# Annotate points
ax.text(A[0], A[1], A[2]+0.5, 'A(3,6,0)', color='red')
ax.text(B[0], B[1], B[2]+0.5, 'B(-12,-3,0)', color='blue')
ax.text(X[0], X[1], X[2]+0.5, 'X(-7,0,0)', color='green')

# Labels
ax.set_xlabel('X-axis')
ax.set_ylabel('Y-axis')
ax.set_zlabel('Z-axis')
ax.set_title('3D Plot of Line Segment AB and Point X')

# Equal aspect ratio
ax.set_box_aspect([1,1,0.5])  

# Show grid and legend
ax.legend()
ax.grid(True)

plt.show()

