import ctypes
import numpy as np
import matplotlib.pyplot as plt

# import platform
# print(platform.architecture())

# defining given points
P = np.array([2,1,-1])
Q = np.array([4,4,-7])
O = np.array([0,0,0])

# calling C function to get unit vector
dll = ctypes.CDLL('./main.so')
unit_vector = dll.get_unit_vector
unit_vector.argtypes = [ctypes.POINTER(ctypes.c_double)]
out = np.zeros(3, dtype=np.float64)
unit_vector(out.ctypes.data_as(ctypes.POINTER(ctypes.c_double)))
print(out)  # This is the unit vector
unit_vec = np.array(out) 


# Create 3D plot
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')


# Plot PQ in 3D
ax.plot([P[0], Q[0]], [P[1], Q[1]], [P[2], Q[2]], color='blue', label='PQ', linewidth=2)
# Plot OA in 3D
ax.plot([0, unit_vec[0]], [0, unit_vec[1]], [0, unit_vec[2]], color='red', label='OA', linewidth=2)


# Label points in 3D
ax.scatter(P[0], P[1], P[2], color='blue')
ax.text(P[0], P[1], P[2], 'P', fontsize=12, ha='right', va='bottom')

ax.scatter(Q[0], Q[1], Q[2], color='blue')
ax.text(Q[0], Q[1], Q[2], 'Q', fontsize=12, ha='left', va='bottom')

ax.scatter(O[0], O[1], O[2], color='red')
ax.text(O[0], O[1], O[2], 'O', fontsize=12, ha='right', va='top')

ax.scatter(unit_vec[0], unit_vec[1], unit_vec[2], color='red')
ax.text(unit_vec[0], unit_vec[1], unit_vec[2], 'A', fontsize=12, ha='left', va='top')



#Add labels and legend
ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Z')
ax.legend()
ax.grid(True, linestyle='--', alpha=0.5)

# Save figure as fig.png in the ../figs directory
fig.savefig('../figs/fig.png', dpi=300)
