import ctypes
import platform
import numpy as np
import matplotlib.pyplot as plt

# --- Part 1: Ctypes setup to call the C function ---

# Load the shared library based on the operating system
lib_name = 'orthocentre_lib.so' if platform.system() != 'Windows' else 'orthocentre_lib.dll'
try:
    ortho_lib = ctypes.CDLL('./' + lib_name)
except OSError as e:
    print(f"Error loading shared library: {e}")
    print("Please ensure you have compiled the C code in Step 2.")
    exit()

# Define the argument types for the C function
ortho_lib.calculateOrthocentre.argtypes = [
    ctypes.c_double, ctypes.c_double, ctypes.c_double,  # Line 1 (a, b, c)
    ctypes.c_double, ctypes.c_double, ctypes.c_double,  # Line 2 (a, b, c)
    ctypes.c_double, ctypes.c_double, ctypes.c_double,  # Line 3 (a, b, c)
    ctypes.POINTER(ctypes.c_double),                     # Pointer for result_x
    ctypes.POINTER(ctypes.c_double)                      # Pointer for result_y
]
# Define the return type (void)
ortho_lib.calculateOrthocentre.restype = None

# Define the coefficients for the three lines
l1_a, l1_b, l1_c = 1.0, 1.0, 1.0
l2_a, l2_b, l2_c = 2.0, 3.0, 6.0
l3_a, l3_b, l3_c = 4.0, -1.0, -4.0

# Prepare variables to receive the output from the C function
result_x = ctypes.c_double()
result_y = ctypes.c_double()

# Call the C function, passing variables by reference for the output
ortho_lib.calculateOrthocentre(
    l1_a, l1_b, l1_c,
    l2_a, l2_b, l2_c,
    l3_a, l3_b, l3_c,
    ctypes.byref(result_x),
    ctypes.byref(result_y)
)

# Get the Python float values from the ctypes objects
# This is the Orthocentre 'H' calculated by the C code
H_from_C = np.array([result_x.value, result_y.value])

print(f"Orthocentre of the triangle : ({H_from_C[0]:.4f}, {H_from_C[1]:.4f})")

# --- Part 2: Matplotlib plotting using the result from C ---

# Define the x-axis range for plotting
x = np.linspace(-4, 2, 500)

# Equations of the Triangle Sides
y_l1 = 1 - x
y_l2 = (6 - 2*x) / 3
y_l3 = 4*x + 4

# Vertices (for plotting purposes)
A = np.array([-3, 4])
B = np.array([-3/7, 16/7])
C = np.array([-3/5, 8/5])

# Altitudes (for plotting purposes)
y_alt_A = (13 - x) / 4
y_alt_C = (3*x + 5) / 2

# Plotting setup
plt.style.use('seaborn-v0_8-whitegrid')
fig, ax = plt.subplots(figsize=(10, 10))

# Plot the sides of the triangle
ax.plot(x, y_l1, 'b-', label='L1: $x + y = 1$')
ax.plot(x, y_l2, 'g-', label='L2: $2x + 3y = 6$')
ax.plot(x, y_l3, 'm-', label='L3: $4x - y = -4$')

# Plot the altitudes
ax.plot(x, y_alt_A, 'r--', alpha=0.7, label='Altitude from A')
ax.plot(x, y_alt_C, 'c--', alpha=0.7, label='Altitude from C')

# Plot the vertices
ax.plot(A[0], A[1], 'ko', markersize=8)
ax.plot(B[0], B[1], 'ko', markersize=8)
ax.plot(C[0], C[1], 'ko', markersize=8)

# Add coordinate labels to vertices
vertices = {'A': A, 'B': B, 'C': C}
for name, pos in vertices.items():
    label = f'{name} ({pos[0]:.2f}, {pos[1]:.2f})'
    ax.text(pos[0] + 0.1, pos[1] + 0.1, label, fontsize=12, va='bottom', ha='left')

# Plot the orthocentre USING THE RESULT FROM THE C FUNCTION
ax.plot(H_from_C[0], H_from_C[1], 'ro', markersize=12, label=f'Orthocentre H ({H_from_C[0]:.2f}, {H_from_C[1]:.2f})')
orthocentre_label = f'H ({H_from_C[0]:.2f}, {H_from_C[1]:.2f})'
ax.text(H_from_C[0] + 0.1, H_from_C[1] - 0.1, orthocentre_label, fontsize=12, va='top', color='red')

# Formatting the Plot
ax.set_title('Orthocentre of a Triangle (Calculated via C)', fontsize=18)
ax.set_xlabel('x-axis', fontsize=12)
ax.set_ylabel('y-axis', fontsize=12)
ax.axhline(0, color='black', linewidth=0.5)
ax.axvline(0, color='black', linewidth=0.5)
ax.set_aspect('equal', adjustable='box')
ax.set_xlim(-4, 2)
ax.set_ylim(-1, 5)
ax.legend(loc='upper right')

plt.show()
