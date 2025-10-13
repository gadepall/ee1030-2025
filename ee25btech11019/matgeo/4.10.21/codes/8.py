import ctypes
import numpy as np
import matplotlib.pyplot as plt

# Load the compiled C library
lib = ctypes.CDLL("./8.so")

# Tell Python how the function looks in C
lib.intersection_point.argtypes = [ctypes.POINTER(ctypes.c_double),
                                   ctypes.POINTER(ctypes.c_double),
                                   ctypes.POINTER(ctypes.c_double)]

# Create variables to receive the output
x = ctypes.c_double()
y = ctypes.c_double()
z = ctypes.c_double()

# Call the C function
lib.intersection_point(ctypes.byref(x), ctypes.byref(y), ctypes.byref(z))
P = np.array([x.value, y.value, z.value])

# Given points
A = np.array([0, -1, -1])
B = np.array([4, 5, 1])
C = np.array([3, 9, 4])
D = np.array([-4, 4, 4])

# Create line coordinates
t = np.linspace(-1, 3, 20)
AB_line = A[np.newaxis, :] + t[:, np.newaxis] * (B - A)
CD_line = C[np.newaxis, :] + t[:, np.newaxis] * (D - C)

# Plot setup
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

# Plot the two lines
ax.plot(AB_line[:,0], AB_line[:,1], AB_line[:,2], 'b', label='Line AB')
ax.plot(CD_line[:,0], CD_line[:,1], CD_line[:,2], 'r', label='Line CD')

# Plot the intersection point
ax.scatter(P[0], P[1], P[2], color='green', s=60)
ax.text(P[0], P[1], P[2], f"P{tuple(P.round(2))}", color='black')

# Label the endpoints
for name, pt in zip(['A','B','C','D'], [A,B,C,D]):
    ax.scatter(pt[0], pt[1], pt[2])
    ax.text(pt[0], pt[1], pt[2], name)

ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Z')
ax.legend()
plt.title("Intersection of Lines AB and CD")
plt.show()

