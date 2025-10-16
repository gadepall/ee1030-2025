import ctypes
import os
import sys
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.lines import Line2D

# Define a ctypes structure that mirrors the C Point struct
class Point(ctypes.Structure):
    _fields_ = [("x", ctypes.c_double),
                ("y", ctypes.c_double)]

def run_analytical_solver(plot_lib):
    """
    Calls the C function to solve for the area and vertices analytically.
    Returns the three vertices of the triangle.
    """
    print("\n--- Running Analytical Solver ---")
    
    # Define function signature
    plot_lib.calculate_area_with_matrices.argtypes = [
        ctypes.POINTER(Point),
        ctypes.POINTER(Point),
        ctypes.POINTER(Point)
    ]
    plot_lib.calculate_area_with_matrices.restype = ctypes.c_double

    # Create instances of the Point structure to hold the results
    p1 = Point()
    p2 = Point()
    p3 = Point()

    # Call the C function, passing pointers to the structs
    area = plot_lib.calculate_area_with_matrices(
        ctypes.byref(p1),
        ctypes.byref(p2),
        ctypes.byref(p3)
    )

    # Print the results calculated by the C code
    print(f"Vertex 1 (Intersection): ({p1.x:.2f}, {p1.y:.2f})")
    print(f"Vertex 2 (Intersection): ({p2.x:.2f}, {p2.y:.2f})")
    print(f"Vertex 3 (Corner):       ({p3.x:.2f}, {p3.y:.2f})")
    print(f"\nCalculated Area (using matrix/determinant method): {area:.4f}")
    print("---------------------------------")
    
    # Return the calculated vertices for plotting
    return p1, p2, p3


def create_final_plot(vertices):
    """
    Generates a clean, vector-based plot using Matplotlib based on the
    provided vertices, matching the style of the example PNG.
    """
    print("\n--- Generating Final Vector Plot ---")
    
    # Unpack and sort vertices by x-coordinate for consistent plotting
    # This makes v_left = (0,1), v_bottom = (1,0), v_right = (2,1)
    sorted_vertices = sorted(vertices, key=lambda p: p.x)
    v_left, v_bottom, v_right = sorted_vertices
    
    fig, ax = plt.subplots(figsize=(8, 7))

    # 1. Fill the area of the triangle
    ax.fill([v_left.x, v_bottom.x, v_right.x], 
            [v_left.y, v_bottom.y, v_right.y], 
            'lightblue', label='Bounded Area')

    # 2. Draw the boundary lines with specific colors
    ax.plot([v_left.x, v_bottom.x], [v_left.y, v_bottom.y], color='blue') # y = -x + 1
    ax.plot([v_bottom.x, v_right.x], [v_bottom.y, v_right.y], color='green') # y = x - 1
    ax.plot([v_left.x, v_right.x], [v_left.y, v_right.y], color='red') # y = 1
    
    # 3. Plot the vertices as black circles
    ax.scatter([v.x for v in vertices], [v.y for v in vertices], color='black', s=80, zorder=5)

    # 4. Set plot titles and labels
    ax.set_title("Area bounded by y = |x-1| and y = 1", fontsize=14)
    ax.set_xlabel("x-axis")
    ax.set_ylabel("y-axis")

    # 5. Set axis limits and grid
    ax.set_xlim(-0.2, 2.2)
    ax.set_ylim(-0.3, 1.3)
    ax.grid(True)
    ax.set_aspect('equal', adjustable='box') # Ensure slopes look correct

    # 6. Create a custom legend to match the example image
    legend_elements = [
        Line2D([0], [0], color='blue', lw=2, label='x + y = 1'),
        Line2D([0], [0], color='green', lw=2, label='x - y = 1'),
        Line2D([0], [0], color='red', lw=2, label='y = 1'),
        Line2D([0], [0], marker='o', color='w', label='Vertex A (1.00, 0.00)', markerfacecolor='black', markersize=8),
        Line2D([0], [0], marker='o', color='w', label='Vertex B (2.00, 1.00)', markerfacecolor='black', markersize=8),
        Line2D([0], [0], marker='o', color='w', label='Vertex C (0.00, 1.00)', markerfacecolor='black', markersize=8)
    ]
    ax.legend(handles=legend_elements, loc='center')

    plt.show()


def main():
    """Main function to load the C library, solve, and display the plot."""
    # --- Manually specify the path to the compiled C library ---
    # You must compile plot_generator.c into a shared library first.
    # On Linux/macOS: gcc -shared -o libplot_generator.so -fPIC plot_generator.c
    # On Windows:     gcc -shared -o plot_generator.dll plot_generator.c
    
    if sys.platform.startswith('win'):
        lib_name = "plot_generator.dll"
    else: # for linux and darwin
        lib_name = "area.so"
        
    lib_path = os.path.abspath(lib_name)

    if not os.path.exists(lib_path):
        print(f"Error: Shared library not found at '{lib_path}'")
        print("Please compile the C code first using the appropriate command for your OS.")
        sys.exit(1)

    try:
        plot_lib = ctypes.CDLL(lib_path)
    except OSError as e:
        print(f"Error loading shared library: {e}")
        sys.exit(1)

    # Get the vertices from the analytical C function
    vertices = run_analytical_solver(plot_lib)

    # Create the final plot using the calculated vertices
    create_final_plot(vertices)


if __name__ == "__main__":
    main()


