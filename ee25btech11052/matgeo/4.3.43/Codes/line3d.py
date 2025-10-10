import ctypes
import numpy as np
import matplotlib.pyplot as plt

# Load C library (compile with: gcc -shared -o libline3d.so -fPIC line3d.c)
lib = ctypes.CDLL("/home/shriyasnh/Desktop/matgeonew/4.3.43/Codes/libline3d.so")

# Function signature
lib.line3d.argtypes = [ctypes.c_double, ctypes.c_double, ctypes.c_double,
                       ctypes.c_double, ctypes.c_double, ctypes.c_double,
                       ctypes.c_double,
                       ctypes.POINTER(ctypes.c_double),
                       ctypes.POINTER(ctypes.c_double),
                       ctypes.POINTER(ctypes.c_double)]

def line3d(P1, P2, lambdas):
    xs, ys, zs = [], [], []
    for lam in lambdas:
        x = ctypes.c_double()
        y = ctypes.c_double()
        z = ctypes.c_double()
        lib.line3d(P1[0], P1[1], P1[2],
                   P2[0], P2[1], P2[2],
                   lam, ctypes.byref(x), ctypes.byref(y), ctypes.byref(z))
        xs.append(x.value)
        ys.append(y.value)
        zs.append(z.value)
    return np.array(xs), np.array(ys), np.array(zs)

if __name__ == "__main__":
    P1 = (3, -2, -5)
    P2 = (3, -2, 6)
    lambdas = np.linspace(-1, 2, 50)

    xs, ys, zs = line3d(P1, P2, lambdas)

    fig = plt.figure()
    ax = fig.add_subplot(111, projection="3d")
    ax.plot(xs, ys, zs, 'k--', label="Line")
    ax.scatter(*P1, color="red", label="P1 (3,-2,-5)")
    ax.scatter(*P2, color="blue", label="P2 (3,-2,6)")

    ax.set_xlabel("X")
    ax.set_ylabel("Y")
    ax.set_zlabel("Z")
    ax.legend()
    plt.show()
    plt.savefig("/home/shriyasnh/Desktop/matgeonew/4.3.43/Figs/line3d.png", dpi=300, bbox_inches='tight')

