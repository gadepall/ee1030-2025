import math
import sys # for path to external scripts
sys.path.insert(0, '/home/anshu-ram/matgeo/codes/CoordGeo') # path to my scripts
import numpy as np
import numpy.linalg as LA
import matplotlib.pyplot as plt
import matplotlib.image as mpimg

# local imports
from line.funcs import *
from triangle.funcs import *
from conics.funcs import circ_gen

# ========== Functions ==========
def section_point(P, Q, m, n, external=True):
    """
    Finds point dividing PQ in ratio m:n
    If external=True -> external division
    """
    if external:
        return (m*Q - n*P)/(m-n)
    else:
        return (m*Q + n*P)/(m+n)

# ========== Given vectors ==========
a = np.array([1,0]).reshape(-1,1)
b = np.array([0,1]).reshape(-1,1)

P = 2*a + b        # P = 2a + b
Q = a - 3*b        # Q = a - 3b

# Find R (external division in ratio 1:2)
R = section_point(P, Q, 1, 2, external=True)

# ========== Lines ==========
x_PQ = line_gen_num(P, Q, 20)
x_PR = line_gen_num(P, R, 20)
x_QR = line_gen_num(Q, R, 20)

# ========== Plotting ==========
plt.plot(x_PQ[0,:], x_PQ[1,:], "g--", label="Line PQ")
plt.plot(x_PR[0,:], x_PR[1,:], "r--", label="Line PR")
plt.plot(x_QR[0,:], x_QR[1,:], "b--", label="Line QR")

# Points
tri_coords = np.hstack((P,Q,R))   # stack column vectors side by side
plt.scatter(tri_coords[0,:], tri_coords[1,:])


# Labels (rounded to int for clean display)
vert_labels = [
    f'P({int(round(P[0,0]))},{int(round(P[1,0]))})',
    f'Q({int(round(Q[0,0]))},{int(round(Q[1,0]))})',
    f'R({int(round(R[0,0]))},{int(round(R[1,0]))})'
]

for i, txt in enumerate(vert_labels):
    plt.annotate(txt, (tri_coords[0,i], tri_coords[1,i]),
                 textcoords="offset points", xytext=(0,10), ha='right')
plt.xlabel('$x$')
plt.ylabel('$y$')
plt.legend(loc='best')
plt.grid()
plt.title("External Division of PQ (Ratio 1:2)")
plt.axis('equal')

# Save & show
plt.savefig("../figs/section_graph2.png")
plt.show()
