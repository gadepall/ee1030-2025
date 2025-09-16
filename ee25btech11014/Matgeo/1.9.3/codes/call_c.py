import ctypes
import matplotlib.pyplot as plt

# Load compiled C library
c_lib = ctypes.CDLL('./rect.so')

# Define function signature
c_lib.findC.argtypes = [ctypes.c_float, ctypes.c_float,
                        ctypes.c_float, ctypes.c_float,
                        ctypes.c_float, ctypes.c_float,
                        ctypes.POINTER(ctypes.c_float),
                        ctypes.POINTER(ctypes.c_float)]

# Define known points
Ax, Ay = 0.0, 0.0
Bx, By = 4.0, 0.0
Dx, Dy = 0.0, -3.0

# Prepare variables for C output
Cx, Cy = ctypes.c_float(), ctypes.c_float()

# Call C function to compute C
c_lib.findC(Ax, Ay, Bx, By, Dx, Dy, ctypes.byref(Cx), ctypes.byref(Cy))

# Convert back to Python floats
Cx, Cy = Cx.value, Cy.value

# Define rectangle points
points = [
    [Ax, Ay],   # A
    [Bx, By],   # B
    [Cx, Cy],   # C (from C code)
    [Dx, Dy],   # D
    [Ax, Ay]    # Close
]

# Extract X and Y
x, y = zip(*points)

# Plot rectangle
plt.figure(figsize=(8, 6))
plt.plot(x, y, 'g--', label='Rectangle')

# Plot diagonal AC
plt.plot([Ax, Cx], [Ay, Cy], 'b', linewidth=2, label='Diagonal')

# Plot points
plt.scatter(x, y, c='r', s=60, label='Points')

# Labels
labels = [f"({Ax},{Ay})", f"({Bx},{By})", f"({Cx},{Cy})", f"({Dx},{Dy})", f"({Ax},{Ay})"]
for i, txt in enumerate(labels):
    plt.text(x[i] + 0.1, y[i] + 0.1, txt)

# Format
plt.xlabel("X-axis")
plt.ylabel("Y-axis")
plt.grid(True)
plt.legend()
plt.axis("equal")

plt.savefig("fig2.png", dpi=300)
plt.show()
