import ctypes
import sys
import os
import matplotlib.pyplot as plt

# --- 1. Define ctypes Structure ---
# This class must match the C struct 'PlotData' field for field.
class PlotData(ctypes.Structure):
    _fields_ = [
        ("center_x", ctypes.c_double),
        ("center_y", ctypes.c_double),
        ("radius", ctypes.c_double),
        ("P_x", ctypes.c_double),
        ("P_y", ctypes.c_double),
        ("M1_x", ctypes.c_double),
        ("M1_y", ctypes.c_double),
        ("M2_x", ctypes.c_double),
        ("M2_y", ctypes.c_double),
        ("Q1_x", ctypes.c_double),
        ("Q1_y", ctypes.c_double),
        ("Q2_x", ctypes.c_double),
        ("Q2_y", ctypes.c_double),
    ]



# Try to load the library
c_lib = ctypes.CDLL('./code.so')



# --- 3. Set up C function prototypes ---
# Get the function from the library
calculate_plot_values = c_lib.calculate_plot_values

# Define the function's argument types (a, b, pointer_to_struct)
calculate_plot_values.argtypes = [
    ctypes.c_double, 
    ctypes.c_double, 
    ctypes.POINTER(PlotData)
]
# Define the function's return type (void)
calculate_plot_values.restype = None

# --- 4. Call the C Function ---
a = 2.0
b = 1.0

# Create an instance of our Python structure
plot_data = PlotData()

# Call the C function.
# We pass 'a' and 'b', and a pointer to our plot_data instance.
calculate_plot_values(ctypes.c_double(a), 
                      ctypes.c_double(b), 
                      ctypes.byref(plot_data))

# --- 5. Extract values into Python-friendly variables ---
center = (plot_data.center_x, plot_data.center_y)
radius = plot_data.radius
P = (plot_data.P_x, plot_data.P_y)
M1 = (plot_data.M1_x, plot_data.M1_y)
M2 = (plot_data.M2_x, plot_data.M2_y)
Q1 = (plot_data.Q1_x, plot_data.Q1_y)
Q2 = (plot_data.Q2_x, plot_data.Q2_y)

# --- 6. Plotting ---
# This section is identical to your original script,
# but it uses the data populated by the C library.

plt.style.use('seaborn-v0_8-whitegrid')
fig, ax = plt.subplots(figsize=(8, 8))

# Plot the circle
circle_patch = plt.Circle(center, radius, color='skyblue', fill=False, lw=2)
ax.add_patch(circle_patch)

# Plot the chords
ax.plot([P[0], Q1[0]], [P[1], Q1[1]], 'r-')
ax.plot([P[0], Q2[0]], [P[1], Q2[1]], 'g-')

# Plot the key points
ax.plot(*P, 'ko', markersize=8)
ax.plot(*center, 'bo', markersize=8)
ax.plot(*M1, 'ro', markersize=6)
ax.plot(*M2, 'go', markersize=6)

# Plot the x-axis
ax.axhline(0, color='black', lw=2)

# --- Direct Annotation on the Graph ---
ax.text(P[0] + 0.05, P[1], f' P({P[0]:.1f}, {P[1]:.1f})', verticalalignment='center')
ax.text(center[0] - 0.05, center[1] - 0.1, f'C({center[0]:.1f}, {center[1]:.2f})', horizontalalignment='right')
ax.text(M1[0], M1[1] + 0.05, f'M1 ({M1[0]:.2f},0)', horizontalalignment='center')
ax.text(M2[0], M2[1] + 0.05, f'M2 ({M2[0]:.2f},0)', horizontalalignment='center')
ax.text(-0.25, 0.05, 'X-axis (bisector)')

# --- Formatting ---
ax.set_aspect('equal', adjustable='box')
ax.set_title(f'For a = {a} and b = {b} (Calculated by C)', fontsize=16)
ax.set_xlabel('X-axis', fontsize=12)
ax.set_ylabel('Y-axis', fontsize=12)
plt.grid(True)

plt.savefig('../figs/fig2.png')

plt.show()
