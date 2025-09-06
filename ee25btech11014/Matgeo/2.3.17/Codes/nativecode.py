import matplotlib.pyplot as plt
import numpy as np
import math

# Define points
A = np.array([4, 0])
B = np.array([-4, 0])
C = np.array([0, 3])

# Function to compute angle at vertex 'v' between points 'a' and 'b'
def compute_angle(a, v, b):
    va = a - v
    vb = b - v
    cos_theta = np.dot(va, vb) / (np.linalg.norm(va) * np.linalg.norm(vb))
    cos_theta = np.clip(cos_theta, -1.0, 1.0)
    angle_rad = math.acos(cos_theta)
    return math.degrees(angle_rad)

# Compute angles
angle_A = compute_angle(B, A, C)
angle_B = compute_angle(A, B, C)
angle_C = compute_angle(A, C, B)

# Create triangle path
x_vals = [A[0], B[0], C[0], A[0]]
y_vals = [A[1], B[1], C[1], A[1]]

# Plot triangle
plt.figure(figsize=(6, 6))
plt.plot(x_vals, y_vals, 'b-', linewidth=2)

# Plot points
plt.plot(A[0], A[1], 'ro')
plt.plot(B[0], B[1], 'go')
plt.plot(C[0], C[1], 'bo')

# Annotate points
plt.text(A[0]+0.2, A[1]-0.3, f"A ({A[0]}, {A[1]})\n∠A ≈ {angle_A:.2f}°", color='red')
plt.text(B[0]-2, B[1]-0.3, f"B ({B[0]}, {B[1]})\n∠B ≈ {angle_B:.2f}°", color='green')
plt.text(C[0]-0.8, C[1]+0.2, f"C ({C[0]}, {C[1]})\n∠C ≈ {angle_C:.2f}°", color='blue')

# Axis settings
plt.axis('equal')
plt.grid(True)
plt.title("Triangle ABC with Angles")
plt.xlabel("X")
plt.ylabel("Y")

plt.savefig("fig_3.png")
plt.show()
