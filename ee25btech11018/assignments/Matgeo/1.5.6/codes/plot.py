import sys
import math
sys.path.insert(0, '/home/darisy-sreetej/Downloads/codes/CoordGeo')

import numpy as np
import numpy.linalg as LA
import matplotlib.pyplot as plt
import matplotlib.image as mpimg

# local imports
from line.funcs import *
from triangle.funcs import *

# Points A and B
A = np.array([7, -6])
B = np.array([3, 4])

# Ratio m:n = 1:2
m, n = 1, 2

# Section formula in vector form: P = (nA + mB) / (m+n)
P = (n*A + m*B) / (m+n)

# Generate line coordinates for plotting
line_AB = line_gen(A, B)

# Plotting
plt.plot(line_AB[0,:], line_AB[1,:], label="Line AB")  # Line AB
plt.scatter(A[0], A[1], color='red', label='A(7,-6)')
plt.scatter(B[0], B[1], color='blue', label='B(3,4)')
plt.scatter(P[0], P[1], color='green', label=f'P({P[0]:.2f},{P[1]:.2f})')

# Add text labels
plt.text(A[0], A[1], ' A(7,-6)', fontsize=10)
plt.text(B[0], B[1], ' B(3,4)', fontsize=10)
plt.text(P[0], P[1], f' P({P[0]:.2f},{P[1]:.2f})', fontsize=10)

# Formatting
plt.xlabel('x-axis')
plt.ylabel('y-axis')
plt.legend()
plt.grid(True)
plt.axis('equal')
plt.title("Point dividing AB in ratio 1:2")
plt.savefig("../figs/plot.png")
plt.show()

