import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import ctypes
import os

# --- Ctypes Setup ---

# Define the Vector3D structure to match the C definition
class Vector3D(ctypes.Structure):
    _fields_ = [
        ("x", ctypes.c_double),
        ("y", ctypes.c_double),
        ("z", ctypes.c_double)
    ]

# Load the shared library


lib = ctypes.CDLL('./2.8.24.so')




# Define the argument types and return types for the C functions
# For vector_magnitude: takes Vector3D, returns double
lib.vector_magnitude.argtypes = [Vector3D]
lib.vector_magnitude.restype = ctypes.c_double

# For does_sum_bisect_angle: takes two Vector3D, returns int
lib.does_sum_bisect_angle.argtypes = [Vector3D, Vector3D]
lib.does_sum_bisect_angle.restype = ctypes.c_int

# --- Python Helper Functions (using numpy where appropriate for plotting) ---

def angle_between_vectors_np(v1_np, v2_np):
    """Calculates the angle in degrees between two numpy vectors."""
    mag1 = np.linalg.norm(v1_np)
    mag2 = np.linalg.norm(v2_np)

    if mag1 == 0 or mag2 == 0:
        return np.nan # Undefined angle with a zero vector

    dot_product = np.dot(v1_np, v2_np)
    cos_theta = np.clip(dot_product / (mag1 * mag2), -1.0, 1.0)
    angle_rad = np.arccos(cos_theta)
    return np.degrees(angle_rad)

def plot_vector_bisection_ctypes(a_np, b_np, title_suffix=""):
    """
    Plots vectors a, b, and a+b in 3D and displays angle bisection information.
    Uses C functions via ctypes for magnitude calculation and bisection check.
    """
    fig = plt.figure(figsize=(10, 8))
    ax = fig.add_subplot(111, projection='3d')

    origin = np.array([0, 0, 0])

    # Calculate sum vector using numpy
    sum_vec_np = a_np + b_np

    # Plot vectors
    ax.quiver(*origin, *a_np, color='r', arrow_length_ratio=0.1, label='Vector a')
    ax.quiver(*origin, *b_np, color='g', arrow_length_ratio=0.1, label='Vector b')
    ax.quiver(*origin, *sum_vec_np, color='b', arrow_length_ratio=0.1, label='Vector a + b')

    # Convert numpy arrays to ctypes Vector3D structures for C function calls
    ctypes_a = Vector3D(x=a_np[0], y=a_np[1], z=a_np[2])
    ctypes_b = Vector3D(x=b_np[0], y=b_np[1], z=b_np[2])
    ctypes_sum_vec = Vector3D(x=sum_vec_np[0], y=sum_vec_np[1], z=sum_vec_np[2])

    # Calculate magnitudes using the C function
    mag_a_c = lib.vector_magnitude(ctypes_a)
    mag_b_c = lib.vector_magnitude(ctypes_b)
    mag_sum_c = lib.vector_magnitude(ctypes_sum_vec)

    # Calculate angles using numpy for clarity in visualization
    angle_a_sum = angle_between_vectors_np(a_np, sum_vec_np)
    angle_b_sum = angle_between_vectors_np(b_np, sum_vec_np)
    angle_a_b = angle_between_vectors_np(a_np, b_np)

    # Set plot limits
    max_coord = np.max(np.abs([a_np, b_np, sum_vec_np])) * 1.2
    ax.set_xlim([-max_coord, max_coord])
    ax.set_ylim([-max_coord, max_coord])
    ax.set_zlim([-max_coord, max_coord])

    ax.set_xlabel('X-axis')
    ax.set_ylabel('Y-axis')
    ax.set_zlabel('Z-axis')

    # Add text for magnitudes and angles
    info_text = f"Magnitudes (from C):\n||a|| = {mag_a_c:.6f}\n||b|| = {mag_b_c:.6f}\n"
    info_text += f"Angles (deg, from Python):\nAngle(a, a+b) = {angle_a_sum:.2f}\nAngle(b, a+b) = {angle_b_sum:.2f}\n"
    info_text += f"Angle(a, b) = {angle_a_b:.2f}\n"

    # Check for bisection condition using the C function
    is_bisected_c = lib.does_sum_bisect_angle(ctypes_a, ctypes_b)

    if is_bisected_c:
        info_text += "\nResult (from C): Magnitudes are equal (within EPSILON),\n so a+b bisects the angle (alpha ~ beta)."
        fig_title = "Angle Bisected (Rhombus Case)"
    else:
        info_text += "\nResult (from C): Magnitudes are NOT equal,\n so a+b does NOT bisect the angle."
        fig_title = "Angle Not Bisected (Parallelogram Case)"

    ax.set_title(f"{fig_title} {title_suffix}\n{info_text}", loc='left', fontsize=10)
    ax.legend()
    plt.tight_layout()
    plt.show()

# --- Test Cases ---

print("--- Case 1: Magnitudes are equal (Expected from C: Bisects) ---")
a1 = np.array([1.0, 2.0, 0.0])
b1 = np.array([2.0, -1.0, 0.0])
# ||a1|| = sqrt(1^2 + 2^2) = sqrt(5)
# ||b1|| = sqrt(2^2 + (-1)^2) = sqrt(5)
plot_vector_bisection_ctypes(a1, b1, "(a=[1,2,0], b=[2,-1,0])")

print("\n--- Case 2: Magnitudes are different (Expected from C: Does NOT Bisect) ---")
a2 = np.array([3.0, 0.0, 0.0]) # Mag = 3
b2 = np.array([1.0, 1.0, 0.0]) # Mag = sqrt(2) approx 1.414
plot_vector_bisection_ctypes(a2, b2, "(a=[3,0,0], b=[1,1,0])")


