import sys
import numpy as np
import matplotlib.pyplot as plt

# path to your external scripts
sys.path.insert(0, '/home/anshu-ram/matgeo/codes/CoordGeo')

# local imports
from line.funcs import line_gen_num

# ========== Given vectors ==========
A = np.array([6, 5]).reshape(-1,1)
B = np.array([-4, 3]).reshape(-1,1)
O = np.array([0, 9]).reshape(-1,1)

# ========== Lines ==========
x_AB = line_gen_num(A, B, 20)
x_OA = line_gen_num(O, A, 20)
x_OB = line_gen_num(O, B, 20)

# ========== Plotting ==========
plt.plot(x_AB[0,:], x_AB[1,:], "g--", label="Line AB")
plt.plot(x_OA[0,:], x_OA[1,:], "r--", label="Line OA")
plt.plot(x_OB[0,:], x_OB[1,:], "b--", label="Line OB")

# Points
tri_coords = np.hstack((A,B,O))   # stack column vectors
plt.scatter(tri_coords[0,:], tri_coords[1,:])

# Labels
vert_labels = [
    f'A({int(A[0,0])},{int(A[1,0])})',
    f'B({int(B[0,0])},{int(B[1,0])})',
    f'O({int(O[0,0])},{int(O[1,0])})'
]

for i, txt in enumerate(vert_labels):
    plt.annotate(txt, (tri_coords[0,i], tri_coords[1,i]),
                 textcoords="offset points", xytext=(0,10), ha='right')

plt.xlabel('$x$')
plt.ylabel('$y$')
plt.legend(loc='best')
plt.grid()
plt.title("Point O(0,9) equidistant from A and B")
plt.axis('equal')

# Save & show
plt.savefig("../figs/equidistant_point.png")
plt.show()

