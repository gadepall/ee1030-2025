import ctypes
import os
import numpy as np
from subprocess import run, PIPE
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# --- Step 1: Compile the C code ---
C_FILE = 'system.c'
os.name == 'posix'
LIB_FILE = './system.so'
compile_cmd = ['gcc', '-shared', '-o', LIB_FILE, C_FILE, '-fPIC', '-lm']

print(f"Attempting to compile C file: {C_FILE}")
compile_result = run(compile_cmd, stderr=PIPE)

if compile_result.returncode != 0:
    print("C Compilation Error:")
    print(compile_result.stderr.decode())
    exit()
print(f"Successfully compiled {C_FILE} to {LIB_FILE}")

# --- Step 2: Load the compiled library and define types ---
try:
    lib = ctypes.CDLL(os.path.abspath(LIB_FILE)) # Use absolute path for robustness
except OSError as e:
    print(f"Error loading {LIB_FILE}. Error: {e}")
    exit()

# Define C types for the 3x4 array argument (double matrix[3][4])
c_double_ptr = ctypes.POINTER(ctypes.c_double)
lib.solve_system_c.argtypes = [c_double_ptr]
lib.solve_system_c.restype = ctypes.c_int

# --- Step 3: Prepare the data for the system with lambda = 1 ---
# Original Augmented Matrix [A|B] for lambda=1
# R1: 2x - y + 2z = 2
# R2: x - 2y + z = -4
# R3: x + y + 1z = 4
matrix_np = np.array([
    [2.0, -1.0, 2.0, 2.0],
    [1.0, -2.0, 1.0, -4.0],
    [1.0, 1.0, 1.0, 4.0]
], dtype=np.float64)

# Create a copy to pass to C, as C function might modify it in-place
matrix_for_c = matrix_np.copy() 
matrix_c_ptr = matrix_for_c.ctypes.data_as(c_double_ptr)

# --- Step 4: Call the C function and interpret the result ---
print("\n--- Running C Code (Gaussian Elimination) ---")
result_code = lib.solve_system_c(matrix_c_ptr)

print(f"System tested with lambda = 1.")
if result_code == 0:
    print("C Function Output: NO SOLUTION (Inconsistent System)")
    plot_required = True
elif result_code == 1:
    print("C Function Output: Solvable (Consistent System)")
    plot_required = False # Only plot if there's no solution for this problem
else:
    print("C Function Output: Unknown result code.")
    plot_required = False

print("\nFinal Matrix after C Gaussian Elimination:")
print(matrix_for_c) # Shows the modified matrix from C

# --- Step 5: Plot the graph if 'No Solution' is found ---
if plot_required:
    print("\n--- Generating 3D Plot of Planes ---")
    fig = plt.figure(figsize=(10, 8))
    ax = fig.add_subplot(111, projection='3d')

    # Define the range for x and y
    x_range = np.linspace(-5, 5, 20)
    y_range = np.linspace(-5, 5, 20)
    X, Y = np.meshgrid(x_range, y_range)

    # Calculate z for each plane from original equations
    # P1: 2x - y + 2z = 2  => z = (2 - 2x + y) / 2
    Z1 = (2 - 2*X + Y) / 2
    
    # P2: x - 2y + z = -4 => z = -4 - x + 2y
    Z2 = -4 - X + 2*Y

    # P3: x + y + z = 4  => z = 4 - x - y
    Z3 = 4 - X - Y

    # Plot the planes
    # Note: plot_surface does not directly support 'label' for legend.
    # We will approximate or add dummy plots for legend.
    ax.plot_surface(X, Y, Z1, alpha=0.5, color='cyan', rstride=100, cstride=100)
    ax.plot_surface(X, Y, Z2, alpha=0.5, color='red', rstride=100, cstride=100)
    ax.plot_surface(X, Y, Z3, alpha=0.5, color='yellow', rstride=100, cstride=100)

    # Create dummy plots for legend
    ax.plot([], [], [], color='cyan', label='Plane 1: $2x - y + 2z = 2$')
    ax.plot([], [], [], color='red', label='Plane 2: $x - 2y + z = -4$')
    ax.plot([], [], [], color='yellow', label='Plane 3: $x + y + z = 4$')


    # Customize the plot appearance
    ax.set_xlabel('X-axis')
    ax.set_ylabel('Y-axis')
    ax.set_zlabel('Z-axis')
    ax.set_title('Planes for Inconsistent System ($\lambda=1$)')
    ax.legend()
    
    # Set view to better show the "no intersection" or "triangular tunnel"
    ax.view_init(elev=20, azim=-45) 
    ax.set_xlim([-5, 5])
    ax.set_ylim([-5, 5])
    ax.set_zlim([-5, 10]) # Adjust z-limits as needed for better visualization

    plt.savefig("/media/indhiresh-s/New Volume/Matrix/ee1030-2025/ee25btech11027/MATGEO/5.13.53/figs/figure1.png")
    plt.show()

