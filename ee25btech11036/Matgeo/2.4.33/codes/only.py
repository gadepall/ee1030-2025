
import sys
sys.path.insert(0, '/home/chanakya/MATGEO/2.4.33/codes')   # path to local scripts
import numpy as np
import numpy.linalg as LA
import matplotlib.pyplot as plt

# local imports
from libs.line.funcs import *

# Function to compute squared distance
def dist2(P, Q):
    return LA.norm(P-Q)**2

# Given points
A = np.array([-5, 6]).reshape(-1,1)
B = np.array([-4, -2]).reshape(-1,1)
C = np.array([7, 5]).reshape(-1,1)

# Distances squared
AB2 = dist2(A,B)
BC2 = dist2(B,C)
CA2 = dist2(C,A)

# Determine type
triangle_type = []
if np.isclose(AB2, BC2) or np.isclose(BC2, CA2) or np.isclose(CA2, AB2):
    triangle_type.append("Isosceles")
else:
    triangle_type.append("Scalene")

if (np.isclose(AB2+BC2, CA2) or
    np.isclose(BC2+CA2, AB2) or
    np.isclose(CA2+AB2, BC2)):
    triangle_type.append("Right-angled")

triangle_type = " ".join(triangle_type)

# Generate triangle sides
x_AB = line_gen(A,B)
x_BC = line_gen(B,C)
x_CA = line_gen(C,A)

# Plotting
plt.plot(x_AB[0,:], x_AB[1,:], label='$AB$')
plt.plot(x_BC[0,:], x_BC[1,:], label='$BC$')
plt.plot(x_CA[0,:], x_CA[1,:], label='$CA$')

# Labeling the coordinates
tri_coords = np.block([[A,B,C]])
vert_labels = ['A','B','C']
for i, txt in enumerate(vert_labels):
    plt.annotate(f'{txt}({int(tri_coords[0,i])},{int(tri_coords[1,i])})',
                 (tri_coords[0,i], tri_coords[1,i]),
                 textcoords="offset points",
                 xytext=(20,5), ha='center')

# Show triangle type at centroid
centroid = (A+B+C)/3
plt.text(centroid[0,0], centroid[1,0],
         f"{triangle_type} Triangle",
         fontsize=12, color='green',
         bbox=dict(facecolor='yellow', alpha=0.3, edgecolor='black'))

# Axes formatting
ax = plt.gca()
ax.spines['top'].set_color('none')
ax.spines['right'].set_color('none')
ax.spines['left'].set_position('zero')
ax.spines['bottom'].set_position('zero')

plt.grid()
plt.axis('equal')
plt.legend(loc='best')
plt.title("Triangle ABC with Classification")
plt.show()

