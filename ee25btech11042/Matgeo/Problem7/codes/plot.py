import ctypes
import numpy as np
import matplotlib.pyplot as plt

# --- Step 1: Load the shared library ---
lib = ctypes.CDLL('./4.7.39.so')

# --- Step 2: Define the C function signature using NumPy-aware pointers ---
calculate_distance = lib.calculate_distance_from_xaxis

# Define the argument types
calculate_distance.argtypes = [
    np.ctypeslib.ndpointer(dtype=np.double, ndim=1, flags='C_CONTIGUOUS'), # input_P
    np.ctypeslib.ndpointer(dtype=np.double, ndim=1, flags='C_CONTIGUOUS')  # output_distance
]
# The function has a 'void' return type in C
calculate_distance.restype = None

# --- Step 3: Prepare NumPy arrays and call the C function ---
# Define the point P as a NumPy array
P = np.array([2.0, 3.0], dtype=np.double)

# Create an empty NumPy array for the C function to fill
output_data = np.zeros(1, dtype=np.double)

# Call the C function. NumPy arrays are passed directly.
calculate_distance(P, output_data)

# --- Step 4: Extract the result and plot ---
# The calculated distance is the first (and only) element in the output array
distance = output_data[0]
print(f"Point P Coordinates: ({P[0]}, {P[1]})")
print(f"Distance from x-axis (calculated by C): {distance:.4f}")

# Setup for plotting
fig, ax = plt.subplots(figsize=(8, 8))
ax.set_aspect('equal', adjustable='box')
ax.grid(True, linestyle=':', alpha=0.7)

# The projection of P onto the x-axis is Q
Q = np.array([P[0], 0.0])

# Plot the distance line between P and Q
ax.plot([P[0], Q[0]], [P[1], Q[1]], 'g--', label=f'Distance = {distance:.2f}')

# Plot point P and its projection Q
ax.plot(P[0], P[1], 'o', markersize=10, color='red', label=f'Point P({P[0]}, {P[1]})')
ax.text(P[0] + 0.1, P[1] + 0.1, 'P', fontsize=14, fontweight='bold', color='red')
ax.plot(Q[0], Q[1], 'o', markersize=8, color='blue')
ax.text(Q[0] + 0.1, Q[1] + 0.1, 'Q', fontsize=14, fontweight='bold', color='blue')

# Axes and Title
ax.axhline(0, color='black', linewidth=0.8)
ax.axvline(0, color='black', linewidth=0.8)
ax.set_xlim(-1, 5)
ax.set_ylim(-1, 5)
ax.set_title('Distance of Point P from the x-axis', fontsize=16)
ax.legend(loc="upper left")

# Save the figure to be used in the LaTeX document
plt.savefig('distance_plot.png')

plt.show()
