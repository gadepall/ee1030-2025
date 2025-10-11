import ctypes
import numpy as np
import matplotlib.pyplot as plt

# --- 1. COMPILE YOUR C CODE FIRST ---
# You must compile the C code for the 2-equation solver into a shared library.
# On Linux or macOS, use: gcc -shared -o mat.so -fPIC your_c_code.c

# --- 2. Load C library and Define Function Signature ---
try:
    lib = ctypes.CDLL('./mat.so')
except OSError as e:
    print(f"Error loading library: {e}")
    print("Please make sure you have compiled the C code into 'mat.so'")
    exit()

# Define the C function signature for a 2x3 augmented matrix
MatrixAug2x3 = (ctypes.c_float * 3) * 2
lib.solve_system.argtypes = [MatrixAug2x3]
lib.solve_system.restype = None

# --- 3. Define the Three Systems of Equations ---
# Each system represents the intersection of two lines

# System 1: 5x - y = 5  AND  3x - y = 3
system1 = np.array([
    [5.0, -1.0, 5.0],
    [3.0, -1.0, 3.0]
], dtype=np.float32)

# System 2: 5x - y = 5  AND  x = 0 (y-axis)
system2 = np.array([
    [5.0, -1.0, 5.0],
    [1.0,  0.0, 0.0]
], dtype=np.float32)

# System 3: 3x - y = 3  AND  x = 0 (y-axis)
system3 = np.array([
    [3.0, -1.0, 3.0],
    [1.0,  0.0, 0.0]
], dtype=np.float32)

systems = [system1, system2, system3]
vertices = []

# --- 4. Call C Function for Each System to Find Vertices ---
print("Calling C function to find vertices...")
for i, sys_np in enumerate(systems):
    # Convert numpy array to ctypes
    aug_ctypes = MatrixAug2x3(
        (ctypes.c_float * 3)(*sys_np[0]),
        (ctypes.c_float * 3)(*sys_np[1]),
    )
    
    # Call the C function (modifies aug_ctypes in-place)
    lib.solve_system(aug_ctypes)
    
    # Extract the solution (x, y) from the last column
    x = aug_ctypes[0][2]
    y = aug_ctypes[1][2]
    vertices.append((x, y))
    print(f"Vertex {i+1}: ({x:.1f}, {y:.1f})")

# --- 5. Plotting the 2D Graph ---
vertices_np = np.array(vertices)
x_vals = np.linspace(-1, 5, 400)

# Equations for plotting: y = mx + c
y1 = 5*x_vals - 5  # From 5x - y = 5
y2 = 3*x_vals - 3  # From 3x - y = 3

plt.figure(figsize=(8, 6))
plt.plot(x_vals, y1, label='5x - y = 5')
plt.plot(x_vals, y2, label='3x - y = 3')

# Plot the y-axis (x=0)
plt.axvline(0, color='gray', linestyle='--', label='y-axis (x=0)')

# Plot the vertices
plt.scatter(vertices_np[:, 0], vertices_np[:, 1], color='red', zorder=5, s=100, label='Vertices')

# Annotate the vertices using plt.annotate for better label placement
for (x, y) in vertices:
    # Format the text for the label
    label = f'({x:.1f}, {y:.1f})'
    # Use annotate to place the text
    plt.annotate(label,                      # The text to display
                 (x, y),                     # The point to annotate
                 textcoords="offset points", # Position the text via an offset
                 xytext=(0, 10),             # Offset text 10 points vertically
                 ha='center',                # Center the text horizontally
                 fontsize=12)

# Labels and appearance
plt.title('Triangle Formed by Lines and the Y-axis')
plt.xlabel('x-axis')
plt.ylabel('y-axis')
plt.axhline(0, color='black', linewidth=0.5) # x-axis
plt.grid(True, which='both', linestyle='--', linewidth=0.5)
plt.legend()
plt.ylim(-6, 2)
plt.xlim(-1, 4)
plt.gca().set_aspect('equal', adjustable='box')
plt.savefig('1.png')
plt.show()
