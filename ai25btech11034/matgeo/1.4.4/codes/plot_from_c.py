
import os
import sys
import ctypes
from ctypes import c_double, byref
import matplotlib.pyplot as plt

def _load_lib():
    # Resolve platform-specific shared library filename
    here = os.path.dirname(os.path.abspath(__file__))
    candidates = []
    if sys.platform.startswith("linux"):
        candidates = [os.path.join(here, "libpoint.so")]
    elif sys.platform == "darwin":
        candidates = [os.path.join(here, "libpoint.dylib")]
    elif os.name == "nt":
        candidates = [os.path.join(here, "point_utils.dll")]
    else:
        raise RuntimeError("Unsupported platform: " + sys.platform)

    for path in candidates:
        if os.path.exists(path):
            return ctypes.CDLL(path)

    raise FileNotFoundError(
        "Shared library not found. Expected one of: " + ", ".join(candidates)
    )

# Wrapper around the C function
def compute_R_from_C(P, Q, m, n):
    lib = _load_lib()
    lib.findPoint.argtypes = [c_double, c_double, c_double, c_double, c_double, c_double,
                              ctypes.POINTER(c_double), ctypes.POINTER(c_double)]
    lib.findPoint.restype  = None

    rx = c_double()
    ry = c_double()
    lib.findPoint(P[0], P[1], Q[0], Q[1], float(m), float(n), byref(rx), byref(ry))
    return (rx.value, ry.value)

def plot_points_with_c(P=(4,3), Q=(8,5), m=3, n=1, save_as="plotc.png"):
    R = compute_R_from_C(P, Q, m, n)

    # Plot line PQ
    plt.plot([P[0], Q[0]], [P[1], Q[1]], linestyle='--', label="Line PQ")

    # Plot points
    plt.scatter(P[0], P[1], label=f"P{P}")
    plt.scatter(Q[0], Q[1], label=f"Q{Q}")
    plt.scatter(R[0], R[1], label=f"R{tuple(round(v,4) for v in R)}")

    # Annotate points
    plt.text(P[0], P[1], "P")
    plt.text(Q[0], Q[1], "Q")
    plt.text(R[0], R[1], "R")

    # Style
    plt.xlabel("x-axis")
    plt.ylabel("y-axis")
    plt.title(f"Point R dividing PQ in ratio {m}:{n} (C + Python)")
    plt.legend()
    plt.grid(True)
    plt.axis("equal")
    plt.savefig(save_as, dpi=300)
    # plt.show()

if __name__ == "__main__":
    # Default example
    plot_points_with_c()
    print("Saved plot to", os.path.abspath("plotc.png"))
