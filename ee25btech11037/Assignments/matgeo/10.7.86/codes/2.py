import ctypes
import numpy as np
import matplotlib.pyplot as plt

# --- 1. Load your C shared library ---
try:
    mat_lib = ctypes.CDLL('./mat.so')
except :
    print(f"Error loading shared library: ")
    print("Please make sure you have compiled 'mat.c' into 'mat.so' in the same directory.")
    exit()

# --- 2. Define the function signature for Python ---

Calc_locus_c = mat_lib.Calc_locus
Calc_locus_c.argtypes = [
    ctypes.c_double, ctypes.c_double, # x1, x2
    ctypes.c_double, ctypes.c_double, # r1, r2
    ctypes.POINTER(ctypes.c_double),  # pointer to a
    ctypes.POINTER(ctypes.c_double),  # pointer to b
    ctypes.POINTER(ctypes.c_double)   # pointer to c
]
Calc_locus_c.restype = None # The C function is void

# --- 3. Set up data and call the C function ---

# Circle properties
c1_center_x, c1_radius = 0.0, 10.0
c2_center_x, c2_radius = 3.0, 2.0

# Create Python variables to hold the results from C
# These are special ctypes variables that can be passed by reference
a = ctypes.c_double()
b = ctypes.c_double()
c = ctypes.c_double()

# Call your C function
Calc_locus_c(c1_center_x, c2_center_x, c1_radius, c2_radius,
             ctypes.byref(a), ctypes.byref(b), ctypes.byref(c))

# Extract the values from the ctypes objects into regular Python variables
a_val, b_val, c_val = a.value, b.value, c.value

print(f"Values calculated from C function:")
print(f"  Semi-major axis (a): {a_val:.4f}")
print(f"  Semi-minor axis (b): {b_val:.4f}")
print(f"  Focus distance (c): {c_val:.4f}")


# --- 4. Generate points and plot using the results from C ---

# The center of the ellipse is the midpoint of the foci (circle centers)
ellipse_center_x = (c1_center_x + c2_center_x) / 2.0

# Generate angles for drawing smooth shapes
angles = np.linspace(0, 2 * np.pi, 200)

# Generate coordinates for the shapes
c1_x = c1_center_x + c1_radius * np.cos(angles)
c1_y = 0 + c1_radius * np.sin(angles)

c2_x = c2_center_x + c2_radius * np.cos(angles)
c2_y = 0 + c2_radius * np.sin(angles)

ellipse_x = ellipse_center_x + a_val * np.cos(angles)
ellipse_y = 0 + b_val * np.sin(angles)

# --- 5. Create the Plot ---
fig, ax = plt.subplots(figsize=(10, 10))
ax.set_aspect('equal', adjustable='box')
ax.grid(True, linestyle='--', alpha=0.6)
ax.set_title("Locus Plot Generated via C Function", fontsize=16)
ax.set_xlabel("x-axis")
ax.set_ylabel("y-axis")

# Create the locus equation string for the legend
locus_eq = f'Locus: $\\frac{{(x - {ellipse_center_x:.2f})^2}}{{{a_val:.2f}^2}} + \\frac{{y^2}}{{{b_val:.2f}^2}} = 1$'

# Plot the shapes
ax.plot(c1_x, c1_y, color='blue', label='$C_1: x^2 + y^2 = 100$')
ax.plot(c2_x, c2_y, color='red', label='$C_2: (x-3)^2 + y^2 = 4$')
ax.plot(ellipse_x, ellipse_y, color='purple', linestyle='-', label=locus_eq)

# Plot and label centers
ax.plot(c1_center_x, 0, 'bo', markersize=8)
ax.text(c1_center_x + 0.2, 0.2, f'$O_1$ ({c1_center_x:.0f}, 0)', color='blue')
ax.plot(c2_center_x, 0, 'ro', markersize=8)
ax.text(c2_center_x + 0.2, 0.2, f'$O_2$ ({c2_center_x:.0f}, 0)', color='red')

ax.set_xlim(-12, 12)
ax.set_ylim(-12, 12)
ax.legend(fontsize='small')
plt.savefig('2.png')
plt.show()


