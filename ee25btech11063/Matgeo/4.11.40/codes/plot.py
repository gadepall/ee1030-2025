import matplotlib.pyplot as plt
import numpy as np

# Define line
x = np.linspace(-2, 1, 400)
y = 3*x + 2

# Vertices
A = (-2, 0)
B = (-2/3, 0)   # x-intercept
C = (1, 0)
D = (-2, -4)
E = (1, 5)

# Plot line
plt.plot(x, y, 'b-', label="y = 3x + 2")

# Plot x-axis
plt.axhline(0, color='black', linewidth=1)

# Shade the bounded area (polygon A-B-C-E-D-A)
polygon_x = [A[0], B[0], C[0], E[0], D[0], A[0]]
polygon_y = [A[1], B[1], C[1], E[1], D[1], A[1]]
plt.fill(polygon_x, polygon_y, color='orange', alpha=0.6, label="Bounded Area")

# Mark and label vertices (B shown symbolically)
vertices = {
    "A(-2,0)": A,
    "B(-2/3,0)": B,   # keep symbolic form
    "C(1,0)": C,
    "D(-2,-4)": D,
    "E(1,5)": E
}

for name, (px, py) in vertices.items():
    plt.plot(px, py, 'ro')
    plt.text(px+0.05, py+0.2, name, fontsize=9)

# Annotate area
plt.text(-0.5, 1.5, "Area = 41/6", fontsize=12, color="red", weight="bold")

# Labels and formatting
plt.xlabel("x-axis")
plt.ylabel("y-axis")
plt.title("Bounded Region between y=3x+2 and x-axis (x∈[-2,1])")
plt.legend()
plt.grid(True)

# Save figure
plt.savefig("bounded_area_vertices.png", dpi=300)
plt.show()


