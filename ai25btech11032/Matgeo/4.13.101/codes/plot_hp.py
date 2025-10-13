# plot_hp_3d.py
import ctypes
from ctypes import c_double, POINTER, byref
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D  # noqa: F401 (needed for 3D projection)

# load shared library (libhp.so should be in current working directory)
lib = ctypes.CDLL("./libhp.so")

# bind functions
lib.analyze_system.argtypes = (c_double, c_double, c_double,
                               POINTER(c_double), POINTER(c_double))
lib.analyze_system.restype = ctypes.c_int

lib.parametric_solution.argtypes = (c_double, POINTER(c_double),
                                    POINTER(c_double), POINTER(c_double))
lib.parametric_solution.restype = None

# row_reduce signature: void row_reduce_3x4(const double A_in[3][4], double A_out[3][4]);
lib.row_reduce_3x4.argtypes = (POINTER(c_double), POINTER(c_double))
lib.row_reduce_3x4.restype = None

# Python wrappers
def analyze(p, q, r):
    D = c_double(); E = c_double()
    code = lib.analyze_system(c_double(p), c_double(q), c_double(r),
                              byref(D), byref(E))
    return int(code), D.value, E.value

def param_sol(t):
    x = c_double(); y = c_double(); z = c_double()
    lib.parametric_solution(c_double(t), byref(x), byref(y), byref(z))
    return x.value, y.value, z.value

def row_reduce(A):
    """
    A : numpy array shape (3,4), dtype float64 (row-major).
    Returns reduced 3x4 numpy array (copy).
    """
    A = np.asarray(A, dtype=np.float64, order='C')
    if A.shape != (3,4):
        raise ValueError("A must be shape (3,4)")
    ArrayType = c_double * 12
    in_buf = ArrayType(*A.ravel().tolist())
    out_buf = ArrayType()
    lib.row_reduce_3x4(in_buf, out_buf)
    return np.frombuffer(out_buf, dtype=np.float64).reshape((3,4)).copy()

# ---- Main demo ----
if __name__ == "__main__":
    # change these to test other triples
    p, q, r = 100.0, 10.0, 1.0

    # Build augmented matrix [M | b]
    A = np.array([
        [1.0,    1.0,    1.0,    1.0],
        [10.0, 100.0, 1000.0,    0.0],
        [q*r,   p*r,   p*q,      0.0]
    ], dtype=np.float64)

    # Call row reduction and show result
    A_red = row_reduce(A)
    print("Reduced augmented matrix (after specified elimination steps):")
    np.set_printoptions(precision=6, suppress=True)
    print(A_red)

    # Analyze system
    code, D, E = analyze(p, q, r)
    print(f"analyze_system -> code={code}, D={D}, E={E}")
    # code: 0 = unique, 1 = no solution, 2 = infinitely many

    # If consistent (infinitely many), plot 3D solution curve
    if code == 2:
        ts = np.linspace(-1.0, 1.0, 401)
        xs = np.empty_like(ts); ys = np.empty_like(ts); zs = np.empty_like(ts)
        for i, t in enumerate(ts):
            xs[i], ys[i], zs[i] = param_sol(t)

        fig = plt.figure(figsize=(7,7))
        ax = fig.add_subplot(111, projection='3d')
        ax.plot(xs, ys, zs, lw=2)
        ax.set_xlabel('x'); ax.set_ylabel('y'); ax.set_zlabel('z')
        ax.set_title(f'Solution curve (p={p}, q={q}, r={r})')
        plt.tight_layout()
        outname = "hp_3d_only.png"
        fig.savefig(outname, dpi=200)
        print("Saved 3D plot:", outname)
    else:
        print("System not consistent — nothing to plot.")

