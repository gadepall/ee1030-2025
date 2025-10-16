import ctypes
import numpy as np
import matplotlib.pyplot as plt
import os

# --- C LIBRARY INTEGRATION ---

# Define a Python class that mirrors the C Point struct.
class Point(ctypes.Structure):
    _fields_ = [("x", ctypes.c_double),
                ("y", ctypes.c_double)]

# Load the shared C library.
# This assumes the compiled library is in the same directory.
lib_path = './circs.so'
if not os.path.exists(lib_path):
    print("Error: Shared library 'circs.so' not found.")
    print("Please compile the C code first with: gcc -shared -o libtangent.so -fPIC tangent_calc.c")
else:
    tangent_lib = ctypes.CDLL(lib_path)

    # Define the function signature for the tangent calculation function.
    calculate_tangents_c = tangent_lib.calculate_tangents
    calculate_tangents_c.argtypes = [ctypes.c_double, Point, ctypes.POINTER(Point), ctypes.POINTER(Point)]
    calculate_tangents_c.restype = None

    # --- PROBLEM SETUP AND C FUNCTION CALL ---

    # 1. Define the problem: circle of radius 5, point 8cm away.
    circle_radius = 5.0
    external_point_p = Point(8.0, 0.0)

    # Create empty Point structures to hold the results from the C function.
    tangent_point_t1 = Point()
    tangent_point_t2 = Point()

    # 2. Call the C function to perform the calculation.
    calculate_tangents_c(
        circle_radius,
        external_point_p,
        ctypes.byref(tangent_point_t1),
        ctypes.byref(tangent_point_t2)
    )

    # 3. Print the results calculated by the C code.
    print(f"Results from C function:")
    print(f"Tangent Point 1 (T1): ({tangent_point_t1.x:.4f}, {tangent_point_t1.y:.4f})")
    print(f"Tangent Point 2 (T2): ({tangent_point_t2.x:.4f}, {tangent_point_t2.y:.4f})")


    # --- PLOTTING ---

    # Helper function to generate circle points.
    def circ_gen(center, r):
        theta = np.linspace(0, 2 * np.pi, 100)
        x = center[0] + r * np.cos(theta)
        y = center[1] + r * np.sin(theta)
        return x, y

    # Generate circle for plotting.
    x_circ, y_circ = circ_gen([0, 0], circle_radius)

    # Plot the circle.
    plt.plot(x_circ, y_circ, label='Circle: $x^2 + y^2 = 25$')

    # Plot the key points.
    plt.scatter([0], [0], color='black', label='Center O(0,0)')
    plt.scatter([external_point_p.x], [external_point_p.y], color='red', label=f'External Point P({external_point_p.x:.0f}, {external_point_p.y:.0f})')
    plt.scatter([tangent_point_t1.x, tangent_point_t2.x], [tangent_point_t1.y, tangent_point_t2.y], color='green', label='Tangent Points')

    # Plot the tangent lines.
    plt.plot([external_point_p.x, tangent_point_t1.x], [external_point_p.y, tangent_point_t1.y], 'r--')
    plt.plot([external_point_p.x, tangent_point_t2.x], [external_point_p.y, tangent_point_t2.y], 'r--', label='Tangents')

    # Annotate points for clarity.
    plt.text(tangent_point_t1.x + 0.5, tangent_point_t1.y, f'T1 ({tangent_point_t1.x:.2f}, {tangent_point_t1.y:.2f})')
    plt.text(tangent_point_t2.x + 0.5, tangent_point_t2.y - 0.5, f'T2 ({tangent_point_t2.x:.2f}, {tangent_point_t2.y:.2f})')

    # Configure and show the plot.
    plt.title('Construction of Tangents to a Circle (C + Python)')
    plt.xlabel('x-axis')
    plt.ylabel('y-axis')
    plt.gca().set_aspect('equal', adjustable='box')
    plt.grid(True)
    plt.legend()
    plt.show()


