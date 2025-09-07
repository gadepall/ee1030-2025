# File: plotter.py
import ctypes
import platform
import numpy as np
import matplotlib.pyplot as plt

c_lib=ctypes.CDLL('./code.so')

# --- Define the C function signature for Python ---
# Get a handle to the function
find_points_func = solver_lib.find_points

# Specify the argument types: four pointers to C doubles
find_points_func.argtypes = [
    ctypes.POINTER(ctypes.c_double),
    ctypes.POINTER(ctypes.c_double),
    ctypes.POINTER(ctypes.c_double),
    ctypes.POINTER(ctypes.c_double)
]
# Specify the return type (void)
find_points_func.restype = None

# --- Call the C function ---
# Create C double variables to hold the results
p1_x, p1_y = ctypes.c_double(), ctypes.c_double()
p2_x, p2_y = ctypes.c_double(), ctypes.c_double()

# Call the function, passing the variables by reference
find_points_func(
    ctypes.byref(p1_x), ctypes.byref(p1_y),
    ctypes.byref(p2_x), ctypes.byref(p2_y)
)

# --- Retrieve the results and prepare for plotting ---
# Extract the Python values from the C types
px = np.array([p1_x.value, p2_x.value])
py = np.array([p1_y.value, p2_y.value])

print(f"Points calculated by C function: ({px[0]}, {py[0]}) and ({px[1]}, {py[1]})")

# ---  Generate the Plot (code adapted from your original script) ---
x = np.linspace(-10, 10, 400)
y1 = 4 - x  # Line 1: x + y = 4
y2 = (10 - 4*x) / 3  # Line 2: 4x + 3y = 10

# Define a helper function to find the foot of the perpendiculars
n = np.array([4, 3])
c = 10
norm_n_sq = np.dot(n, n)
def foot_of_perpendicular(P):
    lamb = (np.dot(n, P) - c) / norm_n_sq
    return P - lamb * n

# Calculate the foot points for the dotted lines
foot_points = np.array([foot_of_perpendicular(np.array([px[i], py[i]])) for i in range(len(px))])

# Create the plot
plt.figure(figsize=(8, 6))
plt.plot(x, y1, label=r'$x+y=4$ (L1)', color='blue')
plt.plot(x, y2, label=r'$4x+3y=10$ (L2)', color='green')
plt.scatter(px, py, color='red', zorder=5)

# Add text labels for the points and distances
plt.text(px[0], py[0], f'({int(px[0])},{int(py[0])})', fontsize=12, va='bottom', ha='right', color='red')
plt.text(px[1], py[1], f'({int(px[1])},{int(py[1])})', fontsize=12, va='bottom', ha='right', color='red')

for i in range(len(px)):
    plt.plot([px[i], foot_points[i,0]], [py[i], foot_points[i,1]], linestyle='dotted', color='red')
    mid_x = (px[i] + foot_points[i,0]) / 2
    mid_y = (py[i] + foot_points[i,1]) / 2
    plt.text(mid_x + 0.3, mid_y + 0.3, 'dist = 1', color='red', fontsize=10, va='bottom', ha='left')

# Final plot styling
plt.xlim(-10, 10)
plt.ylim(-5, 15)
plt.xlabel('x')
plt.ylabel('y')
plt.axhline(0, color='black', linewidth=0.5)
plt.axvline(0, color='black', linewidth=0.5)

plt.legend()
plt.grid(True)
# Save the plot to a file
plt.savefig('../figs/fig.png')

# Display the plot
plt.show()  
