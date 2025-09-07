import numpy as np
import matplotlib.pyplot as plt
import os

# Create figs directory if not exists
os.makedirs("figs", exist_ok=True)

# Define vectors
a = np.array([1, -7, 7])
b = np.array([3, -2, 2])

# Cross product
n = np.cross(a, b)

# Magnitude of cross product
magnitude = np.linalg.norm(n)

# Unit vector
unit = n / magnitude

# Print results
print("Vector a:", a)
print("Vector b:", b)
print("Cross product (a × b):", n)
print("Magnitude of cross product:", magnitude)
print("Unit vector perpendicular to a and b:", unit)

# Save results to text file
results_path = "figs/results.txt"
with open(results_path, "w") as f:
    f.write("Vector a: " + str(a) + "\n")
    f.write("Vector b: " + str(b) + "\n")
    f.write("Cross product (a × b): " + str(n) + "\n")
    f.write("Magnitude of cross product: " + str(magnitude) + "\n")
    f.write("Unit vector perpendicular to a and b: " + str(unit) + "\n")

print(f"Results saved at: {os.path.abspath(results_path)}")

# Plotting
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

# Plot vectors a, b, and unit vector
ax.quiver(0, 0, 0, a[0], a[1], a[2], color='r', label='a')
ax.quiver(0, 0, 0, b[0], b[1], b[2], color='g', label='b')
ax.quiver(0, 0, 0, unit[0], unit[1], unit[2], color='b', label='Unit vector')

# Set axes labels
ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Z')
ax.legend()
ax.set_title("Vectors a, b and perpendicular unit vector")

# Save figure
save_path = "figs/vectors.png"
plt.savefig(save_path)
print(f"Figure saved at: {os.path.abspath(save_path)}")

plt.show()
