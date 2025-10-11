# File: main.py (Corrected Version)
import ctypes
import numpy as np
import matplotlib.pyplot as plt

# --- Part 1: Call the C function (No changes here) ---
try:
    lib = ctypes.CDLL('./1.so')
    count_m = lib.count_integer_m
    count_m.argtypes = [ctypes.c_int, ctypes.c_int, ctypes.c_int, ctypes.c_int, ctypes.c_int]
    count_m.restype = ctypes.c_int
except OSError as e:
    print("Error loading '1.so'. Please ensure it's compiled and in the same directory.")
    exit()

a1, b1, c1 = 3, 4, 9
m_min, m_max = -10, 10
num_solutions = count_m(a1, b1, c1, m_min, m_max)
print(f"C function reports that there are {num_solutions} integer values for m.")


# --- Part 2: Find the actual integer m values in Python (No changes here) ---
integer_m_values = []
for m in range(m_min, m_max + 1):
    a2, b2, c2 = -m, 1, 1
    det = a1 * b2 - a2 * b1
    num_x = c1 * b2 - b1 * c2
    if det != 0 and num_x % det == 0:
        integer_m_values.append(m)
print(f"The integer values are: {integer_m_values}")


# --- Part 3: Plotting the results on a SINGLE graph ---
x_range = np.linspace(-10, 10, 400)

# 1. Create the figure ONCE before the loop
plt.figure(figsize=(10, 8))

# 2. Plot the main line ONCE before the loop
y1 = (9 - 3 * x_range) / 4
plt.plot(x_range, y1, label='$3x + 4y = 9$', color='black', linewidth=2.5, zorder=5)

# 3. Loop to add the other lines to the SAME figure
for m in integer_m_values:
    y2 = m * x_range + 1
    x_intersect = 5 / (3 + 4 * m)
    y_intersect = m * x_intersect + 1
    
    line = plt.plot(x_range, y2, label=f'$y = {m}x + 1$')
    plt.plot(x_intersect, y_intersect, 'o', markersize=8, color=line[0].get_color(), zorder=10)

# 4. Format and show the single plot ONCE after the loop
plt.title('Combined Plot of Line Intersections (from C call)')
plt.grid(True, linestyle='--', alpha=0.6)
plt.legend()
plt.xlim(-10, 10)
plt.ylim(-10, 10)
plt.gca().set_aspect('equal', adjustable='box')
plt.savefig('1.png')
plt.show()
