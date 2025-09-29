import numpy as np
import matplotlib.pyplot as plt

# Given data
median_length_coefficient = 3  # coefficient of 'a' in median length

# Matrix approach to find radius
theta = 2 * np.pi / 3
cos_theta = np.cos(theta)
cos_theta_minus_1 = cos_theta - 1  # -3/2
coefficient_squared = cos_theta_minus_1**2  # 9/4

# Solve for r^2 coefficient: r^2 * (9/4) = 9a^2  =>  r^2 = 4a^2
r_squared_coefficient = (median_length_coefficient**2) / coefficient_squared  # 4
r = 2  # since a = 1 for plotting

# Print final answer
print(f"Answer: (c) x² + y² = {int(r_squared_coefficient)}a²")

# Define triangle vertices on the circle
A = np.array([r, 0])
B = np.array([r * cos_theta, r * np.sin(theta)])
C = np.array([r * cos_theta, -r * np.sin(theta)])
midpoint_BC = (B + C) / 2

# Plot setup
plt.figure(figsize=(8, 8))

# Draw circle
theta_circle = np.linspace(0, 2*np.pi, 200)
x_circle = r * np.cos(theta_circle)
y_circle = r * np.sin(theta_circle)
plt.plot(x_circle, y_circle, 'b-', linewidth=2, label=f'Circle: x² + y² = {int(r_squared_coefficient)}a²')

# Draw triangle
triangle_x = [A[0], B[0], C[0], A[0]]
triangle_y = [A[1], B[1], C[1], A[1]]
plt.plot(triangle_x, triangle_y, 'r-', linewidth=2, label='Equilateral Triangle')

# Draw median from A to midpoint of BC
plt.plot([A[0], midpoint_BC[0]], [A[1], midpoint_BC[1]], 'g--', linewidth=2, label='Median = 3a')

# Mark and label points
plt.plot(0, 0, 'ko')        ; plt.text(0.05, 0.05, 'O(0,0)', fontsize=12)
plt.plot(A[0], A[1], 'ro')  ; plt.text(A[0]+0.1, A[1]+0.1, 'A(2,0)', fontsize=12)
plt.plot(B[0], B[1], 'ro')  ; plt.text(B[0]-0.4, B[1]+0.1, 'B(-1,√3)', fontsize=12)
plt.plot(C[0], C[1], 'ro')  ; plt.text(C[0]-0.4, C[1]-0.2, 'C(-1,-√3)', fontsize=12)
plt.plot(midpoint_BC[0], midpoint_BC[1], 'go') ; plt.text(midpoint_BC[0]+0.1, midpoint_BC[1]+0.1, 'M', fontsize=12)

# Formatting
plt.axis('equal')
plt.xlim(-3, 3)
plt.ylim(-3, 3)
plt.grid(True, alpha=0.3)
plt.xlabel('x')
plt.ylabel('y')
plt.title('Circle with Equilateral Triangle (Median = 3a)')
plt.legend()

plt.tight_layout()
plt.savefig("fig1.png")
plt.show()
