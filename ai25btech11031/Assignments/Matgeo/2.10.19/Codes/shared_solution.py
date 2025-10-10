import ctypes
import numpy as np
import matplotlib.pyplot as plt

# Load shared library
lib = ctypes.CDLL("./Solution.so")

# Define function signatures
lib.dot.argtypes = [ctypes.POINTER(ctypes.c_int), ctypes.POINTER(ctypes.c_int)]
lib.dot.restype = ctypes.c_int

lib.cross.argtypes = [ctypes.POINTER(ctypes.c_int), ctypes.POINTER(ctypes.c_int), ctypes.POINTER(ctypes.c_int)]
lib.cross.restype = None

def dot(a, b):
    a_arr = (ctypes.c_int * 3)(*a)
    b_arr = (ctypes.c_int * 3)(*b)
    return lib.dot(a_arr, b_arr)

def cross(a, b):
    a_arr = (ctypes.c_int * 3)(*a)
    b_arr = (ctypes.c_int * 3)(*b)
    result = (ctypes.c_int * 3)()
    lib.cross(a_arr, b_arr, result)
    return [result[0], result[1], result[2]]

def compute(u, v, w):
    A = dot(u, cross(v, w))      # u · (v × w)
    B = dot(v, cross(u, w))      # v · (u × w)
    C = dot(cross(v, w), u)      # (v × w) · u
    D = dot(cross(u, v), w)      # (u × v) · w
    return A, B, C, D

def plot_vectors(u, v, w):
    fig = plt.figure()
    ax = fig.add_subplot(111, projection="3d")

    origin = [0, 0, 0]

    # Plot u, v, w
    ax.quiver(*origin, *u, color="r", label="u", arrow_length_ratio=0.1)
    ax.quiver(*origin, *v, color="g", label="v", arrow_length_ratio=0.1)
    ax.quiver(*origin, *w, color="b", label="w", arrow_length_ratio=0.1)

    ax.set_xlim([0, max(u[0], v[0], w[0], 1)])
    ax.set_ylim([0, max(u[1], v[1], w[1], 1)])
    ax.set_zlim([0, max(u[2], v[2], w[2], 1)])

    ax.set_xlabel("X")
    ax.set_ylabel("Y")
    ax.set_zlabel("Z")
    ax.legend()
    plt.show()

if __name__ == "__main__":
    u = list(map(int, input("Enter vector u (x y z): ").split()))
    v = list(map(int, input("Enter vector v (x y z): ").split()))
    w = list(map(int, input("Enter vector w (x y z): ").split()))

    A, B, C, D = compute(u, v, w)

    print("\nResults:")
    print(f"A = u · (v × w) = {A}")
    print(f"B = v · (u × w) = {B}")
    print(f"C = (v × w) · u = {C}")
    print(f"D = (u × v) · w = {D}")

    if A == C == D and B != A:
        print("\n=> Expression B is different.")
    elif B == C == D and A != B:
        print("\n=> Expression A is different.")
    elif A == B == D and C != A:
        print("\n=> Expression C is different.")
    elif A == B == C and D != A:
        print("\n=> Expression D is different.")
    else:
        print("\n=> No unique difference found.")

    # Plot the vectors
    plot_vectors(u, v, w)

