import numpy as np
import matplotlib.pyplot as plt

# Points of parallelogram ABCD
A = np.array([6, 1])
B = np.array([8, 2])
C = np.array([9, 4])
D = A + C - B  # parallelogram rule

# Function to generate points along a line segment
def line_points(P, Q, n=100):
    return np.array([np.linspace(P[0], Q[0], n), np.linspace(P[1], Q[1], n)])

# Line segments for sides
AB = line_points(A, B)
BC = line_points(B, C)
CD = line_points(C, D)
DA = line_points(D, A)

# Diagonals
AC = line_points(A, C)
BD = line_points(B, D)

# Plotting
plt.figure(figsize=(8, 8))

# Sides (slightly thinner gray lines)
plt.plot(AB[0], AB[1], color='gray', linewidth=1.5, label='AB')
plt.plot(BC[0], BC[1], color='gray', linewidth=1.5, label='BC')
plt.plot(CD[0], CD[1], color='gray', linewidth=1.5, label='CD')
plt.plot(DA[0], DA[1], color='gray', linewidth=1.5, label='DA')

# Diagonals (keep thickness similar to before)
plt.plot(AC[0], AC[1], 'r--', linewidth=2, label='AC')
plt.plot(BD[0], BD[1], 'b--', linewidth=2, label='BD')

# Points and labels with coordinates
points = [A, B, C, D]
labels = ['A', 'B', 'C', 'D']
colors = ['red', 'green', 'blue', 'orange']

for pt, lbl, clr in zip(points, labels, colors):
    plt.plot(pt[0], pt[1], 'o', color=clr, markersize=10)  # mark the point
    plt.text(pt[0]+0.2, pt[1]+0.2, f'{lbl}({pt[0]},{pt[1]})', fontsize=12, ha='center', color=clr)

# Settings
plt.xlabel('x')
plt.ylabel('y')
plt.title('Parallelogram ABCD with Diagonals')
plt.grid(True)
plt.legend()
plt.gca().set_aspect('equal', adjustable='box')

# Save and show
plt.savefig("Parallelogram_ABC.png", dpi=300, bbox_inches='tight')
plt.show()
