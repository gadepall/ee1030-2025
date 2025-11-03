import ctypes
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# Load shared library
so = ctypes.CDLL("./code.so")

# Function signature
# void find_cube(double n, double *dir_vec, double len_par, double *cube_pts, double *start, double *end)
so.find_cube.argtypes = [
    ctypes.c_double,
    ctypes.POINTER(ctypes.c_double),
    ctypes.c_double,
    ctypes.POINTER(ctypes.c_double),
    ctypes.POINTER(ctypes.c_double)
]
so.find_cube.restype = None

# Inputs
n = 1.0
dir_vec = np.array([2, 1, 3], dtype=np.double)
dir_vec_ptr = dir_vec.ctypes.data_as(ctypes.POINTER(ctypes.c_double))
len_par = 0.5

# Output arrays
cube_pts = (ctypes.c_double*24)()  # 8 points × 3 coords
start_arr = (ctypes.c_double*3)()
end_arr = (ctypes.c_double*3)()

# Call C function
so.find_cube(n, dir_vec_ptr, len_par, cube_pts, start_arr, end_arr)

# Convert outputs to numpy arrays
cube_pts_np = np.array(cube_pts).reshape(8,3)
start = np.array(start_arr)
end = np.array(end_arr)

# Plotting
fig = plt.figure(figsize=(10,10))
ax = fig.add_subplot(111, projection='3d')

# Draw cube edges
edges_idx = [
    (0,1),(1,2),(2,3),(3,0),  # bottom
    (4,5),(5,6),(6,7),(7,4),  # top
    (0,4),(1,5),(2,6),(3,7)   # vertical
]

for i,j in edges_idx:
    s = cube_pts_np[i]
    e = cube_pts_np[j]
    ax.plot([s[0],e[0]], [s[1],e[1]], [s[2],e[2]], 'k--')

# Body diagonals (just as example)
body_diags_idx = [(0,6),(1,7),(2,4),(3,5)]
colors = ['b','g','m','y']
labels = ['d1','d2','d3','d4']

for (i,j),color,label in zip(body_diags_idx,colors,labels):
    s = cube_pts_np[i]
    e = cube_pts_np[j]
    ax.plot([s[0],e[0]], [s[1],e[1]], [s[2],e[2]], color=color, label=label)

# Plot line from C function
ax.plot([start[0],end[0]], [start[1],end[1]], [start[2],end[2]], 'r', label='Line L')

# Labels
ax.set_xlabel("X - AXIS")
ax.set_ylabel("Y - AXIS")
ax.set_zlabel("Z - AXIS")
ax.set_title(r"Line L making angles $\alpha, \beta, \gamma, \delta$ with the body diagonals of a cube")
ax.legend()
ax.set_box_aspect([1,1,1])
ax.view_init(elev=10, azim=135)

plt.savefig("fig_cube_line.png", dpi=300)
plt.show()
