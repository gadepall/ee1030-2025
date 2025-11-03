import ctypes
import numpy as np
import matplotlib.pyplot as plt

# Load the shared library
lib_quadratic = ctypes.CDLL("./code16.so")

# Define the argument types and return type for the C function
lib_quadratic.calculateRootsInfo.argtypes = [
    ctypes.c_double,  # a
    ctypes.c_double,  # b
    ctypes.c_double,  # c
    ctypes.POINTER(ctypes.c_double), # sum_of_roots
    ctypes.POINTER(ctypes.c_double)  # product_of_roots
]
lib_quadratic.calculateRootsInfo.restype = None

# Given quadratic equation: 2x^2 - 9x + 4 = 0
a_given = 2.0
b_given = -9.0
c_given = 4.0

# Create ctypes doubles to hold the results
sum_result = ctypes.c_double()
product_result = ctypes.c_double()

# Call the C function
lib_quadratic.calculateRootsInfo(
    a_given, b_given, c_given,
    ctypes.byref(sum_result),
    ctypes.byref(product_result)
)

sum_of_roots = sum_result.value
product_of_roots = product_result.value

print(f"For the quadratic equation {a_given}x^2 + {b_given}x + {c_given} = 0:")
print(f"The sum of the roots is: {sum_of_roots:.2f}")
print(f"The product of the roots is: {product_of_roots:.2f}")

# --- Part 2: Plotting the parabola and its roots ---

# Calculate the discriminant
delta = b_given**2 - 4 * a_given * c_given

# Find the roots (if real)
roots = []
if delta >= 0:
    root1 = (-b_given + np.sqrt(delta)) / (2 * a_given)
    root2 = (-b_given - np.sqrt(delta)) / (2 * a_given)
    roots.append(root1)
    if root1 != root2: # Add distinct root2 if it exists
        roots.append(root2)
    roots.sort() # Sort for consistent labeling

# Determine plotting range based on roots or a default
if roots:
    min_root = min(roots)
    max_root = max(roots)
    # Expand the range a bit around the roots
    plot_min_x = min_root - (abs(max_root - min_root) * 0.5 + 1)
    plot_max_x = max_root + (abs(max_root - min_root) * 0.5 + 1)
    if plot_min_x == plot_max_x: # Case for a single root
        plot_min_x -= 5
        plot_max_x += 5
else: # If no real roots, use a reasonable default range
    plot_min_x = -5
    plot_max_x = 5

x_vals = np.linspace(plot_min_x, plot_max_x, 400)
y_vals = a_given * x_vals**2 + b_given * x_vals + c_given

plt.figure(figsize=(10, 6))

# Plot the parabola
plt.plot(x_vals, y_vals, label=f'${a_given}x^2 {b_given:+}x {c_given:+} = 0$', color='blue')

# Mark the roots
for i, root in enumerate(roots):
    plt.scatter(root, 0, color='red', s=100, zorder=5, label=f'Root {i+1}: {root:.2f}')
    plt.annotate(f'({root:.2f}, 0)', (root, 0), textcoords="offset points", xytext=(5,5), ha='left', color='red')

# Add x and y axes for reference
plt.axhline(0, color='black', linewidth=0.8, linestyle='--')
plt.axvline(0, color='black', linewidth=0.8, linestyle='--')

plt.xlabel('x')
plt.ylabel('y')
plt.title('Quadratic Parabola and its Real Roots')
plt.grid(True, linestyle=':', alpha=0.7)
plt.legend()
plt.ylim(min(y_vals)-abs(min(y_vals)*0.1)-1, max(y_vals)+abs(max(y_vals)*0.1)+1) # Adjust y-limits dynamically
plt.xlim(plot_min_x, plot_max_x) # Ensure x-limits are set
plt.show()
