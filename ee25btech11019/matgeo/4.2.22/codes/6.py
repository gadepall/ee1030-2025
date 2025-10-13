#!/usr/bin/env python3
# plot_parallel_ctypes.py
import ctypes
import numpy as np
import matplotlib.pyplot as plt
import os

# Load shared library (adjust path if needed)
libpath = os.path.join('.', '6.so')
lib = ctypes.CDLL(libpath)

# Declare function signatures
lib.is_parallel.argtypes = [ctypes.c_double, ctypes.c_double, ctypes.c_double, ctypes.c_double]
lib.is_parallel.restype = ctypes.c_int

lib.eval_line.argtypes = [
    ctypes.c_double, ctypes.c_double, ctypes.c_double,
    ctypes.POINTER(ctypes.c_double), ctypes.POINTER(ctypes.c_double),
    ctypes.c_int
]
lib.eval_line.restype = None

def check_parallel(a1, b1, a2, b2):
    return bool(lib.is_parallel(a1, b1, a2, b2))

def eval_line(a, b, c, xs):
    n = len(xs)
    XTYPE = ctypes.c_double * n
    x_arr = XTYPE(*xs)
    y_arr = XTYPE()  # will be filled by C
    lib.eval_line(ctypes.c_double(a), ctypes.c_double(b), ctypes.c_double(c),
                  x_arr, y_arr, ctypes.c_int(n))
    return np.array([y_arr[i] for i in range(n)])

# ------------------ Example usage ------------------
# Change coefficients below to plot different lines
a1, b1, c1 = 2.0, 4.0, 1.0    # line1: 2x + 4y + 1 = 0  (slope -a1/b1 = -0.5)
a2, b2, c2 = 1.0, 2.0, -3.0   # line2: 1x + 2y - 3 = 0  (slope -0.5) -> parallel to line1

print("Line 1: {} x + {} y + {} = 0".format(a1, b1, c1))
print("Line 2: {} x + {} y + {} = 0".format(a2, b2, c2))
print("Are the lines parallel? ->", check_parallel(a1, b1, a2, b2))

# Choose x-range for plotting. Use x-intercepts to center plot a bit.
def x_intercept(a,c):
    # x when y=0 -> -c/a (if a != 0)
    return (-c / a) if abs(a) > 1e-12 else 0.0

xints = [x_intercept(a1,c1), x_intercept(a2,c2)]
xmin = min(xints) - 5
xmax = max(xints) + 5
xs = np.linspace(xmin, xmax, 600)

ys1 = eval_line(a1, b1, c1, xs)
ys2 = eval_line(a2, b2, c2, xs)

# Plot
plt.figure(figsize=(9,6))
plt.plot(xs, ys1, label=f'{a1}x + {b1}y + {c1} = 0', linewidth=2)
plt.plot(xs, ys2, '--', label=f'{a2}x + {b2}y + {c2} = 0', linewidth=2)

# Annotate sample points at x0 (choose center)
x0 = 0.0
y1_x0 = (-a1 * x0 - c1) / b1
y2_x0 = (-a2 * x0 - c2) / b2

plt.scatter([x0, x0], [y1_x0, y2_x0], color=['red','blue'], zorder=5)
plt.annotate(f'P1 ({x0:.2f}, {y1_x0:.2f})', (x0, y1_x0),
             xytext=(8, -12), textcoords='offset points', fontsize=9)
plt.annotate(f'P2 ({x0:.2f}, {y2_x0:.2f})', (x0, y2_x0),
             xytext=(8, 8), textcoords='offset points', fontsize=9)

plt.xlabel('x')
plt.ylabel('y')
plt.title('Two lines (checked via C functions) — parallel if slopes equal')
plt.grid(True)
plt.legend()
plt.axis('equal')   # tries to use equal scaling on both axes
plt.xlim(xmin, xmax)
plt.tight_layout()
plt.savefig('parallel_lines_ctypes.png', dpi=150)
print("Saved plot to parallel_lines_ctypes.png")
plt.show()
