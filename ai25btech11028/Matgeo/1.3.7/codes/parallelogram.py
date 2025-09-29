import numpy as np
import matplotlib.pyplot as plt

# Given vertices
B = np.array([0, 0])
C = np.array([3, 0])
D = np.array([0, 4])

# Compute A = B + D - C
A = B + D - C
print("Coordinates of A:", A)

 # Plot parallelogram
x_points = [A[0], B[0], C[0], D[0], A[0]]
y_points = [A[1], B[1], C[1], D[1], A[1]]

plt.plot(x_points, y_points, 'b-')
plt.scatter([A[0], B[0], C[0], D[0]], [A[1], B[1], C[1], D[1]], color='r')

 plt.text(A[0]-0.3, A[1]+0.2, 'A(-3,4)')
plt.text(B[0]-0.3, B[1]-0.3, 'B(0,0)')
plt.text(C[0]+0.2, C[1]-0.3, 'C(3,0)')
plt.text(D[0]-0.3, D[1]+0.3, 'D(0,4)')

plt.axis('equal')
plt.grid(True)
# Save before show
plt.savefig("/storage/emulated/0/matrix/Matgeo/1.3.7/figs/Figure_1.png", dpi=300, bbox_inches='tight')
plt.show()