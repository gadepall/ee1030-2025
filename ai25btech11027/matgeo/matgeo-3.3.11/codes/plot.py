import numpy as np
import matplotlib.pyplot as plt

# Coordinates
A = np.array([0, 0])
B = np.array([6, 0])
C = np.array([4.5, (3 * np.sqrt(3)) / 2])  # (4.5, 2.598)

# Triangle vertices for plotting
x_coords = [A[0], B[0], C[0], A[0]]
y_coords = [A[1], B[1], C[1], A[1]]

# Plotting the triangle
plt.figure(figsize=(6, 5))
plt.plot(x_coords, y_coords, 'b-', linewidth=2)
plt.fill(x_coords, y_coords, color='skyblue', alpha=0.3)

# Mark points A, B, C
plt.plot(*A, 'ko')
plt.text(A[0] - 0.2, A[1] - 0.2, 'A', fontsize=12)

plt.plot(*B, 'ko')
plt.text(B[0] + 0.1, B[1] - 0.2, 'B', fontsize=12)

plt.plot(*C, 'ko')
plt.text(C[0], C[1] + 0.2, 'C', fontsize=12)

# Axes settings
plt.axis('equal')
plt.grid(True)
plt.title("Triangle ABC: AB = 6 cm, ∠A = 30°, ∠B = 60°")
plt.xlabel("x-axis (cm)")
plt.ylabel("y-axis (cm)")
plt.show()

