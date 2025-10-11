# call_planes.py
from ctypes import CDLL, c_double
import math
import numpy as np
import matplotlib.pyplot as plt

# Load library
lib = CDLL('./libplanes.so')
lib.equal_inclined_planes.argtypes = (c_double, c_double * 8)
lib.equal_inclined_planes.restype = None

# Prepare output array
coeffs = (c_double * 8)()
distance = 3.0 * math.sqrt(3.0)

# Call C function
lib.equal_inclined_planes(distance, coeffs)

# Extract coefficients
a1,b1,c1,d1 = coeffs[0], coeffs[1], coeffs[2], coeffs[3]
a2,b2,c2,d2 = coeffs[4], coeffs[5], coeffs[6], coeffs[7]

print(f"Plane 1: {a1}x + {b1}y + {c1}z = {d1}")
print(f"Plane 2: {a2}x + {b2}y + {c2}z = {d2}")

# -------------------
# Plotting
# -------------------
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

# Grid for plotting planes
xx, yy = np.meshgrid(np.linspace(-10,10,20), np.linspace(-10,10,20))

# Plane 1: z = (d1 - a1*xx - b1*yy)/c1
zz1 = (d1 - a1*xx - b1*yy)/c1
ax.plot_surface(xx, yy, zz1, alpha=0.3, color='cyan')

# Plane 2: z = (d2 - a2*xx - b2*yy)/c2
zz2 = (d2 - a2*xx - b2*yy)/c2
ax.plot_surface(xx, yy, zz2, alpha=0.3, color='magenta')

# Origin
ax.scatter(0,0,0, color='black', s=60, label="Origin")

ax.set_xlabel("X")
ax.set_ylabel("Y")
ax.set_zlabel("Z")
ax.legend()
plt.show()
