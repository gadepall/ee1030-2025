import ctypes
import math
import os
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# Load compiled C shared library
if os.name == "nt":
    lib = ctypes.CDLL("./direction.dll")  # Windows
else:
    lib = ctypes.CDLL("./direction.so")   # Linux/macOS

# Define Vector3 struct (same layout as in C)
class Vector3(ctypes.Structure):
    _fields_ = [("x", ctypes.c_double),
                ("y", ctypes.c_double),
                ("z", ctypes.c_double)]

# Function signatures
lib.fromDirectionCosines.argtypes = [ctypes.c_double, ctypes.c_double]
lib.fromDirectionCosines.restype = Vector3

lib.dotProduct.argtypes = [Vector3, Vector3]
lib.dotProduct.restype = ctypes.c_double

# Input angles
angle_x = 30.0
angle_y = 120.0

# Call C function to compute direction vector
direction = lib.fromDirectionCosines(angle_x, angle_y)

print("Unit direction vector (from C):")
print(f"x = {direction.x:.6f}")
print(f"y = {direction.y:.6f}")
print(f"z = {direction.z:.6f}")

# Compute angle with z-axis
e_z = Vector3(0.0, 0.0, 1.0)
cos_gamma = lib.dotProduct(direction, e_z)
gamma_deg = math.degrees(math.acos(cos_gamma))
print(f"Angle with z-axis = {gamma_deg:.2f} degrees")

# Example values for the direction cosines
cos_alpha = 0.866025
cos_beta = -0.5
cos_gamma = 0.0

# Generate points along the line (both directions)
t = np.linspace(-3, 3, 100)   # allows negative and positive values
x = cos_alpha * t
y = cos_beta * t
z = cos_gamma * t

# Create the plot
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

# Plot the direction line
ax.plot(x, y, z, color="blue", label=r"$L : (\cos\alpha, \cos\beta, \cos\gamma)t$")

# Draw X, Y, Z axes with arrows
ax.quiver(0, 0, 0, 3, 0, 0, color="red", arrow_length_ratio=0.05)
ax.text(3.2, 0, 0, "X", color="red")

ax.quiver(0, 0, 0, 0, 3, 0, color="green", arrow_length_ratio=0.05)
ax.text(0, 3.2, 0, "Y", color="green")

ax.quiver(0, 0, 0, 0, 0, 3, color="black", arrow_length_ratio=0.05)
ax.text(0, 0, 3.2, "Z", color="black")

# Axis labels and title
ax.set_xlabel("X-axis")
ax.set_ylabel("Y-axis")
ax.set_zlabel("Z-axis")
ax.set_title("Line with Direction Cosines")
ax.legend()

# Set view limits
ax.set_xlim([-3, 3])
ax.set_ylim([-3, 3])
ax.set_zlim([-3, 3])

# Save the figure
plt.savefig("direction_line_full.png", dpi=300, bbox_inches="tight")

plt.show()

