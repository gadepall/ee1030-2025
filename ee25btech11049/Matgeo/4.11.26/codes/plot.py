import numpy as np
import matplotlib.pyplot as plt
from libs.funcs import line_gen

# --- 1. Define Lines in Matrix Form (n.T * x = c) ---
n1 = np.array([1, -1]).reshape(-1, 1)
c1 = 1
n2 = np.array([1, 1]).reshape(-1, 1)
c2 = 1
n3 = np.array([0, 1]).reshape(-1, 1)
c3 = 1

# --- 2. Find Vertices using Matrix Inversion ---
# This function solves a 2x2 system to find the intersection point
def get_intersection(n_a, c_a, n_b, c_b):
    # Form the matrix N = [n_a.T; n_b.T]
    N = np.block([[n_a.T], [n_b.T]])
    # Form the vector C = [c_a; c_b]
    C = np.array([c_a, c_b]).reshape(-1, 1)
    # Solve for the intersection point x = N_inv * C
    N_inv = np.linalg.inv(N)
    intersection_point = N_inv @ C
    return intersection_point

# Calculate the three vertices
A = get_intersection(n1, c1, n2, c2)
B = get_intersection(n1, c1, n3, c3)
C = get_intersection(n2, c2, n3, c3)

print("--- Vertices calculated via Matrix Inversion ---")
print(f"Vertex A: {A.flatten()}")
print(f"Vertex B: {B.flatten()}")
print(f"Vertex C: {C.flatten()}")

# --- 3. Calculate Area using Vector Determinant ---
# Form vectors for two sides of the triangle
vec_AB = B - A
vec_AC = C - A

# Create the matrix from the side vectors
M_area = np.hstack([vec_AB, vec_AC])

# Area is 0.5 * |det(M_area)|
area = 0.5 * np.abs(np.linalg.det(M_area))

print(f"\n--- Area Calculation ---")
print(f"Matrix of side vectors:\n{M_area}")
print(f"Determinant: {np.linalg.det(M_area):.1f}")
print(f"Calculated Area: {area:.2f} square units")

# --- 4. Plotting ---
plt.figure(figsize=(8, 6))

# Generate lines for plotting
line_AC = line_gen(A, C)
line_AB = line_gen(A, B)
line_CB = line_gen(C, B)

# Plot the lines and fill the area
plt.plot(line_AC[0, :], line_AC[1, :], 'b-', label='x + y = 1')
plt.plot(line_AB[0, :], line_AB[1, :], 'g-', label='x - y = 1')
plt.plot(line_CB[0, :], line_CB[1, :], 'r-', label='y = 1')
plt.fill([A[0,0], C[0,0], B[0,0]], [A[1,0], C[1,0], B[1,0]], 'skyblue', alpha=0.6)

# Plot the vertices
plt.plot(A[0], A[1], 'o', color='black', markersize=8, label='Vertex A')
plt.plot(B[0], B[1], 'o', color='black', markersize=8, label='Vertex B')
plt.plot(C[0], C[1], 'o', color='black', markersize=8, label='Vertex C')

# --- 5. Plot Customization ---
plt.title(f'Area bounded by y = |x-1| and y = 1')
plt.xlabel("x-axis")
plt.ylabel("y-axis")
plt.grid(True)
plt.axhline(0, color='black', linewidth=0.7)
plt.axvline(0, color='black', linewidth=0.7)
plt.axis('equal')
plt.legend()
plt.show()

