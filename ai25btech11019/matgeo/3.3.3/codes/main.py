import matplotlib.pyplot as plt
import math

# Coordinates of vertices
A = (0, 0)
B = (5, 0)
C = (2.5, 5 * math.sqrt(3) / 2)  # (2.5, 4.33...)

# Create the figure
plt.figure(figsize=(5, 5))

# Draw the triangle
plt.plot([A[0], B[0], C[0], A[0]],
         [A[1], B[1], C[1], A[1]],
         'b-', linewidth=2)

# Mark vertices
plt.scatter(*A, color='red')
plt.scatter(*B, color='red')
plt.scatter(*C, color='red')

# Annotate vertices
plt.text(A[0]-0.3, A[1]-0.3, f'A{A}', fontsize=10)
plt.text(B[0]+0.1, B[1]-0.3, f'B{B}', fontsize=10)
plt.text(C[0]-0.5, C[1]+0.3, f'C({C[0]:.1f},{C[1]:.2f})', fontsize=10)

# Axes & grid
plt.axhline(0, color='black', linewidth=0.5)
plt.axvline(0, color='black', linewidth=0.5)
plt.xlim(-1, 6)
plt.ylim(-1, 6)
plt.gca().set_aspect('equal', adjustable='box')
plt.title('Equilateral Triangle ABC (side 5 cm)')
plt.grid(True)

plt.show()
