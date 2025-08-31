import numpy as np
import matplotlib.pyplot as plt

# Define abstract vectors a and b
a = np.array([1, 0])   # arbitrary choice for a
b = np.array([0, 1])   # arbitrary choice for b

# Given vectors
BA = 2 * a
BC = 3 * b

# Place point B at origin
B = np.array([0, 0])
A = B + BA
C = B + BC

# Compute AC
AC = C - A

print("Vector BA =", BA)
print("Vector BC =", BC)
print("Vector AC =", AC)

# Function to plot arrows
def draw_vector(start, vec, color, label):
    plt.arrow(start[0], start[1], vec[0], vec[1],
              head_width=0.2, length_includes_head=True,
              color=color)
    mid = start + vec/2
    plt.text(mid[0]+0.2, mid[1]+0.2, label, fontsize=12, color=color)

# Plot triangle sides
plt.plot([A[0], B[0], C[0], A[0]],
         [A[1], B[1], C[1], A[1]],
         'gray', linewidth=1.5)

# Draw vectors
draw_vector(B, BA, "red", "BA=2a")
draw_vector(B, BC, "blue", "BC=3b")
draw_vector(A, AC, "green", "AC=3b-2a")

# Mark points
points = {"A": A, "B": B, "C": C}
colors = {"A": "red", "B": "black", "C": "blue"}

for name, pt in points.items():
    plt.plot(pt[0], pt[1], 'o', color=colors[name])
    plt.text(pt[0]+0.3, pt[1]+0.3, f"{name}({pt[0]},{pt[1]})", fontsize=12)

# Settings
plt.xlabel("x-axis")
plt.ylabel("y-axis")
plt.title("Triangle ABC with Vectors BA, BC, AC")
plt.grid(True)
plt.gca().set_aspect('equal', adjustable='box')

plt.show()
