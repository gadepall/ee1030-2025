# Code by /sdcard/github/matgeo/codes/CoordGeoVV Sharma
# September 12, 2023
# Revised July 21, 2024
# Released under GNU GPL
# Section Formula
import sys
sys.path.insert(0, '/workspaces/urban-potato/matgeo/codes/CoordGeo/') 
import numpy as np
import matplotlib.pyplot as plt
from call import find_locus_equation  

locus_equation = find_locus_equation()
 
print(f"Locus equation: {locus_equation}")
fig, ax = plt.subplots(figsize=(8, 8))
  
c1 = plt.Circle((0, 1), 1, color='blue', fill=False, label='$x^2 + (y-1)^2 = 1$')
ax.add_patch(c1)
 
x_vals = np.linspace(-10, 10, 400)
y_vals = x_vals**2 / 4
ax.plot(x_vals, y_vals, 'r-', label=f'Locus: $x^2=4y, y\leq 0$')
ax.plot([0, 0], [-10, 0], 'r-') 
ax.set_title("Locus of the Centre of the Touching Circle")
ax.set_xlabel("x"); ax.set_ylabel("y")
ax.grid(True); ax.axis('equal'); ax.legend()
plt.show()

plt.savefig('fig1.png')
 
