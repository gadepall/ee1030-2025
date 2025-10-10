import sys
import math
import sys
import numpy as np
import numpy.linalg as LA
import matplotlib.pyplot as plt
import matplotlib.image as mpimg

# local imports
from libs.line.funcs import *
from libs.triangle.funcs import *

# if using termux
# import subprocess
# import shlex

def section_formula(A, B, k):
    return (1*A + k*B) / (k + 1)

# Given points
A = np.array([-5, 8]).reshape(-1, 1)
B = np.array([4, -10]).reshape(-1, 1)

# Given y-coordinate of P
yP = 4

# Compute k so that P = (A + k B)/(1 + k) has y-coordinate = yP
# Solve: yP = (A_y + k*B_y) / (1 + k)
k = (A[1,0] - yP) / (yP - B[1,0])

# Reduce ratio AP:PB = k:1 to integers
num, den = int(round(k)), 1
g = math.gcd(num, den)
num //= g
den //= g

# Compute P
P = section_formula(A, B, k).reshape(-1, 1)

# Print results
print(f"Ratio AP:PB = {num}:{den}")
print(f"Value of x at P = {P[0,0]}")

# Plotting (same style as your template)
x_AB = line_gen_num(A, B, 20)
plt.plot(x_AB[0, :], x_AB[1, :], 'g--', label="Line Segment AB")

plot_coords = np.block([[A, B, P]])
plt.scatter(plot_coords[0, :], plot_coords[1, :], color='blue')

vert_labels = [
    f'A({A[0,0]}, {A[1,0]})',
    f'B({B[0,0]}, {B[1,0]})',
    f'P({P[0,0]:.2f}, {P[1,0]:.2f})'
]

for i, txt in enumerate(vert_labels):
    plt.annotate(txt,
                 (plot_coords[0, i], plot_coords[1, i]),
                 textcoords="offset points",
                 xytext=(0, 10),
                 ha='center')

plt.xlabel('$x$')
plt.ylabel('$y$')
plt.title("Division of Line Segment AB by Point P")
plt.legend(loc='best')
plt.grid()
plt.axis('equal')

plt.savefig("../figs/plot_p.jpg")
plt.show()

