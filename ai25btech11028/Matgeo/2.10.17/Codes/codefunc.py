 import ctypes
import numpy as np
import matplotlib.pyplot as plt

# Load shared library (relative path)
vec = ctypes.CDLL("./libvec.so")

# Define C function signature
vec.analyze_vector.argtypes = (
    ctypes.c_double, ctypes.c_double, ctypes.c_double,  # v
    ctypes.c_double, ctypes.c_double, ctypes.c_double,  # u
    ctypes.c_double, ctypes.c_double, ctypes.c_double,  # w
    ctypes.POINTER(ctypes.c_double),  # mag
    ctypes.POINTER(ctypes.c_double),  # par_t
    ctypes.POINTER(ctypes.c_double)   # dot_vw
)
vec.analyze_vector.restype = None

def analyze_vector(v: np.ndarray, u: np.ndarray, w: np.ndarray):
    """Call the C function via ctypes."""
    mag = ctypes.c_double()
    par_t = ctypes.c_double()
    dot_vw = ctypes.c_double()

    vec.analyze_vector(
        v[0], v[1], v[2],
        u[0], u[1], u[2],
        w[0], w[1], w[2],
        ctypes.byref(mag),
        ctypes.byref(par_t),
        ctypes.byref(dot_vw)
    )
    return mag.value, par_t.value, dot_vw.value
if __name__ == "__main__":
    v = np.array([2/3, -2/3, 1/3])
    u = np.array([-1, 1, -0.5])
    w = np.array([3, 2, -2])

    mag, par_t, dot_vw = analyze_vector(v, u, w)

    print("||v|| =", mag)
    if np.isnan(par_t):
        print("v is NOT parallel to u")
    else:
        print(f"v is parallel to u, scalar t = {par_t}")
    print("v^T w =", dot_vw)

    # === Plotting ===
    fig = plt.figure()
    ax = fig.add_subplot(111, projection="3d")
 origin = np.array([0, 0, 0])
    ax.quiver(*origin, *v, color="r", label="v")
    ax.quiver(*origin, *u, color="g", label="u")
    ax.quiver(*origin, *w, color="b", label="w")

    ax.set_xlabel("X")
    ax.set_ylabel("Y")
    ax.set_zlabel("Z")
    ax.legend()


# Save before show
plt.savefig("/storage/emulated/0/matrix/Matgeo/2.10.17/figs/Figure_1.png", dpi=300, bbox_inches='tight')
plt.show()
