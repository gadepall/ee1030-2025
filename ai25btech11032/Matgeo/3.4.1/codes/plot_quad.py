import ctypes
import matplotlib.pyplot as plt

# 1) load the compiled C library
lib = ctypes.CDLL("./libquad.so")

# tell Python about the function signature
lib.get_vertices.argtypes = [ctypes.POINTER(ctypes.c_double * 8)]
lib.get_vertices.restype = None

# 2) create an array of 8 doubles and call C
vertices = (ctypes.c_double * 8)()
lib.get_vertices(vertices)

# 3) convert to Python list of tuples [(x,y),...]
coords = [(vertices[i], vertices[i+1]) for i in range(0, 8, 2)]
A, B, C, D = coords

# 4) plotting
xs = [A[0], B[0], C[0], D[0], A[0]]
ys = [A[1], B[1], C[1], D[1], A[1]]

fig, ax = plt.subplots()
ax.plot(xs, ys, marker='o')

labels = ['A(-4,5)', 'B(0,7)', 'C(5,-5)', 'D(-4,-2)']
for (x, y), lab in zip(coords, labels):
    ax.annotate(lab, (x, y))

ax.set_aspect('equal', adjustable='box')
ax.set_title('Quadrilateral ABCD')
plt.savefig("quad_only.png")
plt.show()

