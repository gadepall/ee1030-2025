
import ctypes
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# Load shared library built from plane.c
lib = ctypes.CDLL('./plane.so')

# C function signatures
lib.cross_product.argtypes = [
    ctypes.POINTER(ctypes.c_double),
    ctypes.POINTER(ctypes.c_double),
    ctypes.POINTER(ctypes.c_double),
]
lib.cross_product.restype = None

def read_vectors_from_file(filename):
    vectors = {}
    with open(filename, 'r') as f:
        for line in f:
            parts = line.strip().split()
            if len(parts) != 4:
                continue
            name = parts[0]  # Fixed: should be parts[0] not just parts
            x, y, z = map(float, parts[1:4])
            vectors[name] = [x, y, z]
    return vectors

def c_cross(a, b):
    a_arr = (ctypes.c_double * 3)(*a)
    b_arr = (ctypes.c_double * 3)(*b)
    r_arr = (ctypes.c_double * 3)()
    lib.cross_product(a_arr, b_arr, r_arr)
    return [r_arr[0], r_arr[1], r_arr[2]]  # Fixed: proper indexing

def solve_and_prepare():
    V = read_vectors_from_file('vector.dat')
    n1, n2 = V['n1'], V['n2']
    a = V['a']
    u = V['u']  # Added vector u
    # Optional verification of n3:
    _n3_check = c_cross(n1, n2)
    return a, u, n1, n2  # Return u instead of n3

def plot_planes_and_vectors(a, u, n1, n2):
    fig = plt.figure(figsize=(10, 8))
    ax = fig.add_subplot(111, projection='3d')

    # Grid for planes
    lim = 2.0
    X = np.linspace(-lim, lim, 25)
    Y = np.linspace(-lim, lim, 25)
    X, Y = np.meshgrid(X, Y)

    # Plane 1: n1 = (A1,B1,C1), Ax+By+Cz=0 => z = -(A1 x + B1 y)/C1
    A1, B1, C1 = n1
    if abs(C1) > 1e-9:
        Z1 = -(A1*X + B1*Y)/C1
        ax.plot_surface(X, Y, Z1, alpha=0.25, color='gray', edgecolor='none')

    # Plane 2: n2 = (A2,B2,C2)
    A2, B2, C2 = n2
    if abs(C2) > 1e-9:
        Z2 = -(A2*X + B2*Y)/C2
        ax.plot_surface(X, Y, Z2, alpha=0.25, color='orange', edgecolor='none')

    # Vectors a and u only (removed n3)
    origin = [0, 0, 0]
    ax.quiver(*origin, *a, color='red', arrow_length_ratio=0.1, linewidth=3, label='Vector a')
    ax.quiver(*origin, *u, color='blue', arrow_length_ratio=0.1, linewidth=3, label='Vector u')

    # Fixed: proper indexing for text labels
    ax.text(a[0], a[1], a[2], 'a', fontsize=12, color='red', weight='bold')
    ax.text(u[0], u[1], u[2], 'u', fontsize=12, color='blue', weight='bold')

    ax.set_xlabel('X')
    ax.set_ylabel('Y')
    ax.set_zlabel('Z')
    ax.set_title('Planes and vectors a, u')

    # Legends for planes
    from matplotlib.patches import Patch
    leg_planes = [
        Patch(facecolor='gray', alpha=0.25, label='Plane 1 (i, i+j)'),
        Patch(facecolor='orange', alpha=0.25, label='Plane 2 (i-j, i+k)'),
    ]
    ax.legend(handles=leg_planes, loc='upper left')
    ax.legend(loc='upper right')

    max_val = max(max(abs(x) for x in a), max(abs(x) for x in u), lim)
    margin = 0.2 * max_val
    ax.set_xlim(-max_val - margin, max_val + margin)
    ax.set_ylim(-max_val - margin, max_val + margin)
    ax.set_zlim(-max_val - margin, max_val + margin)
    ax.set_box_aspect([1, 1, 1])
    ax.grid(True)

    plt.savefig('fig1.png', dpi=300, bbox_inches='tight')
    print('Visualization saved as fig1.png')

if __name__ == '__main__':
    a, u, n1, n2 = solve_and_prepare()
    plot_planes_and_vectors(a, u, n1, n2)
