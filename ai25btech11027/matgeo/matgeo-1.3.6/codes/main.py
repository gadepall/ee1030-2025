import numpy as np
import matplotlib.pyplot as plt

# Define the points of the quadrilateral
A = np.array([6, 2])
B = np.array([2, 1])
C = np.array([1, 5])
D = np.array([5, 6])

# Function to compute distance between two points
def distance(P, Q):
    return np.linalg.norm(P - Q)

# Function to compute vector between two points
def vector(P, Q):
    return Q - P

# Function to compute dot product of two vectors
def dot(u, v):
    return np.dot(u, v)

# Function to check if two vectors are perpendicular
def is_perpendicular(u, v):
    return np.isclose(dot(u, v), 0, atol=1e-8)

# Step 1: Check if it's a parallelogram
AB = vector(A, B)
BC = vector(B, C)
CD = vector(C, D)
DA = vector(D, A)

# Opposite sides
AB_len = distance(A, B)
CD_len = distance(C, D)

BC_len = distance(B, C)
DA_len = distance(D, A)

# Check if opposite sides are equal
opp_sides_equal = np.isclose(AB_len, CD_len) and np.isclose(BC_len, DA_len)

# Check if opposite sides are parallel (same direction vector)
AB_CD_parallel = np.allclose(AB / np.linalg.norm(AB), -CD / np.linalg.norm(CD))
BC_DA_parallel = np.allclose(BC / np.linalg.norm(BC), -DA / np.linalg.norm(DA))

is_parallelogram = opp_sides_equal and AB_CD_parallel and BC_DA_parallel

# Step 2: Check if any angle is 90° to prove it's a rectangle
# Use dot product between adjacent sides
angle_at_B = is_perpendicular(AB, BC)

is_rectangle = is_parallelogram and angle_at_B

# Step 3: Check if diagonals are perpendicular ⇒ square
AC = vector(A, C)
BD = vector(B, D)

diagonals_perpendicular = is_perpendicular(AC, BD)

is_square = is_rectangle and diagonals_perpendicular

# ----------- Output the Results -----------
print("Step-by-step proof:\n")

print("1. Opposite sides equal?", opp_sides_equal)
print("2. Opposite sides parallel?", AB_CD_parallel and BC_DA_parallel)
print("➡️ Is it a parallelogram?", is_parallelogram)

print("\n3. Angle at A is 90°?", angle_at_B)
print("➡️ Is it a rectangle?", is_rectangle)

print("\n4. Diagonals are perpendicular?", diagonals_perpendicular)
print("➡️ Is it a square?", is_square)

# ----------- Plotting -----------
points = [A, B, C, D, A]  # Loop back to A
x = [p[0] for p in points]
y = [p[1] for p in points]

plt.figure(figsize=(6,6))
plt.plot(x, y, 'k-', linewidth=2)

# Mark points
labels = ['A', 'B', 'C', 'D']
colors = ['red', 'green', 'blue', 'orange']
for pt, lbl, clr in zip(points[:-1], labels, colors):
    plt.plot(pt[0], pt[1], 'o', color=clr, markersize=8)
    plt.text(pt[0] + 0.2, pt[1] + 0.2, f'{lbl}({pt[0]},{pt[1]})', fontsize=12, color=clr)

# Draw diagonals
plt.plot([A[0], C[0]], [A[1], C[1]], 'r--', label='AC (Diagonal)', linewidth=1.5)
plt.plot([B[0], D[0]], [B[1], D[1]], 'b--', label='BD (Diagonal)', linewidth=1.5)

plt.title("Quadrilateral ABCD with Diagonals")
plt.gca().set_aspect('equal', adjustable='box')
plt.grid(True)
plt.legend()
plt.xlabel('x')
plt.ylabel('y')
plt.show()
