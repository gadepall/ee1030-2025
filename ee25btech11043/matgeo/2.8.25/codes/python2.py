import numpy as np
import numpy.linalg as LA
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D # For 3D plotting

# --- 1. Define vectors A, B, C ---
# Mutually perpendicular vectors of equal magnitude
# Example 1: Standard basis vectors scaled
magnitude = 3.0 # You can change the magnitude
A = np.array([magnitude, 0.0, 0.0])
B = np.array([0.0, magnitude, 0.0])
C = np.array([0.0, 0.0, magnitude])

# Example 2: Another set of mutually perpendicular vectors
# A = np.array([2.0, 0.0, 0.0])
# B = np.array([0.0, -2.0, 0.0])
# C = np.array([0.0, 0.0, 2.0])


print(f"Given Vectors:")
print(f"A = {A}")
print(f"B = {B}")
print(f"C = {C}")

# Verify mutual perpendicularity and equal magnitude (optional, for self-check)
print("\nVerification (optional):")
print(f"A . B = {np.dot(A, B)}")
print(f"A . C = {np.dot(A, C)}")
print(f"B . C = {np.dot(B, C)}")
print(f"|A| = {LA.norm(A)}")
print(f"|B| = {LA.norm(B)}")
print(f"|C| = {LA.norm(C)}")


# --- 2. Calculate the resultant vector R = A + B + C ---
R = A + B + C
print(f"\nResultant vector R = A + B + C = {R}")


# --- 3. Calculate angles using dot products ---
# Function to calculate angle between two vectors
def angle_between_vectors(v1, v2):
    dot_product = np.dot(v1, v2)
    magnitude_v1 = LA.norm(v1)
    magnitude_v2 = LA.norm(v2)

    # Handle potential division by zero for zero vectors
    if magnitude_v1 < 1e-9 or magnitude_v2 < 1e-9:
        if magnitude_v1 < 1e-9 and magnitude_v2 < 1e-9:
            return 0.0 # Both are zero, angle is 0
        else:
            return np.pi / 2 # One is zero, other non-zero, angle is 90 degrees (pi/2 radians)

    cosine_angle = dot_product / (magnitude_v1 * magnitude_v2)
    # Ensure cosine_angle is within [-1, 1] due to potential floating point inaccuracies
    cosine_angle = np.clip(cosine_angle, -1.0, 1.0)
    return np.arccos(cosine_angle) # Returns angle in radians

# Calculate angles
angle_RA_rad = angle_between_vectors(R, A)
angle_RB_rad = angle_between_vectors(R, B)
angle_RC_rad = angle_between_vectors(R, C)

angle_RA_deg = np.degrees(angle_RA_rad)
angle_RB_deg = np.degrees(angle_RB_rad)
angle_RC_deg = np.degrees(angle_RC_rad)


# --- 4. Print the results ---
print("\n--- Calculated Angles ---")
print(f"Angle between R and A: {angle_RA_deg:.2f} degrees")
print(f"Angle between R and B: {angle_RB_deg:.2f} degrees")
print(f"Angle between R and C: {angle_RC_deg:.2f} degrees")

# Conclusion
if np.isclose(angle_RA_deg, angle_RB_deg) and np.isclose(angle_RB_deg, angle_RC_deg):
    print("\nConclusion: The angles are approximately equal. This shows that A+B+C is equally inclined to A, B, and C.")
else:
    print("\nConclusion: The angles are not equal. Please check the input vectors to ensure they are mutually perpendicular and have equal magnitudes.")


# --- 5. Generate a 3D plot to visualize these vectors ---
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
# Automatically adjust limits based on vector magnitudes
all_coords = np.concatenate((A, B, C, R))
max_coord = np.max(np.abs(all_coords)) * 1.2 # Add some padding
ax.set_xlim([-max_coord, max_coord])
ax.set_ylim([-max_coord, max_coord])
ax.set_zlim([-max_coord, max_coord])

# Add grid
ax.grid(True)

plt.savefig("fig2.png")
plt.show()

print("\nFigure saved as fig2.png")
