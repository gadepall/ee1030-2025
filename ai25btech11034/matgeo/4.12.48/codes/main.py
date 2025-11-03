import ctypes
import numpy as np
import matplotlib.pyplot as plt

# Load C library
lib = ctypes.CDLL("./function.so")
lib.check_condition.argtypes = [ctypes.c_double, ctypes.c_double, ctypes.c_double, ctypes.c_double]
lib.check_condition.restype = ctypes.c_int

# Input intercepts
a = float(input("Enter intercept a on x-axis: "))
b = float(input("Enter intercept b on y-axis: "))
c = float(input("Enter intercept c on z-axis: "))

# Equation of plane: x/a + y/b + z/c = 1
# Distance of plane from origin
p = 1 / np.sqrt((1/a**2) + (1/b**2) + (1/c**2))

# Check condition using C function
res = lib.check_condition(a, b, c, p)

print(f"\nEquation of Plane: x/{a} + y/{b} + z/{c} = 1")
print(f"Distance from origin (p) = {p:.4f}")

if res == 1:
    print("✅ Condition satisfied: 1/a² + 1/b² + 1/c² = 1/p²")
else:
    print("❌ Condition not satisfied")

# Plotting plane
fig = plt.figure()
ax = fig.add_subplot(111, projection="3d")

# Create mesh grid
x = np.linspace(0, a, 20)
y = np.linspace(0, b, 20)
X, Y = np.meshgrid(x, y)
Z = c * (1 - X/a - Y/b)

# Plot plane
ax.plot_surface(X, Y, Z, alpha=0.5, color='cyan')

# Plot intercept points
ax.scatter(a, 0, 0, color='r', s=60, label="(a,0,0)")
ax.scatter(0, b, 0, color='g', s=60, label="(0,b,0)")
ax.scatter(0, 0, c, color='b', s=60, label="(0,0,c)")

# Labels
ax.set_xlabel("X")
ax.set_ylabel("Y")
ax.set_zlabel("Z")
ax.legend()
ax.set_title("Intercept Plane")

# Save figure
plt.savefig("../figures/intercept_plane.png", dpi=300)
plt.show()

