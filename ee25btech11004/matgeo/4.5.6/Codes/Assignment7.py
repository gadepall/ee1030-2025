import numpy as np
import matplotlib.pyplot as plt
import ctypes


c_lib = ctypes.CDLL('./7cnew.so')



vecA = input("Input the first vector")
vecA.strip()
vecA1, vecA2, vecA3 = vecA.split(" ") 
vecA = np.array([int(vecA1), int(vecA2), int(vecA3)])


vecB = input("Input the second vector")
vecB.strip()
vecB1, vecB2, vecB3 = vecB.split(" ") 
vecB = np.array([int(vecB1), int(vecB2), int(vecB3)])

c_lib.crossx.argtypes = [ctypes.c_int, ctypes.c_int, ctypes.c_int, ctypes.c_int]
c_lib.crossx.restype = ctypes.c_int

answerx = c_lib.crossx(
    ctypes.c_int(vecA[1]),
    ctypes.c_int(vecB[2]), 
    ctypes.c_int(vecA[2]),
    ctypes.c_int(vecB[1])
)

c_lib.crossy.argtypes = [ctypes.c_int, ctypes.c_int, ctypes.c_int, ctypes.c_int]
c_lib.crossy.restype = ctypes.c_int

answery = c_lib.crossy(
    ctypes.c_int(vecA[0]),
    ctypes.c_int(vecB[2]), 
    ctypes.c_int(vecA[2]),
    ctypes.c_int(vecB[0])
)



c_lib.crossz.argtypes = [ctypes.c_int, ctypes.c_int, ctypes.c_int, ctypes.c_int]
c_lib.crossz.restype = ctypes.c_int

answerz = c_lib.crossz(
    ctypes.c_int(vecA[0]),
    ctypes.c_int(vecB[1]), 
    ctypes.c_int(vecA[1]),
    ctypes.c_int(vecB[0])
)

crossvec = np.array([answerx, answery, answerz])
print(crossvec)

# Create a figure and a 3D axes
fig = plt.figure(figsize=(6, 6))
ax = fig.add_subplot(111, projection='3d')

# --- Plane 1: x + 2y = 0 ---
# This is equivalent to x = -2y. The plane is parallel to the z-axis.

# Define the grid for y and z
y1 = np.linspace(-40, 40, 10)
z1 = np.linspace(-40, 40, 10)
Y1, Z1 = np.meshgrid(y1, z1)

# Calculate the corresponding X values
X1 = -2 * Y1

# Plot the first plane with a blue color and some transparency
ax.plot_surface(X1, Y1, Z1, color='b', alpha=0.5, label='x + 2y = 0')

# --- Plane 2: 3y - z = 0 ---
# This is equivalent to z = 3y. The plane is parallel to the x-axis.

# Define the grid for x and y
x2 = np.linspace(-40, 40, 10)
y2 = np.linspace(-40, 40, 10)
X2, Y2 = np.meshgrid(x2, y2)

# Calculate the corresponding Z values
Z2 = 3 * Y2

# Plot the second plane with a red color and some transparency
ax.plot_surface(X2, Y2, Z2, color='g', alpha=0.5, label='3y - z = 0')

# --- Set labels and title ---
ax.set_xlabel('X axis')
ax.set_ylabel('Y axis')
ax.set_zlabel('Z axis')
ax.set_title('Two Intersecting Planes')

# To avoid label overlap issues in some matplotlib versions, we create proxy artists for the legend
import matplotlib.patches as mpatches
blue_patch = mpatches.Patch(color='blue', label='x + 2y = 0')
red_patch = mpatches.Patch(color='green', label='3y - z = 0')
blue_line = mpatches.Patch(color = 'black', label='line')
red_arrow= mpatches.Patch(color = 'red', label='direction vector')
ax.legend(handles=[blue_patch, red_patch, blue_line, red_arrow])



ax.quiver(12,-6,-18, -12, 6 ,18 ,color='red')

P = np.array([-73,38,105]).reshape(-1,1)
Q= np.array([79,-38,-103]).reshape(-1,1)
x_PQ = np.block([P,Q])

ax.plot(x_PQ[0,:],x_PQ[1,:], x_PQ[2,:],label='line', color='black')


plt.show()



plt.show()