import matplotlib.pyplot as plt
import numpy as np
import ctypes
import os

# --- Configuration ---
LIB_NAME = './code.so'
NUM_POINTS = 400 # Number of points for smooth curves

# --- Load the shared C library ---
c_lib = ctypes.CDLL(LIB_NAME)

# --- Define the signature for the plotting function ---
calculate_plot_data = c_lib.calculate_plot_data
calculate_plot_data.argtypes = [
    ctypes.POINTER(ctypes.c_double), # x1
    ctypes.POINTER(ctypes.c_double), # y1
    ctypes.POINTER(ctypes.c_double), # x2
    ctypes.POINTER(ctypes.c_double), # y2
    ctypes.POINTER(ctypes.c_double), # x_tangent2
    ctypes.POINTER(ctypes.c_double), # y_tangent2
    ctypes.c_int                    # num_points
]
calculate_plot_data.restype = None

# --- Define the signature for the geometry calculation function ---
calculate_geometric_properties = c_lib.calculate_geometric_properties
calculate_geometric_properties.argtypes = [
    ctypes.POINTER(ctypes.c_double), # p_x
    ctypes.POINTER(ctypes.c_double), # p_y
    ctypes.POINTER(ctypes.c_double), # m1
    ctypes.POINTER(ctypes.c_double)  # m2
]
calculate_geometric_properties.restype = None


# --- Call C function to calculate P and m ---
# Prepare variables to hold the results (passed by reference)
p_x_c = ctypes.c_double()
p_y_c = ctypes.c_double()
m1_c = ctypes.c_double()
m2_c = ctypes.c_double()

print("Calling C function to calculate geometric properties (P and m)...")
calculate_geometric_properties(ctypes.byref(p_x_c), ctypes.byref(p_y_c), ctypes.byref(m1_c), ctypes.byref(m2_c))

# Extract the values
p_x = p_x_c.value
p_y = p_y_c.value
m1 = m1_c.value
m2 = m2_c.value

print(f"Point of Contact P: ({p_x:.4f}, {p_y:.4f})")
print(f"Tangent Slopes: m1 = {m1:.4f}, m2 = {m2:.4f}\n")


# --- Prepare data arrays for the plotting function ---
DoubleArray = ctypes.c_double * NUM_POINTS
x1_c = DoubleArray()
y1_c = DoubleArray()
x2_c = DoubleArray()
y2_c = DoubleArray()
x_tangent2_c = DoubleArray()
y_tangent2_c = DoubleArray()

# --- Call the C function to populate the plotting arrays ---
print("Calling C function to calculate plot data...")
calculate_plot_data(x1_c, y1_c, x2_c, y2_c, x_tangent2_c, y_tangent2_c, NUM_POINTS)
print("Plotting data calculation complete.")

# --- Convert ctypes arrays to NumPy arrays for plotting ---
x1 = np.ctypeslib.as_array(x1_c)
y1 = np.ctypeslib.as_array(y1_c)
x2 = np.ctypeslib.as_array(x2_c)
y2 = np.ctypeslib.as_array(y2_c)
x_tangent2 = np.ctypeslib.as_array(x_tangent2_c)
y_tangent2 = np.ctypeslib.as_array(y_tangent2_c)

# --- Static data for labels and markers ---
C1_center = np.array([2., 1.])
C2_center = np.array([6., 4.])
# Use the point of contact calculated from C
P_contact = np.array([p_x, p_y])

# --- Plotting Code ---
print("Generating plot...")
fig, ax = plt.subplots(figsize=(12, 9))
ax.set_aspect('equal', adjustable='box')
ax.grid(True, linestyle='--', alpha=0.6)

# Plot the circles using data from the C function
ax.plot(x1, y1, color='blue', linewidth=2, label='Circle 1 (from C)')
ax.plot(x2, y2, color='green', linewidth=2, label='Circle 2 (from C)')

# Plot the common tangents
ax.axhline(0, color='red', linestyle='-', linewidth=2, label=f'Tangent (m={m1:.2f})')
ax.plot(x_tangent2, y_tangent2, color='purple', linestyle='-', linewidth=2, label=f'Tangent (m={m2:.2f})')

# Plot and label important points
ax.plot(C1_center[0], C1_center[1], 'bo', markersize=5)
ax.text(C1_center[0] + 0.1, C1_center[1] + 0.1, '$C_1(2,1)$', fontsize=12)

ax.plot(C2_center[0], C2_center[1], 'go', markersize=5)
ax.text(C2_center[0] + 0.1, C2_center[1] + 0.1, '$C_2(6,4)$', fontsize=12)

ax.plot(P_contact[0], P_contact[1], 'ko', markersize=7)
ax.text(P_contact[0] + 0.1, P_contact[1] - 0.3, f'P({p_x:.2f}, {p_y:.2f})', fontsize=12)

# Final plot formatting
ax.set_xlim(-1, 9)
ax.set_ylim(-2, 9)
ax.set_xlabel("X-axis", fontsize=12)
ax.set_ylabel("Y-axis", fontsize=12)
plt.title("Common Tangents (Data from C Library)", fontsize=14)
plt.legend()
plt.tight_layout()

# Save the figure to a file

plt.savefig('../figs/fig2.png')

