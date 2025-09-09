import matplotlib.pyplot as plt
import numpy as np
from fractions import Fraction

# Define points
A = np.array([4, 0], dtype=float)
B = np.array([-4, 0], dtype=float)
C = np.array([0, 3], dtype=float)

# Helpers
def midpoint(P, Q):
    return (P + Q) / 2.0

def fmt_fraction(P):
    # Convert coordinates into fractions nicely
    x, y = Fraction(P[0]).limit_denominator(), Fraction(P[1]).limit_denominator()
    return f"({x}, {y})"

# Midpoints
M_AB = midpoint(A, B)  # Opposite of C
M_BC = midpoint(B, C)  # Opposite of A
M_CA = midpoint(C, A)  # Opposite of B

# Triangle path
x_vals = [A[0], B[0], C[0], A[0]]
y_vals = [A[1], B[1], C[1], A[1]]

plt.figure(figsize=(6, 6))

# Triangle edges
plt.plot(x_vals, y_vals, 'k-', linewidth=2, label="Triangle")

# Vertices
plt.plot(A[0], A[1], 'ro'); plt.text(A[0]+0.2, A[1]-0.3, "A (4, 0)", color='red')
plt.plot(B[0], B[1], 'go'); plt.text(B[0]-2.0, B[1]-0.3, "B (-4, 0)", color='green')
plt.plot(C[0], C[1], 'bo'); plt.text(C[0]-0.8, C[1]+0.2, "C (0, 3)", color='blue')

# === Medians with same-color midpoints ===
# Median from A to M_BC
plt.plot([A[0], M_BC[0]], [A[1], M_BC[1]], 'r--', label="Median from A")
plt.plot(M_BC[0], M_BC[1], 'rs', markersize=8)
plt.text(M_BC[0]+0.15, M_BC[1]-0.25, f"M_BC {fmt_fraction(M_BC)}", color='red')

# Median from B to M_CA
plt.plot([B[0], M_CA[0]], [B[1], M_CA[1]], 'g--', label="Median from B")
plt.plot(M_CA[0], M_CA[1], 'gs', markersize=8)
plt.text(M_CA[0]+0.15, M_CA[1]-0.25, f"M_CA {fmt_fraction(M_CA)}", color='green')

# Median from C to M_AB
plt.plot([C[0], M_AB[0]], [C[1], M_AB[1]], 'b--', label="Median from C")
plt.plot(M_AB[0], M_AB[1], 'bs', markersize=8)
plt.text(M_AB[0]+0.15, M_AB[1]-0.25, f"M_AB {fmt_fraction(M_AB)}", color='blue')

# Axis/legend
plt.axis('equal')
plt.grid(True)
plt.title("Triangle ABC with Medians (Midpoints in Fractions)")
plt.xlabel("X"); plt.ylabel("Y")
plt.legend()

plt.savefig("fig_3.png", dpi=150, bbox_inches='tight')
plt.show()
