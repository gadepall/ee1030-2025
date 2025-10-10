import ctypes
import sys
import math
import matplotlib.pyplot as plt
import os

#to save figure in figs folder
figs_folder = os.path.join("..","figs")

# ==========================
# Step 1: Load the shared library
# ==========================
# Assuming libvector.so is in the same directory
lib = ctypes.CDLL("./libvector.so")

# Define the argument and return types for the C function
lib.findMagnitude.argtypes = [ctypes.c_float, ctypes.c_float]  # Two float arguments
lib.findMagnitude.restype = ctypes.c_float  # Return type is float

# ==========================
# Step 2: Call the C function to compute magnitude
# ==========================
angle_deg = 60.0         # Angle in degrees
dot_product = 4.5         # Given scalar product (9/2)

# Call the C function
magnitude = lib.findMagnitude(angle_deg, dot_product)
print(f"The magnitude of each vector is: {magnitude:.2f}")

# ==========================
# Step 3: Plot the two vectors
# ==========================

# Convert angle to radians
angle_rad = math.radians(angle_deg)

# Vector a along the x-axis
a = [magnitude, 0]

# Vector b at 60 degrees
b = [magnitude * math.cos(angle_rad), magnitude * math.sin(angle_rad)]

# Create plot
plt.figure(figsize=(6, 6))

# Plot vector a (blue)
plt.quiver(0, 0, a[0], a[1], angles='xy', scale_units='xy', scale=1, color='blue', label='vector a')

# Plot vector b (red)
plt.quiver(0, 0, b[0], b[1], angles='xy', scale_units='xy', scale=1, color='red', label='vector b')

# Add text annotations
plt.text(a[0] / 2, a[1] / 2, f"|a| = {magnitude:.2f}", fontsize=10, color='blue')
plt.text(b[0] / 2, b[1] / 2, f"|b| = {magnitude:.2f}", fontsize=10, color='red')

# Labels and title
plt.xlim(-1, magnitude + 2)
plt.ylim(-1, magnitude + 2)
plt.xlabel("X-axis")
plt.ylabel("Y-axis")
plt.title(f"Two vectors with magnitude {magnitude:.2f} and {angle_deg}° between them")
plt.legend()
plt.grid(True)
plt.gca().set_aspect('equal', adjustable='box')

# Show the plot
plt.savefig(os.path.join(figs_folder,"fig1.png"))
plt.show()

