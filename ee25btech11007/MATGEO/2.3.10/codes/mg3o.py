import ctypes
from ctypes import c_double, c_int
import numpy as np
import matplotlib.pyplot as plt

# --- load the shared lib ---
# Change name below if you're on macOS (.dylib) or Windows (.dll)
lib = ctypes.CDLL("./mg3.so")

# C signature:
# int solve_angle_simple(const double *a, const double *b, int n, double *theta_deg)
lib.solve_angle_simple.argtypes = [
    ctypes.POINTER(c_double),
    ctypes.POINTER(c_double),
    c_int,
    ctypes.POINTER(c_double),
]
lib.solve_angle_simple.restype = c_int

def solve_angle_np(a: np.ndarray, b: np.ndarray):
    """
    Call the C function using NumPy arrays a, b (1D, same length).
    Returns (theta_deg, status) where status==0 if the unit checks passed.
    """
    a = np.asarray(a, dtype=np.float64).ravel()
    b = np.asarray(b, dtype=np.float64).ravel()
    if a.shape != b.shape:
        raise ValueError("a and b must have the same shape")

    theta = c_double(0.0)
    pa = a.ctypes.data_as(ctypes.POINTER(c_double))
    pb = b.ctypes.data_as(ctypes.POINTER(c_double))
    status = lib.solve_angle_simple(pa, pb, a.size, ctypes.byref(theta))
    return theta.value, status

def plot_vectors(a: np.ndarray, b: np.ndarray, theta_deg: float):
    """Plot a, b, and a - √2 b on the unit circle for context."""
    a = np.asarray(a, dtype=np.float64).ravel()
    b = np.asarray(b, dtype=np.float64).ravel()
    c = a - np.sqrt(2.0) * b

    # 2D only for plotting
    if a.size != 2:
        raise ValueError("Plot expects 2D vectors (length 2).")

    # unit circle
    t = np.linspace(0, 2*np.pi, 400)
    plt.figure(figsize=(6,6))
    plt.plot(np.cos(t), np.sin(t), label="Unit circle")

    # vectors
    plt.quiver(0,0, a[0], a[1], angles='xy', scale_units='xy', scale=1, label="a")
    plt.quiver(0,0, b[0], b[1], angles='xy', scale_units='xy', scale=1, label="b")
    plt.quiver(0,0, c[0], c[1], angles='xy', scale_units='xy', scale=1, label="a − √2 b")

    # angle arc (between a and b) if both unit and 2D
    theta = np.deg2rad(theta_deg)
    arc = np.linspace(0, theta, 100)
    plt.plot(0.25*np.cos(arc), 0.25*np.sin(arc))
    plt.text(0.32*np.cos(theta/2), 0.32*np.sin(theta/2), rf"$\theta={theta_deg:.0f}^\circ$")

    plt.gca().set_aspect('equal', adjustable='box')
    plt.grid(True, linewidth=0.4, alpha=0.5)
    plt.xlim(-1.6, 1.6); plt.ylim(-1.6, 1.6)
    plt.legend()
    plt.title("Vectors a, b, and a − √2 b")
    plt.tight_layout()
    plt.show()

if __name__ == "__main__":
    # Example: a is x-axis unit; b is unit at 45°
    a = np.array([1.0, 0.0])
    b = np.array([np.cos(np.pi/4), np.sin(np.pi/4)])

    theta_deg, status = solve_angle_np(a, b)
    print(f"theta from C = {theta_deg:.6f}°, status={status} (0 means unit checks passed)")
    print(f"||a||={np.linalg.norm(a):.3f}, ||b||={np.linalg.norm(b):.3f}, "
          f"||a-√2 b||={np.linalg.norm(a - np.sqrt(2)*b):.3f}")

    plot_vectors(a, b, theta_deg)
