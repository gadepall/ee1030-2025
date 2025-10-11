import ctypes
import numpy as np

# Load C library
lib = ctypes.CDLL("./nor_points.so")
lib.generate_line_points.argtypes = [
    ctypes.c_double,
    ctypes.POINTER(ctypes.c_double),
    ctypes.POINTER(ctypes.c_double)
]

def get_line_points(m):
    P = (ctypes.c_double * 2)()
    Q = (ctypes.c_double * 2)()
    lib.generate_line_points(ctypes.c_double(m), P, Q)
    return np.array([P[0], P[1]]), np.array([Q[0], Q[1]])

def compute_R_points(m_values):
    R_points = []
    for m in m_values:
        if m == 0:  # avoid horizontal line
            continue
        P, Q = get_line_points(m)
        R = P + Q
        R_points.append(R)
    return np.array(R_points)

if __name__ == "__main__":
    # Use fine slope sampling for smooth curve
    slopes = np.linspace(-50, 50, 2000)
    R_pts = compute_R_points(slopes)
    np.save("R_points.npy", R_pts)

