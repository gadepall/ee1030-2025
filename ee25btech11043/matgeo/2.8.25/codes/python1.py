import ctypes
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# Load the shared library
lib_angles = ctypes.CDLL("./code4.so")

# Define the argument types and return type for the C function
# The function takes 9 doubles (for A, B, C components) and a pointer to a double array (for results)
lib_angles.calculate_angles_cosines.argtypes = [
    ctypes.c_double, ctypes.c_double, ctypes.c_double, # A_x, A_y, A_z
    ctypes.c_double, ctypes.c_double, ctypes.c_double, # B_x, B_y, B_z
    ctypes.c_double, ctypes.c_double, ctypes.c_double, # C_x, C_y, C_z
    ctypes.POINTER(ctypes.c_double * 3)                # Pointer to an array of 3 doubles for results
]
lib_angles.calculate_angles_cosines.restype = None

# Define mutually perpendicular vectors of equal magnitude
# Example: unit vectors along axes
A = np.array([1.0, 0.0, 0.0])
B = np.array([0.0, 1.0, 0.0])
C = np.array([0.0, 0.0, 1.0])

# Another example: scaled vectors
# magnitude = 5.0
# A = np.array([magnitude, 0.0, 0.0])
# B = np.array([0.0, magnitude, 0.0])
# C = np.array([0.0, 0.0, magnitude])

# Resultant vector R = A + B + C
R = A + B + C

# Create a C array to hold the three cosine results
cos_angles_c_array = (ctypes.c_double * 3)()

# Call the C function
lib_angles.calculate_angles_cosines(
    A[0], A[1], A[2],
    B[0], B[1], B[2],
    C[0], C[1], C[2],
    ctypes.byref(cos_angles_c_array)
)

# Retrieve the results from the C array
cos_theta_RA = cos_angles_c_array[0]
cos_theta_RB = cos_angles_c_array[1]
cos_theta_RC = cos_angles_c_array[2]

# Convert cosines to angles in degrees
theta_RA_deg = np.degrees(np.arccos(cos_theta_RA))
theta_RB_deg = np.degrees(np.arccos(cos_theta_RB))
theta_RC_deg = np.degrees(np.arccos(cos_theta_RC))

print(f"Vectors A = {A}, B = {B}, C = {C}")
print(f"Resultant vector R = A + B + C = {R}")
print("\n--- Angles calculated via C shared library ---")
print(f"Cosine of angle between R and A: {cos_theta_RA:.6f}")
print(f"Angle between R and A: {theta_RA_deg:.2f} degrees")
print(f"Cosine of angle between R and B: {cos_theta_RB:.6f}")
print(f"Angle between R and B: {theta_RB_deg:.2f} degrees")
print(f"Cosine of angle between R and C: {cos_theta_RC:.6f}")
print(f"Angle between R and C: {theta_RC_deg:.2f} degrees")

if np.isclose(theta_RA_deg, theta_RB_deg) and np.isclose(theta_RB_deg, theta_RC_deg):
    print("\nConclusion: The angles are approximately equal, showing that A+B+C is equally inclined to A, B, and C.")
else:
    print("\nConclusion: The angles are not equal. There might be an issue with the input vectors or calculation.")


# --- Visualization ---
fig = plt.figure(figsize=(10, 8))
ax = fig.add_subplot(111, projection='3d')

origin = [0, 0, 0]

# Plot vectors A, B, C
ax.quiver(*origin, *A, color='r', linewidth=2, arrow_length_ratio=0.1, label='Vector A')
ax.quiver(*origin, *B, color='g', linewidth=2, arrow_length_ratio=0.1, label='Vector B')
ax.quiver(*origin, *C, color='b', linewidth=2, arrow_length_ratio=0.1, label='Vector C')

# Plot resultant vector R
ax.quiver(*origin, *R, color='purple', linewidth=3, arrow_length_ratio=0.08, label='Vector A+B+C')

# Set labels and title
ax.set_xlabel('X-axis')
ax.set_ylabel('Y-axis')
ax.set_zlabel('Z-axis')
ax.set_title('Mutually Perpendicular Vectors and Their Sum')
ax.legend()

# Set limits for a better view
max_coord = max(np.max(np.abs(A)), np.max(np.abs(B)), np.max(np.abs(C)), np.max(np.abs(R))) * 1.2
ax.set_xlim([-max_coord, max_coord])
ax.set_ylim([-max_coord, max_coord])
ax.set_zlim([-max_coord, max_coord])

# Add grid
ax.grid(True)

plt.show()
