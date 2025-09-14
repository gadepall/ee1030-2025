import numpy as np
import matplotlib.pyplot as plt

# --- Line: x + y = 0 ---
normal_vector = np.array([1, 1])     # n = (1, 1)
direction_vector = np.array([-1, 1]) # m = (-1, 1)

print(f"Normal Vector (n): {normal_vector}")
print(f"Direction Vector (m): {direction_vector}")

# Check orthogonality
dot_product = np.dot(normal_vector, direction_vector)
print(f"Dot product of n and m: {dot_product}")
if np.isclose(dot_product, 0):
    print("The vectors are orthogonal (as expected).")
else:
    print("The vectors are NOT orthogonal (something is wrong).")

# Line equation: x + y = 0 -> y = -x
def line_equation(x):
    return -x

x_vals = np.linspace(-5, 5, 200)
y_vals = line_equation(x_vals)

# Plotting
vector_origin = np.array([0, 0])  # start vectors at origin

plt.style.use('seaborn-v0_8-whitegrid')
plt.figure(figsize=(8, 8))

# Line
plt.plot(x_vals, y_vals, label='Line: x + y = 0', color='blue', zorder=1)

# Direction vector
plt.quiver(vector_origin[0], vector_origin[1],
           direction_vector[0], direction_vector[1],
           angles='xy', scale_units='xy', scale=1,
           color='green', label='Direction Vector', zorder=2)

# Normal vector
plt.quiver(vector_origin[0], vector_origin[1],
           normal_vector[0], normal_vector[1],
           angles='xy', scale_units='xy', scale=1,
           color='red', label='Normal Vector', zorder=2)

# Origin
plt.plot(vector_origin[0], vector_origin[1], 'o', color='purple', markersize=8, label='Origin (0, 0)')

plt.title('Line x + y = 0 with Direction and Normal Vectors')
plt.xlabel('x-axis')
plt.ylabel('y-axis')

plt.axis('equal')
plt.legend()
plt.grid(True)

plt.xlim(-5, 5)
plt.ylim(-5, 5)

# Save figure
plt.savefig("fig5.png")
plt.show()
