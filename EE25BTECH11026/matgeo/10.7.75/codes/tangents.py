import ctypes
import numpy as np
import matplotlib.pyplot as plt

# Load shared C library
lib = ctypes.CDLL("./libtangent_solver.so")

# Define C function signature
lib.solve_tangents.argtypes = [ctypes.c_double, ctypes.c_double,
                               ctypes.POINTER(ctypes.c_double)]
lib.solve_tangents.restype = None

def get_tangents_from_c(r, h):
    results = (ctypes.c_double * 4)()
    lib.solve_tangents(r, h, results)
    vals = list(results)
    tangents = [(vals[0], vals[1]), (vals[2], vals[3])]

    tangent_eqs = []
    for a, b in tangents:
        if b == 0:  # x=0
            tangent_eqs.append("x = 0")
        elif a == 0:  # y=0
            tangent_eqs.append("y = 0")
        else:
            tangent_eqs.append(f"{a:.0f}x {b:+.0f}y = 0")

    return tangents, tangent_eqs


def plot_tangents(r, h):
    tangents, tangent_eqs = get_tangents_from_c(r, h)

    print("Tangents from origin:")
    for eq in tangent_eqs:
        print("   ", eq)

    # Circle
    theta = np.linspace(0, 2*np.pi, 400)
    x_circ = r + r*np.cos(theta)
    y_circ = h + r*np.sin(theta)

    plt.figure(figsize=(6,6))
    plt.plot(x_circ, y_circ, 'b', label="Circle")

    # Tangents
    x_vals = np.linspace(-2*r, 2*r, 400)
    for (a,b), eq in zip(tangents, tangent_eqs):
        if b == 0:
            plt.axvline(0, color='r', linestyle='--', label=eq)
        else:
            y_vals = -(a/b)*x_vals
            plt.plot(x_vals, y_vals, 'r--', label=eq)

    # Origin & center
    plt.scatter([0],[0], color='k', marker='o', label="Origin (0,0)")
    plt.scatter([r],[h], color='g', marker='x', label=f"Center ({r},{h})")

    plt.gca().set_aspect('equal', adjustable='box')
    plt.axhline(0, color='gray', linewidth=0.5)
    plt.axvline(0, color='gray', linewidth=0.5)
    plt.legend()
    plt.title(f"Tangents from Origin to Circle (r={r}, h={h})")
    plt.savefig("/home/user/Matrix Theory: workspace/Matgeo_assignments/10.7.75/figs/figure_1.png")
    plt.show()


# Example
plot_tangents(r=3, h=4)

