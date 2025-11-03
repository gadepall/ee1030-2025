import ctypes
import numpy as np

# Load shared library
lib = ctypes.CDLL("./points.so")

# Prepare array for slopes
slopes = (ctypes.c_double * 2)()
lib.compute_slopes(slopes)

slope_given = slopes[0]
slope_perp = slopes[1]

# Known point
x0, y0 = 1, 2

# Equation form: y = mx + c
def line_eqn(m, x0, y0):
    c = y0 - m * x0
    return m, c

m1, c1 = line_eqn(slope_given, x0, y0)
m2, c2 = line_eqn(slope_perp, x0, y0)

print("Given line:        y =", m1, "x +", c1)
print("Perpendicular line: y =", m2, "x +", c2)

