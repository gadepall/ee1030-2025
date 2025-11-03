import numpy as np 
from mpl_toolkits.mplot3d import Axes3D
from mpl_toolkits.mplot3d.art3d import Poly3DCollection
import ctypes
import matplotlib.pyplot as plt

# Load the shared object file
main_lib = ctypes.CDLL('./main.so')


# Define input and return types for the C function
a = np.array([3, 1, 4],dtype=np.float64)
b = np.array([1, -1, 1],dtype=np.float64)

main_lib.main.argtypes = [ctypes.POINTER(ctypes.c_double), 
    ctypes.POINTER(ctypes.c_double)]

main_lib.main.restype = ctypes.c_double

# Call the C function to calculate the area
area_value = main_lib.main(a.ctypes.data_as(ctypes.POINTER(ctypes.c_double)), 
	b.ctypes.data_as(ctypes.POINTER(ctypes.c_double)))

print(f"Python :  {area_value}")

area = area_value

O = np.array([0, 0, 0])

fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

# Plot vectors OA and OB
ax.quiver(*O, *a, color='r', label='OA')
ax.quiver(*O, *b, color='b', label='OB')
ax.text(a[0], a[1], a[2], 'OA', color='r', fontsize=12)
ax.text(b[0], b[1], b[2], 'OB', color='b', fontsize=12)

verts = [ [O, a, a+b, b] ]
ax.add_collection3d(Poly3DCollection(verts, alpha=0.3, facecolor='green'))

# Set limits and labels
ax.set_xlim([0, max(a[0], b[0], a[0]+b[0])+1])
ax.set_ylim([min(0, a[1], b[1], a[1]+b[1])-1, max(a[1], b[1], a[1]+b[1])+1])
ax.set_zlim([0, max(a[2], b[2], a[2]+b[2])+1])
ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Z')
ax.legend()

# Set the graph title to the area value
ax.set_title(f'Area = {area}')

plt.tight_layout()
plt.savefig('../figs/fig.png')
plt.close()