import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d.art3d import Poly3DCollection
import os

# Custom sqrt using Newton-Raphson
def sqrt_newton(n, tolerance=1e-9):
    x = n
    y = 1.0
    while x - y > tolerance:
        x = (x + y) / 2
        y = n / x
    return x

# Define points
A = [1, 2, 3]
B = [2, -1, 4]
C = [4, 5, -1]

# Define vectors (B - A) and (C - A)
AB = [B[i] - A[i] for i in range(3)]
AC = [C[i] - A[i] for i in range(3)]

# Compute norms squared
AB_sq = sum(x*x for x in AB)
AC_sq = sum(x*x for x in AC)

# Dot product
dot = sum(AB[i]*AC[i] for i in range(3))

# Using identity: |AB x AC|^2 = |AB|^2|AC|^2 - (AB · AC)^2
cross_sq = AB_sq * AC_sq - dot * dot

# Magnitude of cross product using custom sqrt
cross_norm = sqrt_newton(cross_sq)

# Area of triangle
area = 0.5 * cross_norm

# Print results
print(f"||AB||^2 = {AB_sq}")
print(f"||AC||^2 = {AC_sq}")
print(f"AB · AC = {dot}")
print(f"||AB x AC||^2 = {cross_sq}")
print(f"||AB x AC|| = {cross_norm:.6f}")
print(f"Area of triangle ABC = {area:.6f}")

# -----------------------------
# Plot the triangle in 3D
# -----------------------------
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

# Plot points
ax.scatter(*A, color='r', s=50, label='A(1,2,3)')
ax.scatter(*B, color='g', s=50, label='B(2,-1,4)')
ax.scatter(*C, color='b', s=50, label='C(4,5,-1)')

# Plot triangle surface
verts = [[A, B, C]]
ax.add_collection3d(Poly3DCollection(verts, alpha=0.3, facecolor='cyan'))

# Label axes
ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Z')
ax.legend()
ax.set_title("Triangle ABC (Image Visual)")

# -----------------------------
# Save figure to figs/image.png
# -----------------------------
os.makedirs("figs", exist_ok=True)  # create folder if not exists
plt.savefig("figs/image.png", dpi=300, bbox_inches='tight')

plt.show()
