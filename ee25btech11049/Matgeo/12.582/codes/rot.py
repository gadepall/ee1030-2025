import ctypes
import os
import matplotlib.pyplot as plt
from matplotlib.patches import Arc
import numpy as np # Required for the plotting function

# Define a Python class that mirrors the C 'Point' struct.
# This tells ctypes how to interpret the block of memory.
class Point(ctypes.Structure):
    _fields_ = [("x", ctypes.c_double),
                ("y", ctypes.c_double)]

def plot_rotation(p, q, angle_degrees):
    """
    Generates a plot to visualize the rotation of point P to Q.
    Args:
        p (tuple): The original (x, y) coordinates.
        q (tuple): The rotated (x, y) coordinates.
        angle_degrees (float): The angle of rotation.
    """
    fig, ax = plt.subplots(figsize=(8, 8))

    # Plot origin
    ax.plot(0, 0, 'ko', markersize=10, label='Origin (O)')

    # Create formatted strings for the labels
    p_label = f'({p[0]:.2f}, {p[1]:.2f})'
    q_label = f'({q[0]:.2f}, {q[1]:.2f})'

    # Plot vectors and points
    # Vector OP
    ax.arrow(0, 0, p[0], p[1], head_width=0.5, head_length=0.7, fc='blue', ec='blue', length_includes_head=True)
    ax.plot(p[0], p[1], 'bo', markersize=8, label=f'Point P {p_label}')
    ax.text(p[0] + 0.5, p[1] + 0.5, f'P {p_label}', fontsize=12, color='blue')

    # Vector OQ
    ax.arrow(0, 0, q[0], q[1], head_width=0.5, head_length=0.7, fc='red', ec='red', length_includes_head=True)
    ax.plot(q[0], q[1], 'ro', markersize=8, label=f'Point Q {q_label}')
    ax.text(q[0] + 0.5, q[1] + 0.5, f'Q {q_label}', fontsize=12, color='red')

    # Add the rotation arc
    radius = np.linalg.norm(p)
    angle_p_rad = np.arctan2(p[1], p[0])
    angle_p_deg = np.degrees(angle_p_rad)
    arc = Arc((0, 0), radius*0.5, radius*0.5, angle=0,
              theta1=angle_p_deg, theta2=angle_p_deg + angle_degrees,
              color='green', linewidth=2, linestyle='--')
    ax.add_patch(arc)
    theta_label_rad = np.radians(angle_p_deg + angle_degrees / 2)
    ax.text(radius*0.3 * np.cos(theta_label_rad), radius*0.3 * np.sin(theta_label_rad),
            f'θ={angle_degrees}°', fontsize=12, color='green')

    # Set up the plot aesthetics
    ax.axhline(0, color='black',linewidth=0.5)
    ax.axvline(0, color='black',linewidth=0.5)
    ax.grid(True, which='both', linestyle='--', linewidth=0.5)
    ax.set_aspect('equal', adjustable='box')
    ax.set_title('2D Vector Rotation (using C function)', fontsize=16)
    ax.set_xlabel('X-axis', fontsize=12)
    ax.set_ylabel('Y-axis', fontsize=12)

    max_val = max(abs(p[0]), abs(p[1]), abs(q[0]), abs(q[1])) * 1.2
    ax.set_xlim(-5, max_val)
    ax.set_ylim(-5, max_val)

    ax.legend()
    plt.show()

# --- Main execution block ---
if __name__ == "__main__":
    # Determine the correct shared library file extension based on the operating system
    if os.name == 'nt': # For Windows
        lib_name = 'rotate_vector.dll'
    else: # For Linux, macOS, etc.
        lib_name = 'rot.so'
    
    # Construct the full path to the library file, assuming it's in the same directory
    lib_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), lib_name)

    try:
        # Load the compiled C code as a shared library
        c_lib = ctypes.CDLL(lib_path)
    except OSError as e:
        print(f"Error: Could not load the shared library '{lib_name}'.")
        print(f"Details: {e}")
        print("\nPlease compile the C code first. See README.md for instructions.")
        exit()

    # Get a handle to the 'rotate_point_c' function inside the library
    rotate_point_c = c_lib.rotate_point_c
    
    # Define the function's signature for ctypes
    rotate_point_c.argtypes = [ctypes.POINTER(Point), ctypes.c_double]
    rotate_point_c.restype = None

    # --- Use the C function ---
    p = Point(x=20.0, y=10.0)
    theta = 30.0

    # Store the original coordinates before they are modified, for plotting
    p_original_coords = (p.x, p.y)

    print(f"Original point P: ({p.x}, {p.y})")
    print(f"Rotation angle: {theta}°")
    
    # Call the C function. This modifies the 'p' object in place.
    rotate_point_c(ctypes.byref(p), theta)

    # Store the new coordinates for printing and plotting
    q_rotated_coords = (p.x, p.y)

    print(f"New point Q (calculated by C): ({q_rotated_coords[0]:.2f}, {q_rotated_coords[1]:.2f})")

    # --- Visualize the result ---
    plot_rotation(p_original_coords, q_rotated_coords, theta)


