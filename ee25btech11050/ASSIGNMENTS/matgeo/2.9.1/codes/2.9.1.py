import ctypes
import numpy as np
import matplotlib.pyplot as plt

# Load the compiled shared C lib (use correct path if needed)
lib = ctypes.CDLL('./2.9.1.so')

# Set up output variables
outputs = (ctypes.c_double * 9)()
lib.solve_from_pdf(outputs)

# Extract variables (variable names as in C and PDF)
R = (outputs[0], outputs[1])
S = (outputs[2], outputs[3])
area = outputs[4]
diagonal = outputs[5]
C = (outputs[6], outputs[7])
K = outputs[8]

P = (-200, 0)
Q = (200, 0)
A = (200, 800)
O = (0, 0)

# --- Print for verification ---
print("Coordinates of R:", R)
print("Coordinates of S:", S)
print("Area of PQRS:", area)
print("Length of diagonal PR:", diagonal)
print("Coordinates of C:", C)
print("Value of K:", K)

# --- Plot as in the PDF ---
plt.figure(figsize=(9,9))
# Triangle AQC (A,Q,C)
triangle_x = [A[0], Q[0], C[0], A[0]]
triangle_y = [A[1], Q[1], C[1], A[1]]
plt.plot(triangle_x, triangle_y, 'k-', label='Triangle AQC', linewidth=2)

# Square PQRS
square_x = [P[0], Q[0], R[0], S[0], P[0]]
square_y = [P[1], Q[1], R[1], S[1], P[1]]
plt.plot(square_x, square_y, 'b-', label='Square PQRS', linewidth=2)

plt.scatter([O[0], P[0], Q[0], A[0], R[0], S[0], C[0]],
            [O[1], P[1], Q[1], A[1], R[1], S[1], C[1]], color='red')
for pt, name in zip([O, P, Q, A, R, S, C], ['O', 'P', 'Q', 'A', 'R', 'S', 'C']):
    plt.text(pt[0]+10, pt[1]+20, name, fontsize=13)

# Diagonal PR in square
plt.plot([P[0], R[0]], [P[1], R[1]], 'r--', label='Diagonal PR')

# Annotate area & diagonal
plt.text(-350, 200, f'Area = {area:.0f}', fontsize=13, color='blue', bbox=dict(facecolor='white', alpha=0.7))
plt.text(-350, 120, f'Diagonal = {diagonal:.1f}', fontsize=13, color='purple', bbox=dict(facecolor='white', alpha=0.7))

plt.xlabel('x')
plt.ylabel('y')
plt.xlim(-700, 300)
plt.ylim(-100, 900)
plt.grid(True)
plt.legend()
plt.title('Triangle AQC & Square PQRS')
plt.tight_layout()
plt.show()


