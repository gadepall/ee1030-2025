import numpy as np
import matplotlib.pyplot as plt

# --- Given vertices
A = np.array([0.0, 0.0])
B = np.array([4.0, 0.0])
C = np.array([4.0, 3.0])
D = np.array([0.0, 3.0])

k = 4.0 / 3.0  # scale factor

# --- Compute C' and D' (scaled triangle BDC)
Dp = B + k * (D - B)   # D'
Cp = B + k * (C - B)   # C'

# --- A' must be such that A'BC'D' is a parallelogram
# In a parallelogram: A' = B + D' - C'
Ap = B + Dp - Cp

# --- Collect points
points = {"A":A, "B":B, "C":C, "D":D, "D'":Dp, "C'":Cp, "A'":Ap}

# --- Print coordinates
print("Corrected coordinates:")
for name, p in points.items():
    print(f"{name:3} = ({p[0]:.6f}, {p[1]:.6f})")

# --- Plotting
plt.figure(figsize=(8,6))

# Original quadrilateral ABCD
plt.plot([A[0],B[0],C[0],D[0],A[0]], [A[1],B[1],C[1],D[1],A[1]], 
         'b-', linewidth=1.5, label="ABCD")

# Triangle B-D'-C'
plt.plot([B[0],Dp[0],Cp[0],B[0]], [B[1],Dp[1],Cp[1],B[1]], 
         'r--', linewidth=1.5, label="Δ B D' C'")

# Parallelogram A'-B-C'-D'
plt.plot([Ap[0],B[0],Cp[0],Dp[0],Ap[0]], [Ap[1],B[1],Cp[1],Dp[1],Ap[1]], 
         'g-o', linewidth=2, label="Parallelogram A' B C' D'")

# Labels
for name, p in points.items():
    plt.scatter(p[0], p[1], s=60, zorder=5)
    plt.text(p[0]+0.1, p[1]+0.1, f"{name} ({p[0]:.2f},{p[1]:.2f})", fontsize=9)

plt.gca().set_aspect('equal', adjustable='box')
plt.grid(True)
plt.legend()
plt.title("Parallelogram A' B C' D' with scaled triangle BD'C'")
plt.show()



