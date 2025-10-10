# Code by GVV Sharma
# Date: Today's Date
# Released under GNU GPL
# Area of Triangle ADE (using .so library)
import sys
import numpy as np
import matplotlib.pyplot as plt
sys.path.insert(0, '/workspaces/urban-potato/matgeo/codes/CoordGeo/') 
# --- Import from our C Interface Module ---
from call import get_all_points

from line.funcs import *
from triangle.funcs import *
from conics.funcs import circ_gen
points=get_all_points()
# This single function call runs the C code and returns all points.
A, B, C, D, E = points

print(f"Midpoint E coordinates: ({E[0]:.1f}, {E[1]:.1f})")
# Calculate and print the area of triangle ADE
area_ADE = 0.5 * np.abs(A[0]*(D[1] - E[1]) + D[0]*(E[1] - A[1]) + E[0]*(A[1] - D[1]))
print(f"The area of Triangle ADE is: {area_ADE}")

# --- Plotting ---
fig, ax = plt.subplots(figsize=(10, 8))

# Draw and fill the shapes
ax.plot(np.vstack([A, B, C, D, A])[:, 0], np.vstack([A, B, C, D, A])[:, 1], 'b-', label='Parallelogram ABCD')
ax.fill(np.vstack([A, D, E, A])[:, 0], np.vstack([A, D, E, A])[:, 1], 'lightgreen', alpha=0.6, label='Triangle ADE')

# Draw the vertices
ax.scatter(points[:, 0], points[:, 1], color='black', s=40)

# Add annotations with specific offsets
ax.annotate(f'A({A[0]:.1f}, {A[1]:.1f})', xy=A, xytext=(-30, -20), textcoords='offset points')
ax.annotate(f'B({B[0]:.1f}, {B[1]:.1f})', xy=B, xytext=(30, -15), textcoords='offset points')
ax.annotate(f'C({C[0]:.1f}, {C[1]:.1f})', xy=C, xytext=(15, 15), textcoords='offset points')
ax.annotate(f'D({D[0]:.1f}, {D[1]:.1f})', xy=D, xytext=(-50, 5), textcoords='offset points')
ax.annotate(f'({E[0]:.1f}, {E[1]:.1f})\nE', xy=E, xytext=(0, 8), textcoords='offset points', ha='center', va='bottom')

# --- Final Formatting ---
ax.set_xlabel('X-axis')
ax.set_ylabel('Y-axis')
ax.set_title('Area of △ADE within Parallelogram ABCD')
ax.grid(True)
ax.axis('equal')
ax.legend()

plt.savefig('fig1.png')
plt.show()