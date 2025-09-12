import numpy as np
import numpy.linalg as la
import matplotlib.pyplot as plt

# Solving eqns

# 9*a - 2 = (27*a + 1)/4 -> 1
# -1*b = 3 -> 2
coeff = np.array([[9-27/4, 0], [0, -1]])
rhs = np.array([2+1/4, 3])
soln = la.solve(coeff, rhs)
a = soln[0]
b = soln[1]

# Coordinates
A = (3*a + 1, -3)
B = (8*a, 5)
P = (9*a - 2, -b)

# Plotting points
plt.figure(figsize=(6,6))
plt.plot([A[0], B[0]], [A[1], B[1]], 'k--', label='Line AB')  # Line AB
plt.scatter(*A, color='blue', s=100, label='A (3a+1, -3)')
plt.scatter(*B, color='green', s=100, label='B (8a, 5)')
plt.scatter(*P, color='red', s=100, label='P (9a-2, -b)')

# Annotating points
plt.text(A[0]+0.2, A[1], 'A', fontsize=12)
plt.text(B[0]+0.2, B[1], 'B', fontsize=12)
plt.text(P[0]+0.2, P[1], 'P', fontsize=12)

# Axis labels and grid
plt.xlabel('x')
plt.ylabel('y')
plt.title('Plot of Points A, B and P dividing AB in 3:1')
plt.grid(True)
plt.legend()
plt.axis('equal')
plt.show()