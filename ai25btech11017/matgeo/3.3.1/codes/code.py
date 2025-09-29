import matplotlib.pyplot as plt
import numpy as np

# Given values
BC = 6
AB = 5
angle_ABC = np.radians(60)  # convert degrees to radians

# Use cosine rule to find AC
AC = np.sqrt(AB**2 + BC**2 - 2*AB*BC*np.cos(angle_ABC))

# Coordinates of points
B = np.array([0, 0])
C = np.array([BC, 0])
A = np.array([AB * np.cos(angle_ABC), AB * np.sin(angle_ABC)])

# Plot triangle
x_coords = [A[0], B[0], C[0], A[0]]
y_coords = [A[1], B[1], C[1], A[1]]

plt.figure(figsize=(6,6))
plt.plot(x_coords, y_coords, 'b-o')

# Label points
plt.text(A[0], A[1]+0.2, 'A', fontsize=12, color='red')
plt.text(B[0]-0.3, B[1]-0.3, 'B', fontsize=12, color='red')
plt.text(C[0]+0.1, C[1]-0.3, 'C', fontsize=12, color='red')

# Add side labels
plt.text((A[0]+B[0])/2 -0.5, (A[1]+B[1])/2, f"AB={AB}", fontsize=10, color="green")
plt.text((B[0]+C[0])/2, (B[1]+C[1])/2 -0.3, f"BC={BC}", fontsize=10, color="green")
plt.text((A[0]+C[0])/2 +0.2, (A[1]+C[1])/2, f"AC={AC:.2f}", fontsize=10, color="green")

# Formatting
plt.axis("equal")
plt.grid(True, linestyle="--", alpha=0.5)
plt.title("Triangle ABC with BC=6 cm, AB=5 cm, ∠ABC=60°")

# Save as image
plt.savefig("triangle_solution.png", dpi=300)
plt.show()

print("Triangle saved as 'triangle_solution.png'")
