import ctypes
import numpy as np
import matplotlib.pyplot as plt
import matplotlib as mp
mp.use("TkAgg")

# Load shared library
lib = ctypes.CDLL("./libline_rotation.so")

# Function signatures
lib.line_intercepts_after_rotation.argtypes = [
    ctypes.c_double, ctypes.c_double, ctypes.c_double,
    ctypes.POINTER(ctypes.c_double), ctypes.POINTER(ctypes.c_double)
]
lib.line_intercepts_after_rotation.restype = None

lib.check_options.argtypes = [
    ctypes.c_double, ctypes.c_double,
    ctypes.c_double, ctypes.c_double, ctypes.c_double
]
lib.check_options.restype = ctypes.c_int


# Parameters
a, b = 3.0, 4.0
theta = np.pi / 3

# Call C function to compute new intercepts
p, q = ctypes.c_double(), ctypes.c_double()
lib.line_intercepts_after_rotation(a, b, theta, ctypes.byref(p), ctypes.byref(q))
p, q = p.value, q.value

# Check which option is true
opt = lib.check_options(a, b, p, q, 1e-8)
print(f"Correct Option: {opt}")


# ========== PLOT ONLY IF OPTION B IS TRUE ==========
if opt == 2:
    # Original line
    x_vals = np.linspace(-1, max(a, 6), 400)
    y_vals = b * (1 - x_vals / a)

    # Original intercepts
    A = (a, 0)
    B = (0, b)

    # Rotated axes directions
    e1_new = np.array([np.cos(theta), np.sin(theta)])
    e2_new = np.array([-np.sin(theta), np.cos(theta)])

    # Transform new intercepts (rotated -> original coords)
    P = np.array([
        [np.cos(theta), -np.sin(theta)],
        [np.sin(theta),  np.cos(theta)]
    ])
    Pp = P @ np.array([p, 0])
    Pq = P @ np.array([0, q])

    # Plot
    plt.figure(figsize=(7,7))
    plt.axhline(0, color='gray', lw=1)
    plt.axvline(0, color='gray', lw=1)

    # Original line
    plt.plot(x_vals, y_vals, 'b', label="Original line")

    # Original intercepts (A, B)
    plt.scatter(*A, color='blue')
    plt.text(A[0], A[1]-0.3, f"A({a:.3f},0)", ha='center', fontsize=10, color="blue")

    plt.scatter(*B, color='blue')
    plt.text(B[0]-0.3, B[1], f"B(0,{b:.3f})", va='center', fontsize=10, color="blue")

    # Rotated axes
    t = np.linspace(-6, 6, 200)
    plt.plot(t*e1_new[0], t*e1_new[1], 'r--', label="Rotated X'-axis")
    plt.plot(t*e2_new[0], t*e2_new[1], 'r--', label="Rotated Y'-axis")

    # New intercepts (P, Q)
    plt.scatter(*Pp, color='green')
    plt.text(Pp[0], Pp[1]-0.2, f"P({p:.3f},0)", color='green', ha='center', fontsize=10)

    plt.scatter(*Pq, color='green')
    plt.text(Pq[0]-0.2, Pq[1], f"Q(0,{q:.3f})", color='green', va='center', fontsize=10)

    plt.axis("equal")
    plt.legend(loc="upper right")
    plt.title("Graph for the True Relation:\n1/a² + 1/b² = 1/p² + 1/q²")
    plt.savefig("/home/user/Matrix/Matgeo_assignments/4.13.31/figs/Figure_1")
    plt.show()

