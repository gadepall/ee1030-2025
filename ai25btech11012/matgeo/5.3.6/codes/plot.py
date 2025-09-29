#Code by Unnathi Garige

#Line plotting: 3x - y + 8 = 0

import sys
import numpy as np
import matplotlib.pyplot as plt

sys.path.insert(0, '/Users/unnathi/Documents/matgeo/codes/CoordGeo')  
from line.funcs import *
from triangle.funcs import *
from conics.funcs import circ_gen
# Line: 3x - y + 8 = 0
n = np.array(([3, -1])).reshape(-1,1)   # normal vector
c = -8                                  # constant term

# Generate line points
k1, k2 = -5, 5
x_vals = line_norm(n, c, k1, k2)

# Plot the line
plt.plot(x_vals[0,:], x_vals[1,:], label='$3x - y + 8 = 0$')

# Axes setup
ax = plt.gca()
ax.spines['top'].set_color('none')
ax.spines['left'].set_position('zero')
ax.spines['right'].set_color('none')
ax.spines['bottom'].set_position('zero')

plt.legend(loc='best')
plt.grid()
plt.axis('equal')

# Save or show
plt.savefig('/Users/unnathi/Documents/ee1030-2025/ai25btech11012/matgeo/5.3.6/figs ')   # saves to file
plt.show()                   # uncomment to display

