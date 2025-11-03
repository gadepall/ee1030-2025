import os
import ctypes
import numpy as np
import matplotlib.pyplot as plt

# --- Hardcoded inputs from the question ---
a1, b1, c1 = 1, -2, -300
a2, b2, c2 = 6, -1, 70

# --- Compile and Load C Library ---
if os.system("gcc -shared -o word.so -fPIC word.c") != 0:
    print("\nC compilation failed. Exiting.")
    exit()

class Solution(ctypes.Structure):
    _fields_ = [("a", ctypes.c_double), ("b", ctypes.c_double)]

c_lib = ctypes.CDLL(os.path.abspath("word.so"))
c_lib.solve_equations.argtypes = [ctypes.c_double] * 6
c_lib.solve_equations.restype = Solution

# --- Solve by Calling C Function ---
solution = c_lib.solve_equations(a1, b1, c1, a2, b2, c2)
a_sol, b_sol = solution.a, solution.b
print(f"Solution from C: a = {a_sol:.2f}, b = {b_sol:.2f}")

# --- Plot the Graph ---
a_vals = np.linspace(a_sol - 50, a_sol + 50, 400)
b1_vals = (c1 - a1 * a_vals) / b1
b2_vals = (c2 - a2 * a_vals) / b2

plt.figure(figsize=(10, 8))
plt.plot(a_vals, b1_vals, label=f'{a1}a + {b1}b = {c1}')
plt.plot(a_vals, b2_vals, label=f'{a2}a + {b2}b = {c2}')

# Mark the intersection
plt.scatter(a_sol, b_sol, color="red", s=200, marker="*", edgecolors="black",
            label=f'Intersection ({a_sol:.0f}, {b_sol:.0f})')

# Annotate with arrow
plt.annotate(f"({a_sol:.0f}, {b_sol:.0f})",
             (a_sol, b_sol),
             textcoords="offset points",
             xytext=(10,10),
             fontsize=12,
             color="red",
             arrowprops=dict(arrowstyle="->", color="red"))

plt.title("Graphical Solution of Linear Equations", fontsize=16)
plt.xlabel("a-axis", fontsize=12)
plt.ylabel("b-axis", fontsize=12)
plt.grid(True)
plt.legend()
plt.savefig("/media/indhiresh-s/New Volume/Matrix/ee1030-2025/ee25btech11027/MATGEO/5.8.25/figs/figure1.png")
plt.show()
