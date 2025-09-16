import ctypes
import numpy as np
import matplotlib.pyplot as plt

# Load shared library (Linux/Mac)
lib = ctypes.CDLL("./libvector.so")

# Set argument and return types
lib.compute_u.argtypes = [ctypes.POINTER(ctypes.c_double),
                          ctypes.POINTER(ctypes.c_double),
                          ctypes.POINTER(ctypes.c_double)]
lib.cross.argtypes = [ctypes.POINTER(ctypes.c_double),
                      ctypes.POINTER(ctypes.c_double),
                      ctypes.POINTER(ctypes.c_double)]

# Helper function to call C compute_u
def compute_u(a, b):
    a_c = (ctypes.c_double * 3)(*a)
    b_c = (ctypes.c_double * 3)(*b)
    u_c = (ctypes.c_double * 3)()
    lib.compute_u(a_c, b_c, u_c)
    return np.array([u_c[0], u_c[1], u_c[2]])

# Helper function to call C cross
def compute_cross(a, b):
    a_c = (ctypes.c_double * 3)(*a)
    b_c = (ctypes.c_double * 3)(*b)
    v_c = (ctypes.c_double * 3)()
    lib.cross(a_c, b_c, v_c)
    return np.array([v_c[0], v_c[1], v_c[2]])

# Define vectors
a = np.array([1, 0, 0], dtype=float)
b = np.array([0.5, np.sqrt(3)/2, 0], dtype=float)

# Compute using C functions
u = compute_u(a, b)
v = compute_cross(a, b)

print("u =", u)
print("v =", v)

# Plot results
fig = plt.figure(figsize=(8, 8))
ax = fig.add_subplot(111, projection="3d")

def draw_vec(ax, vec, color, label):
    ax.quiver(0, 0, 0, vec[0], vec[1], vec[2],
              color=color, arrow_length_ratio=0.1, linewidth=2)
    ax.text(vec[0]*1.1, vec[1]*1.1, vec[2]*1.1, label, color=color, fontsize=12)

draw_vec(ax, a, "blue", r"$\vec{a}$")
draw_vec(ax, b, "green", r"$\vec{b}$")
draw_vec(ax, u, "red", r"$\vec{u}$")
draw_vec(ax, v, "purple", r"$\vec{v}$")

ax.set_xlim([-1, 1.5])
ax.set_ylim([-1, 1.5])
ax.set_zlim([-1, 1.5])

ax.set_xlabel("X")
ax.set_ylabel("Y")
ax.set_zlabel("Z")
ax.set_title("Vectors from C Library", fontsize=14)

plt.tight_layout()

# Save figure to file
plt.savefig("vector_plot.png", dpi=300)   # you can also use "vector_plot.pdf"
plt.show()

