# Code to plot y = x and y = x^2 and their intersection points
# Based on GVV Sharma's structure
# Corrected and updated: Sep 30, 2025

import numpy as np
import matplotlib.pyplot as plt
import sys

# Path to custom geometry modules
sys.path.insert(0, '/sdcard/github/matgeo/codes/CoordGeo')

# Local imports (from your repo)
from line.funcs import line_norm
from conics.funcs import conic_param, parab_param, parab_gen

# Termux (Android) support
import subprocess
import shlex

# Define unit vectors (if needed)
e1 = np.array([[1], [0]])
e2 = np.array([[0], [1]])

# Set up plot
fig = plt.figure()
ax = fig.add_subplot(111, aspect='equal')

# =========================
# ✅ Parabola: y = x^2
# =========================

# Conic form: x^T V x + 2u^T x + f = 0
V = np.array([[1, 0], [0, 0]])                   # x^2 term
u = np.array([[0], [-1/2]])                      # -y term → 2u^T x = -y
f = 0                                            # constant term

# Get conic parameters using your functions
n, c, F, O, lam, P, e = conic_param(V, u, f)

# Generate parabola in standard form, then apply affine transform
flen = parab_param(lam, P, u)
y_vals = np.linspace(-2, 2, 100)
x_parab = parab_gen(y_vals, flen)
x_parab_affine = P @ x_parab + O

# Plot parabola
plt.plot(x_parab_affine[0,:], x_parab_affine[1,:], label='$y = x^2$', color='red')

# =========================
# ✅ Line: y = x
# =========================

# Line in normal vector form: (1, -1)^T x = 0
n_line = np.array([[1], [-1]])
c_line = 0
x_line = line_norm(n_line, c_line, -2, 2)

# Plot line
plt.plot(x_line[0,:], x_line[1,:], label='$y = x$', color='blue')

# =========================
# ✅ Intersection Points
# =========================

P1 = np.array([[0], [0]])
P2 = np.array([[1], [1]])
intersections = np.hstack((P1, P2))

# Plot intersection points
plt.scatter(intersections[0,:], intersections[1,:], color='black', zorder=5)
labels = ['(0, 0)', '(1, 1)']
for i, txt in enumerate(labels):
    plt.annotate(txt,
                 (intersections[0,i], intersections[1,i]),
                 textcoords="offset points",
                 xytext=(0,10), ha='center')

# =========================
# ✅ Axes and Display
# =========================

# Axes through origin
ax.spines['top'].set_color('none')
ax.spines['right'].set_color('none')
ax.spines['left'].set_position('zero')
ax.spines['bottom'].set_position('zero')

# Labels, legend, grid
plt.xlabel('$x$')
plt.ylabel('$y$')
plt.title('Graphs of $y = x^2$ and $y = x$ with Intersections')
plt.legend()
plt.grid(True)
plt.axis('equal')

# =========================
# ✅ Save and Show
# =========================

plt.savefig('chapters/11/11/2/2/figs/line_parabola_intersections.pdf')
subprocess.run(shlex.split("termux-open chapters/11/11/2/2/figs/line_parabola_intersections.pdf"))

# For desktop use, uncomment:
# plt.show()
