import ctypes
import matplotlib.pyplot as plt
import numpy as np

# --- Load the DLL ---
lib = ctypes.CDLL(r"C:\Users\Navya\code8.dll")
  # <-- change path as needed

# Prepare variables to receive x and y from C
x = ctypes.c_double()
y = ctypes.c_double()

# Call the C function
result = lib.find_intersection(ctypes.byref(x), ctypes.byref(y))
xi, yi = x.value, y.value

print(f"Intersection point: ({xi:.2f}, {yi:.2f})")

if result == 0:
    print("Lines are parallel, no intersection.")
elif result == 1:
    print("The line 5x + 4y = 0 passes through the intersection point.")
else:
    print("The line 5x + 4y = 0 does NOT pass through the intersection point.")

# Plot the lines 
x_vals = np.linspace(-10, 10, 400)

# Line 1: x + 2y = 10 => y = (10 - x)/2
y1 = (10 - x_vals)/2

# Line 2: 2x + y = -5 => y = -5 - 2*x
y2 = -5 - 2*x_vals

# Line 3: 5x + 4y = 0 => y = -5/4 * x
y3 = -5/4 * x_vals

plt.figure(figsize=(8,6))
plt.plot(x_vals, y1, label=r'$(1\ 2)\mathbf{x} = 10$', color='blue')
plt.plot(x_vals, y2, label=r'$(2\ 1)\mathbf{x} = -5$', color='green')
plt.plot(x_vals, y3, label=r'$(5\ 4)\mathbf{x} = 0$', color='red')

# Mark the intersection point
plt.scatter(xi, yi, color='black', zorder=5)
plt.text(xi+0.5, yi, f'({xi:.2f},{yi:.2f})', fontsize=10)

plt.xlabel('x')
plt.ylabel('y')
plt.title('Intersection of Lines')
plt.grid(True)
plt.legend()
plt.xlim(-10, 10)
plt.ylim(-10, 10)

# Save figure as fig8.png
plt.savefig('fig8.png', dpi=300)
plt.show()
