import ctypes
import numpy as np
import matplotlib.pyplot as plt
import os

def solve_and_plot_ctypes():
    """
    Calls a C shared library to get eigenvectors and plots the result.
    """
    print("--- 3. Python with C Library Solution ---")

    # Path to the shared library
    lib_path = './eigen.so'

    # Load the shared library
    eigen_lib = ctypes.CDLL(lib_path)

    # Define the function signature (argument types and return type)
    eigen_lib.get_eigenvectors.argtypes = [
        np.ctypeslib.ndpointer(dtype=np.float64, ndim=2, shape=(2,2)),
        np.ctypeslib.ndpointer(dtype=np.float64, ndim=1, shape=(2,)),
        np.ctypeslib.ndpointer(dtype=np.float64, ndim=1, shape=(2,)),
        np.ctypeslib.ndpointer(dtype=np.float64, ndim=1, shape=(2,))
    ]
    eigen_lib.get_eigenvectors.restype = None

    # Prepare data
    A = np.array([[4, 3], [9, -2]], dtype=np.float64)
    eigenvalues = np.array([-5, 7], dtype=np.float64)
    
    # Create empty arrays for the output
    vec1 = np.zeros(2, dtype=np.float64)
    vec2 = np.zeros(2, dtype=np.float64)

    # Call the C function
    eigen_lib.get_eigenvectors(A, eigenvalues, vec1, vec2)

    print("Matrix A:\n", A)
    print("\nResults from C library:")
    print(f"Eigenvector for λ = {eigenvalues[0]}: {vec1}")
    print(f"Eigenvector for λ = {eigenvalues[1]}: {vec2}")

    # --- Plotting (identical to native Python) ---
    v1_plot = np.array([1, 1])
    v2_plot = np.array([2, -6])
    v_other = np.array([3, 4])
    Av1 = A @ v1_plot
    Av2 = A @ v2_plot
    Av_other = A @ v_other
    
    fig, ax = plt.subplots(figsize=(10, 10))

    ax.quiver(0, 0, v1_plot[0], v1_plot[1], angles='xy', scale_units='xy', scale=1, color='blue', label='Eigenvector $\\vec{v_1}$ for $\\lambda=7$')
    ax.quiver(0, 0, Av1[0], Av1[1], angles='xy', scale_units='xy', scale=1, color='cyan', alpha=0.8, label='$A\\vec{v_1}$')
    ax.quiver(0, 0, v2_plot[0], v2_plot[1], angles='xy', scale_units='xy', scale=1, color='red', label='Eigenvector $\\vec{v_2}$ for $\\lambda=-5$')
    ax.quiver(0, 0, Av2[0], Av2[1], angles='xy', scale_units='xy', scale=1, color='magenta', alpha=0.8, label='$A\\vec{v_2}$')
    ax.quiver(0, 0, v_other[0], v_other[1], angles='xy', scale_units='xy', scale=1, color='green', label='Non-Eigenvector $\\vec{v_3}$')
    ax.quiver(0, 0, Av_other[0], Av_other[1], angles='xy', scale_units='xy', scale=1, color='lime', alpha=0.8, label='$A\\vec{v_3}$')

    ax.set_xlim([-15, 30]); ax.set_ylim([-20, 35])
    ax.set_xlabel("X-axis"); ax.set_ylabel("Y-axis")
    ax.set_title("Figure")
    ax.axhline(0, color='grey', lw=0.5); ax.axvline(0, color='grey', lw=0.5)
    ax.grid(True); ax.set_aspect('equal', adjustable='box'); ax.legend()
    
    plt.savefig("/media/indhiresh-s/New Volume/Matrix/ee1030-2025/ee25btech11027/MATGEO/12.41/figs/figure1.png")
    plt.show()
if __name__ == '__main__':
    solve_and_plot_ctypes()
