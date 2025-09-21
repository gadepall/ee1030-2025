import numpy as np
import matplotlib.pyplot as plt

# Function for norm
def norm(v):
    return np.sqrt(np.dot(v, v))

# Input points (A,B,C,D)
A = np.array([1, -2], dtype=float)
B = np.array([2,  3], dtype=float)
C = np.array([None, 2], dtype=float)   # a unknown
D = np.array([-4, -3], dtype=float)

# --- Step 1: Find a using parallelogram condition A+C = B+D ---
a_val = (B[0] + D[0]) - A[0]   # x-component
C[0] = a_val
print(f"Value of a = {a_val}")

# --- Step 2: Base vector and AC vector ---
u = B - A   # AB
v = C - A   # AC

# Projection of v onto u
proj = (np.dot(v,u)/np.dot(u,u)) * u

# Perpendicular component
w = v - proj

# Height = norm of perpendicular
h = norm(w)
print(f"Height of parallelogram (AB as base) = {h}")

# --- Step 3: Plotting ---
fig, ax = plt.subplots(figsize=(6,6))

# Plot parallelogram
x_vals = [A[0], B[0], C[0], D[0], A[0]]
y_vals = [A[1], B[1], C[1], D[1], A[1]]
ax.plot(x_vals, y_vals, 'k-', linewidth=2)

# Points with labels
for point, label in zip([A,B,C,D], ["A","B","C","D"]):
    ax.scatter(*point, color="red")
    ax.text(point[0]+0.2, point[1]+0.2, f"{label}{tuple(map(int,point))}")

# Draw height from C to AB
Foot = A + proj  # foot of perpendicular
ax.plot([C[0], Foot[0]], [C[1], Foot[1]], 'r-', linewidth=2, label="Height")
ax.scatter(Foot[0], Foot[1], color="blue")
ax.text(Foot[0]+0.2, Foot[1]-0.3, "foot", color="blue")

# Formatting
ax.axhline(0, color='gray', linewidth=0.8)
ax.axvline(0, color='gray', linewidth=0.8)
ax.set_aspect('equal', 'box')
ax.grid(True, linestyle=':', alpha=0.5)
ax.legend()
ax.set_xlim(-6,4)
ax.set_ylim(-5,5)
plt.show()
