import matplotlib.pyplot as plt
import numpy as np

# Side length and angle
s = 3.4
theta = np.deg2rad(45)

# Coordinates of vertices
A = np.array([0, 0])
B = np.array([s, 0])
D = np.array([s*np.cos(theta), s*np.sin(theta)])
C = B + D

# Plot rhombus
x = [A[0], B[0], C[0], D[0], A[0]]
y = [A[1], B[1], C[1], D[1], A[1]]

plt.figure(figsize=(7,5))
plt.plot(x, y, 'o-', color='orange')
plt.fill(x, y, color='orange', alpha=0.2)

# Mark vertices
plt.text(A[0]-0.3, A[1]-0.3, f"A{tuple(A)}")
plt.text(B[0]+0.1, B[1]-0.3, f"B{tuple(B)}")
plt.text(C[0]+0.1, C[1],   f"C{tuple(np.round(C,2))}")
plt.text(D[0]-0.6, D[1]+0.1, f"D{tuple(np.round(D,2))}")

# Add side labels
plt.text((A[0]+B[0])/2 - 0.5, (A[1]+B[1])/2 - 0.3, "3.40 cm")
plt.text((B[0]+C[0])/2 + 0.1, (B[1]+C[1])/2, "3.40 cm")
plt.text((C[0]+D[0])/2, (C[1]+D[1])/2 + 0.3, "3.40 cm")
plt.text((A[0]+D[0])/2 - 1.0, (A[1]+D[1])/2, "3.40 cm")

# Draw angle at A
arc = np.linspace(0, theta, 100)
plt.plot(0.6*np.cos(arc), 0.6*np.sin(arc), color="blue")
plt.text(0.8, 0.3, "45°", color="blue")

# Axes setup
plt.title("Rhombus with side = 3.4 cm and angle A = 45°")
plt.xlabel("x (cm)")
plt.ylabel("y (cm)")
plt.grid(True, linestyle="--", alpha=0.6)
plt.axis("equal")
plt.show()
