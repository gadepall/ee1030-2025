import numpy as np
import matplotlib.pyplot as plt

# Function to find line coefficients Ax + By = C given two points
def line_coeffs(p1, p2):
    A = p2[1] - p1[1]
    B = p1[0] - p2[0]
    C = A*p1[0] + B*p1[1]
    return A, B, C

# Function to find intersection of two lines (given in Ax+By=C form)
def intersection(L1, L2):
    A1, B1, C1 = L1
    A2, B2, C2 = L2
    det = A1*B2 - A2*B1
    if det == 0:
        raise ValueError("Lines are parallel, no intersection.")
    x = (C1*B2 - C2*B1) / det
    y = (A1*C2 - A2*C1) / det
    return np.array([x, y])

# Define triangle vertices
A = np.array([1, 1])
B = np.array([5, 1])
C = np.array([3, 4])

# Slopes of sides
L_BC = line_coeffs(B, C)
L_AC = line_coeffs(A, C)

# Altitude from A (perpendicular to BC, passes through A)
A1, B1, _ = L_BC
L_alt_A = (-B1, A1, -B1*A[0] + A1*A[1])

# Altitude from B (perpendicular to AC, passes through B)
A2, B2, _ = L_AC
L_alt_B = (-B2, A2, -B2*B[0] + A2*B[1])

# Orthocenter (D)
D = intersection(L_alt_A, L_alt_B)

# Plotting
plt.figure(figsize=(6,6))
# Triangle
plt.plot([A[0],B[0]],[A[1],B[1]],'b')
plt.plot([B[0],C[0]],[B[1],C[1]],'b')
plt.plot([C[0],A[0]],[C[1],A[1]],'b')

# Lines showing perpendicularity
plt.plot([A[0], D[0]], [A[1], D[1]], 'g--', label="AD")
plt.plot([B[0], C[0]], [B[1], C[1]], 'r--', label="BC")
plt.plot([B[0], D[0]], [B[1], D[1]], 'g--', label="BD")
plt.plot([A[0], C[0]], [A[1], C[1]], 'r--', label="AC")

# Points
plt.scatter(*A, color='red')
plt.scatter(*B, color='red')
plt.scatter(*C, color='red')
plt.scatter(*D, color='purple')

# Labels
plt.text(A[0]+0.1, A[1], 'A')
plt.text(B[0]+0.1, B[1], 'B')
plt.text(C[0]+0.1, C[1], 'C')
plt.text(D[0]+0.1, D[1], 'D (Orthocenter)')

plt.legend()
plt.gca().set_aspect('equal', adjustable='box')
plt.grid(True)
plt.savefig("/sdcard/Matrix/ee1030-2025/ai25btech11016/Matgeo/2.10.5/figs/2.10.5.png")
plt.show()