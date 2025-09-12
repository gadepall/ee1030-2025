import numpy as np
import math
import matplotlib.pyplot as plt

# --- Define vectors ---
a = np.array([2.0, 1.0, 3.0])
b = np.array([-1.0, 2.0, 1.0])
c = np.array([3.0, 1.0, 2.0])

# --- Step 1: Build Gram matrix ---
G = np.array([
    [np.dot(a, a), np.dot(a, b), np.dot(a, c)],
    [np.dot(b, a), np.dot(b, b), np.dot(b, c)],
    [np.dot(c, a), np.dot(c, b), np.dot(c, c)]
])

print("Gram matrix:\n", G)

# --- Step 2: Compute det(G) ---
detG = np.linalg.det(G)
print("det(G) =", detG)

# --- Step 3: Magnitude of scalar triple product ---
magnitude = math.sqrt(detG)
print("|a · (b × c)| =", magnitude)

# --- Step 4: Compute sign using det(A) ---
A_mat = np.column_stack((a, b, c))   # matrix [a b c]
sign_val = np.linalg.det(A_mat)
scalar_triple = math.copysign(magnitude, sign_val)

print("a · (b × c) =", scalar_triple)

# Image Generation
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

def draw_vec(v, color, label):
    ax.quiver(0, 0, 0, v[0], v[1], v[2],
              color=color, arrow_length_ratio=0.1, label=label)

# Draw the vectors
draw_vec(a, 'r', 'a')
draw_vec(b, 'g', 'b')
draw_vec(c, 'b', 'c')

# Optionally also draw b × c for clarity
bx_c = np.cross(b, c)
draw_vec(bx_c, 'm', 'b × c')

# Set axes limits
lim = 6
ax.set_xlim([-lim, lim])
ax.set_ylim([-lim, lim])
ax.set_zlim([-lim, lim])

# Labels
ax.set_xlabel("X")
ax.set_ylabel("Y")
ax.set_zlabel("Z")
ax.legend()

plt.title(f"Scalar triple product = {scalar_triple}")
plt.savefig("gram_triple_product_python.png", dpi=300)
plt.show()

