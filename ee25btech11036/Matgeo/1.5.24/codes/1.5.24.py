import numpy as np
import matplotlib.pyplot as plt

print("Problem 1.5.24:")
print("A line intersects the Y-axis and X-axis at P=(0,b) and Q=(c,0).")
print("If (2,-5) is the midpoint of PQ, find P and Q.\n")

# --- Step 1: Rank condition using matrix ---
print("Step 1: Rank condition (collinearity)")
P = np.array([0, 'b'], dtype=object)   # keep symbolic b
Q = np.array(['c', 0], dtype=object)   # keep symbolic c
M = np.array([2, -5])

print("Matrix formed from (P-M) and (Q-M):")
print("[[-2, c-2], [b+5, 5]]")

print("Perform row operation: R2 -> -2*R2 - (b+5)*R1")
print("=> [[-2, c-2], [0, -10 - (b+5)(c-2)]]")

print("For rank=1, last entry must vanish:")
print("(b+5)(c-2) = -10   (relation 1)\n")

# --- Step 2: Midpoint condition ---
print("Step 2: Midpoint condition")
Mx, My = 2, -5
print(f"Midpoint M = ((0+c)/2, (b+0)/2) = ({Mx}, {My})")

# Solve midpoint equations
c = 2 * Mx
b = 2 * My
print(f"From midpoint: c = {c}, b = {b} (relation 2)\n")

# --- Step 3: Solve ---
P = np.array([0, b])
Q = np.array([c, 0])
print("Step 3: Final Solution")
print(f"P = {tuple(P)}")
print(f"Q = {tuple(Q)}\n")

# --- Step 4: Verification ---
midpoint = (P + Q) / 2
print("Verification:")
print(f"Midpoint of P and Q = {tuple(midpoint)}")

# --- Step 5: Plot the graph ---
plt.figure(figsize=(6,6))
plt.axhline(0, color='black', linewidth=0.8)  # X-axis
plt.axvline(0, color='black', linewidth=0.8)  # Y-axis

# Plot line PQ
plt.plot([P[0], Q[0]], [P[1], Q[1]], 'b-', label="Line PQ")

# Mark points
plt.scatter(*P, color='red')
plt.scatter(*Q, color='green')
plt.scatter(*M, color='purple')

# Add labels
plt.text(P[0]-0.5, P[1], f"P({int(P[0])},{int(P[1])})", fontsize=10, color="red")
plt.text(Q[0]+0.2, Q[1], f"Q({int(Q[0])},{int(Q[1])})", fontsize=10, color="green")
plt.text(M[0]+0.2, M[1], f"M({int(M[0])},{int(M[1])})", fontsize=10, color="purple")

plt.title("Line PQ with Midpoint M(2,-5)")
plt.grid(True)
plt.legend()
plt.axis("equal")

plt.show()
