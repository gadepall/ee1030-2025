import ctypes
import numpy as np
import matplotlib.pyplot as plt

# --- Setup and Library Loading ---
# This will now raise an error and stop the script if 'verifier.so' isn't found.
# Ensure you have compiled it first with:
# gcc -shared -o verifier.so -fPIC verifier.c
lib_name = 'verifier.so'
verifier_lib = ctypes.CDLL(f'./{lib_name}')
check_point = verifier_lib.check_point_on_conic
check_point.argtypes = [ctypes.c_double, ctypes.c_double]
check_point.restype = ctypes.c_double

# Define the points to check
vertex = (0.0, 0.0)
point_on_curve = (2.0, 3.0)

# Check 1: Vertex
is_vertex_on_curve = np.isclose(check_point(vertex[0], vertex[1]), 0)
if is_vertex_on_curve:
    print(f"PASSED: The vertex {vertex} is on the curve.")
else:
    print(f"FAILED: The vertex {vertex} is NOT on the curve.")

# Check 2: Point (2, 3)
is_point_on_curve = np.isclose(check_point(point_on_curve[0], point_on_curve[1]), 0)
if is_point_on_curve:
    print(f"PASSED: The point {point_on_curve} is on the curve.")
else:
    print(f"FAILED: The point {point_on_curve} is NOT on the curve.")

# --- Plotting Section ---
# This block only runs if both checks passed
if is_vertex_on_curve and is_point_on_curve:
    print("\nAll conditions verified successfully.")
    
    # From the equation y^2 = (9/2)x, we know 4a = 9/2, so a = 9/8
    a = 9.0 / 8.0
    focus = (a, 0)

    # Generate points for the parabola: x = (2/9) * y^2
    # Increased point density for a smoother curve
    y_vals = np.linspace(-10, 10, 1500)
    x_vals = (2.0 / 9.0) * y_vals**2

    # Create the plot
    plt.figure(figsize=(10, 8))
    # Increased line width for better visibility
    plt.plot(x_vals, y_vals, label='Parabola: $2y^2 - 9x = 0$', linewidth=2)
    
    # Plot and label the key points with a smaller size
    plt.scatter(*vertex, color='red', s=50, zorder=5, label=f'Vertex: {vertex}')
    plt.scatter(*focus, color='green', s=50, zorder=5, label=f'Focus: ({a:.3f}, 0)')
    plt.scatter(*point_on_curve, color='purple', s=50, zorder=5, label=f'Point: {point_on_curve}')
    
    # Add text labels with coordinates next to the points for clarity
    plt.text(vertex[0] - 1.2, vertex[1], f'Vertex\n{vertex}')
    plt.text(focus[0] + 0.2, focus[1] + 0.2, f'Focus\n({focus[0]:.2f}, {focus[1]:.2f})')
    plt.text(point_on_curve[0] + 0.2, point_on_curve[1] + 0.2, f'Point\n{point_on_curve}')
    
    # Style the plot
    plt.title('Analysis of the Parabola $2y^2 - 9x = 0$')
    plt.xlabel('X-axis')
    plt.ylabel('Y-axis')
    plt.axhline(0, color='black', linewidth=0.5)
    plt.axvline(0, color='black', linewidth=0.5)
    plt.grid(True, linestyle='--', alpha=0.6)
    plt.legend()
    plt.axis('equal')
    plt.show()

