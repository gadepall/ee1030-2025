import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import ctypes
from numpy.ctypeslib import ndpointer

# This script uses the compiled C library 'vector_lib.so' 
# to calculate the unit vector.
#
# Before running this script, you must compile the C code by running
# the following command in your terminal:
# python setup.py build_ext --inplace

try:
    # --- 1. Load the C Shared Library ---
    # This loads the .so (Linux/macOS) or .dll (Windows) file.
    vector_lib = ctypes.CDLL('./vector_lib.so') 
    
    # --- 2. Define the C function's argument and return types ---
    # This tells Python how to correctly call the C function.
    calculate_unit_vector_c = vector_lib.calculate_unit_vector_c
    calculate_unit_vector_c.restype = None  # The C function returns void
    calculate_unit_vector_c.argtypes = [
        ndpointer(dtype=np.float64, flags="C_CONTIGUOUS"), # Pointer to the input vector
        ctypes.c_int,                                     # Integer for the vector size
        ndpointer(dtype=np.float64, flags="C_CONTIGUOUS")  # Pointer to the output array
    ]

    # --- 3. Prepare data and call the C function ---
    from params import a_vector
    
    # Ensure the vector is a float64 numpy array for the C function
    a = a_vector.astype(np.float64)
    
    # Create an empty numpy array to store the result from C
    unit_a = np.zeros_like(a, dtype=np.float64)

    # Call the C function
    calculate_unit_vector_c(a, a.size, unit_a)

    # --- 4. Print and Plot the results ---
    magnitude_a = np.linalg.norm(a) # Calculate magnitude in Python for display

    print(f"Original vector a: {a}")
    print(f"Magnitude of a: {magnitude_a:.4f}")
    print(f"Unit vector â (from C library): {unit_a}")
    print(f"Magnitude of the unit vector: {np.linalg.norm(unit_a):.4f}")

    # Create the 3D plot
    fig = plt.figure(figsize=(10, 10))
    ax = fig.add_subplot(111, projection='3d')

    # Plot the original vector 'a' and the unit vector 'â'
    ax.quiver(0, 0, 0, a[0], a[1], a[2], color='b', arrow_length_ratio=0.1, label=f'Vector a = {a}')
    ax.quiver(0, 0, 0, unit_a[0], unit_a[1], unit_a[2], color='r', arrow_length_ratio=0.2, label=f'Unit Vector â ≈ [{unit_a[0]:.2f}, {unit_a[1]:.2f}, {unit_a[2]:.2f}]')

    # Configure and display the plot
    limit = max(np.max(np.abs(a)), 1.5)
    ax.set_xlim([-limit, limit]); ax.set_ylim([-limit, limit]); ax.set_zlim([0, limit])
    ax.set_title('Unit Vector in 3D (Calculated in C)', fontsize=16)
    ax.set_xlabel('x-axis'); ax.set_ylabel('y-axis'); ax.set_zlabel('z-axis')
    ax.legend(fontsize=12)
    ax.view_init(elev=20., azim=30)
    plt.grid(True)
    plt.show()

except FileNotFoundError:
    print("Error: Could not find 'vector_lib.so' or 'vector_lib.dll'.")
    print("Please ensure you have compiled the C library first by running this command in your terminal:")
    print("python setup.py build_ext --inplace")
except Exception as e:
    print(f"An unexpected error occurred: {e}")


