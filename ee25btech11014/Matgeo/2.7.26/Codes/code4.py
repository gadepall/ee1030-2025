import ctypes
import matplotlib.pyplot as plt

# Load compiled shared C library
quad_lib = ctypes.CDLL('./code4.so')

# Define function signature
quad_lib.findQuadArea.argtypes = [ctypes.c_int, ctypes.c_int,
                                  ctypes.c_int, ctypes.c_int,
                                  ctypes.c_int, ctypes.c_int,
                                  ctypes.c_int, ctypes.c_int]
quad_lib.findQuadArea.restype = ctypes.c_float

# Take input from user
print("Enter coordinates of quadrilateral ABCD:")

x1, y1 = map(int, input("Enter A (x y): ").split())
x2, y2 = map(int, input("Enter B (x y): ").split())
x3, y3 = map(int, input("Enter C (x y): ").split())
x4, y4 = map(int, input("Enter D (x y): ").split())

# Call C function
area = quad_lib.findQuadArea(x1, y1, x2, y2, x3, y3, x4, y4)

# Store points and labels
points = [(x1, y1), (x2, y2), (x3, y3), (x4, y4)]
labels = ["A", "B", "C", "D"]

# Close polygon for plotting
x_vals = [p[0] for p in points] + [points[0][0]]
y_vals = [p[1] for p in points] + [points[0][1]]

# Plot quadrilateral
plt.figure(figsize=(7,7))
plt.plot(x_vals, y_vals, 'b-o', linewidth=2)

# Fill (shade) the quadrilateral
plt.fill(x_vals, y_vals, color="skyblue", alpha=0.5, label="Quadrilateral Area")

# Mark vertices with labels + coordinates
for (x, y), label in zip(points, labels):
    plt.text(x+0.2, y+0.2, f"{label}{(x,y)}", fontsize=11, color="red")

# Draw diagonal AC
A = points[0]  # A(x1, y1)
C = points[2]  # C(x3, y3)
plt.plot([A[0], C[0]], [A[1], C[1]], 'r--', linewidth=2, label="Diagonal AC")

# Formatting
plt.title(f"Quadrilateral ABCD (Area = {area:.2f} sq. units)")
plt.axhline(0, color="black", linewidth=0.5)
plt.axvline(0, color="black", linewidth=0.5)
plt.grid(True, linestyle="--", alpha=0.6)
plt.gca().set_aspect('equal', adjustable='box')
plt.legend()

# Save the figure
plt.savefig("fig_4.png", dpi=300, bbox_inches="tight")

# Show the plot
plt.show()
