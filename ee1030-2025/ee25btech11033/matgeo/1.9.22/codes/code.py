import numpy as np
import matplotlib.pyplot as plt
import ctypes
import os

c_lib=ctypes.CDLL('./code.so')

# --- 2. Define the C Function Signature in Python ---
# Get a handle to the C function
find_y_coordinates = c_lib.findYCoordinates

# Define the argument types (argtypes) for the C function
# double, double, double, double, *double, *double
find_y_coordinates.argtypes = [
    ctypes.c_double, ctypes.c_double,
    ctypes.c_double, ctypes.c_double,
    ctypes.POINTER(ctypes.c_double),
    ctypes.POINTER(ctypes.c_double)
]
# Define the return type (restype)
find_y_coordinates.restype = ctypes.c_int

# --- 3. Prepare Inputs and Call the C Function ---
# Problem parameters
px, py = 2.0, -3.0
qx = 10.0
distance = 10.0

# Create C-compatible variables to hold the results (y1 and y2)
y1_c = ctypes.c_double()
y2_c = ctypes.c_double()

# Call the C function. Use ctypes.byref() to pass the variables by reference.
success = find_y_coordinates(px, py, qx, distance, ctypes.byref(y1_c), ctypes.byref(y2_c))

if not success:
    print("C function failed to find real coordinates. Check your inputs.")
    exit()

# Extract the Python values from the C-type objects
y1 = y1_c.value
y2 = y2_c.value

print(f"Values calculated by C function: y1 = {y1}, y2 = {y2}")

# --- 4. Plot the Results ---
# Define the points using the values from the C function
P = np.array([px, py]).reshape(-1, 1)
Q1 = np.array([qx, y1]).reshape(-1, 1) # Use y1 from C
Q2 = np.array([qx, y2]).reshape(-1, 1) # Use y2 from C

# Plotting the lines from P to Q1 and P to Q2
plt.plot([P[0,0], Q1[0,0]], [P[1,0], Q1[1,0]], label=f'$PQ_1$ (distance={distance})')
plt.plot([P[0,0], Q2[0,0]], [P[1,0], Q2[1,0]], label=f'$PQ_2$ (distance={distance})')

# Combining all points for easy plotting and labeling
coords = np.block([[P, Q1, Q2]])
plt.scatter(coords[0, :], coords[1, :], color='red', zorder=5)

# Adding labels for each point
vert_labels = ['P', 'Q₁', 'Q₂']
for i, txt in enumerate(vert_labels):
    plt.annotate(f'{txt}\n({coords[0, i]:.0f}, {coords[1, i]:.0f})',
                 (coords[0, i], coords[1, i]),
                 textcoords="offset points",
                 xytext=(0, 10),
                 ha='center')

# --- Plot Formatting ---
ax = plt.gca()
ax.spines['top'].set_color('none')
ax.spines['left'].set_position('zero')
ax.spines['right'].set_color('none')
ax.spines['bottom'].set_position('zero')

plt.legend(loc='best')
plt.grid(True)
plt.axis('equal')
plt.title("Plot generated using values from C function")
# Save the plot to a file
plt.savefig('../figs/fig.png')


plt.show()
