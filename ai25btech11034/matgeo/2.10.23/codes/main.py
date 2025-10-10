import numpy as np
import matplotlib.pyplot as plt
import ctypes

# Load shared library
lib = ctypes.CDLL("./function.so")

# Define argtypes and restype
lib.is_coplanar.argtypes = [ctypes.POINTER(ctypes.c_double),
                            ctypes.POINTER(ctypes.c_double),
                            ctypes.POINTER(ctypes.c_double)]
lib.is_coplanar.restype = ctypes.c_int

lib.is_perpendicular.argtypes = [ctypes.POINTER(ctypes.c_double),
                                 ctypes.POINTER(ctypes.c_double)]
lib.is_perpendicular.restype = ctypes.c_int

# Fixed vectors
A = np.array([1, 1, 2], dtype=np.double)
B = np.array([1, 2, 1], dtype=np.double)
C = np.array([1, 1, 1], dtype=np.double)

# Test D vectors
D_vectors = [
    np.array([0, 1, -1], dtype=np.double),
    np.array([1, 1, 0], dtype=np.double),
    np.array([1, -1, 0], dtype=np.double),
    np.array([0, 1, 1], dtype=np.double),
]

def check_and_plot(D, save_path):
    # Convert numpy arrays to C pointers
    A_ptr = A.ctypes.data_as(ctypes.POINTER(ctypes.c_double))
    B_ptr = B.ctypes.data_as(ctypes.POINTER(ctypes.c_double))
    C_ptr = C.ctypes.data_as(ctypes.POINTER(ctypes.c_double))
    D_ptr = D.ctypes.data_as(ctypes.POINTER(ctypes.c_double))

    # Call C functions
    is_coplanar = lib.is_coplanar(A_ptr, B_ptr, D_ptr)
    is_perpendicular = lib.is_perpendicular(C_ptr, D_ptr)

    print(f"\nVector D = {D}")
    print(f"Coplanar with A & B? {'Yes' if is_coplanar else 'No'}")
    print(f"Perpendicular to C (1,1,1)? {'Yes' if is_perpendicular else 'No'}")

    # ---- Plot ----
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')
    origin = np.array([0, 0, 0])

    ax.quiver(*origin, *A, color='r', label='A (1,1,2)')
    ax.quiver(*origin, *B, color='g', label='B (1,2,1)')
    ax.quiver(*origin, *C, color='y', label='C (1,1,1)')
    ax.quiver(*origin, *D, color='b', label=f'D {D.tolist()}')

    # Plane formed by A & B
    normal = np.cross(A, B)
    xx, yy = np.meshgrid(range(-2, 3), range(-2, 3))
    z_plane = (-normal[0]*xx - normal[1]*yy) / normal[2]
    ax.plot_surface(xx, yy, z_plane, alpha=0.3, color='cyan')

    ax.set_xlabel('X')
    ax.set_ylabel('Y')
    ax.set_zlabel('Z')
    ax.legend()
    ax.set_title("Plane with A, B, D vectors")

    plt.savefig(save_path, dpi=300)
    print(f"Figure saved at: {save_path}")
    plt.close()


# ---- Run for all D vectors ----
if __name__ == "__main__":
    for i, D in enumerate(D_vectors, start=1):
        save_path = f"../figures/plot_new_{i}.png"
        check_and_plot(D, save_path)

