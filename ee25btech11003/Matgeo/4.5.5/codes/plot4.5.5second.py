import ctypes
import os
import platform
import subprocess
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# --- Part 1: Compile and Load C Library using ctypes ---

def compile_c_library():
    """Compiles the C source file into a shared library."""
    c_file = "line_lib.c"
    if not os.path.exists(c_file):
        print(f"Error: C source file '{c_file}' not found.")
        print("Please create it with the C function code.")
        return None, None

    # Determine the output library name based on the operating system
    system = platform.system()
    if system == "Windows":
        lib_name = "line_lib.dll"
        compile_command = ["gcc", "-shared", "-o", lib_name, c_file]
    else: # Linux, macOS
        lib_name = "line_lib.so"
        compile_command = ["gcc", "-shared", "-o", lib_name, "-fPIC", c_file]

    print(f"Compiling C library: {' '.join(compile_command)}")
    try:
        subprocess.run(compile_command, check=True)
        print("Compilation successful.")
        return lib_name
    except (subprocess.CalledProcessError, FileNotFoundError) as e:
        print(f"Error during C compilation: {e}")
        print("Please ensure you have a C compiler (like GCC) installed and in your system's PATH.")
        return None


# Compile the library
lib_file = compile_c_library()

if lib_file:
    # --- 2. Define the Line's Data ---
    # Base point h = (1, -2, 3)
    h = np.array([1.0, -2.0, 3.0])
    # Direction vector m = <3, -2, 6>
    m = np.array([3.0, -2.0, 6.0])

    # --- 3. Call the C function from Python ---
    try:
        # Load the shared library
        line_lib = ctypes.CDLL(os.path.abspath(lib_file))

        # Get a reference to the C function
        c_print_parametric_form = line_lib.printParametricForm

        # Define the argument types for the C function (all are C doubles)
        c_print_parametric_form.argtypes = [
            ctypes.c_double, ctypes.c_double, ctypes.c_double,
            ctypes.c_double, ctypes.c_double, ctypes.c_double
        ]

        # Call the C function with our data
        c_print_parametric_form(h[0], h[1], h[2], m[0], m[1], m[2])

    except Exception as e:
        print(f"An error occurred while using the C library: {e}")


    # --- Part 2: Plotting the line using Matplotlib ---

    print("Generating 3D plot using Python...")

    # --- 1. Setup for the Plot ---
    fig = plt.figure(figsize=(10, 8))
    ax = fig.add_subplot(111, projection='3d')

    # --- 2. Define Line for Plotting ---
    t_range = 20
    t = np.linspace(-t_range, t_range, 200)

    # Parametric equations for the line
    x_coords = h[0] + m[0] * t
    y_coords = h[1] + m[1] * t
    z_coords = h[2] + m[2] * t

    # --- 3. Plot the Components ---
    ax.plot(x_coords, y_coords, z_coords, color='blue', linewidth=3, label='Line: $\\mathbf{x} = \\mathbf{h} + t\\mathbf{m}$')
    ax.scatter(h[0], h[1], h[2], color='red', s=150, label='Point $\\mathbf{h}$ (1, -2, 3)', depthshade=True)
    ax.quiver(h[0], h[1], h[2],
              m[0], m[1], m[2],
              color='green', arrow_length_ratio=0.15, linewidth=2, label='Direction vector $\\mathbf{m}$',
              length=np.linalg.norm(m) * 1.5)

    # --- 4. Finalize the Plot ---
    ax.set_xlabel('X-axis', fontsize=12)
    ax.set_ylabel('Y-axis', fontsize=12)
    ax.set_zlabel('Z-axis', fontsize=12)
    ax.set_title('3D Plot of the Vector Equation of a Line (Extended)', fontsize=14)
    ax.grid(True)
    ax.view_init(elev=20, azim=-60)
    ax.legend(fontsize=10, loc='lower right')
    plt.tight_layout()
    plt.show()

