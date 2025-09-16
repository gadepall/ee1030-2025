# plot.py
import ctypes
import numpy as np
import matplotlib.pyplot as plt

lib = ctypes.CDLL('./libcode.so')
arr = (ctypes.c_double * 12)()
lib.get_points(arr)
pts = np.array(arr).reshape(4,3)
A, B, C, D = pts

def extend_line(pt1, dir_vec, length=10):
    pt1 = np.array(pt1)
    dir_vec = np.array(dir_vec)
    pt_neg = pt1 - length * dir_vec / np.linalg.norm(dir_vec)
    pt_pos = pt1 + length * dir_vec / np.linalg.norm(dir_vec)
    return pt_neg, pt_pos

# Get direction vectors from code.c (optionally recompute in Python)
dir_AB = B - A
dir_CD = D - C
AB_start, AB_end = extend_line(A, dir_AB)
CD_start, CD_end = extend_line(C, dir_CD)

fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

# Extended lines for visual intersection
ax.plot([AB_start[0], AB_end[0]], [AB_start[1], AB_end[1]], [AB_start[2], AB_end[2]],
        color='blue', label='Line AB', linewidth=2)
ax.plot([CD_start[0], CD_end[0]], [CD_start[1], CD_end[1]], [CD_start[2], CD_end[2]],
        color='green', label='Line CD', linewidth=2)

# Points and labels
ax.scatter(pts[:,0], pts[:,1], pts[:,2], color='red', s=60)
for i, txt in enumerate(['A', 'B', 'C', 'D']):
    ax.text(pts[i,0], pts[i,1], pts[i,2], txt, size=12)

ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Z')
ax.set_title('Perpendicular Lines ')
ax.legend()
plt.show()

