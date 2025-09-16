import math
import sys # for path to external scripts
sys.path.insert(0, '/home/anshu-ram/matgeo/codes/CoordGeo') # left commented — adjust if you use your local helpers
import numpy as np
import numpy.linalg as LA
import matplotlib.pyplot as plt

# Given vertex A
A = np.array([1.0, -1.0]).reshape(-1,1)

# Real k solutions found using norm approach
k_vals = [3.0, -9.0/2.0]

plt.figure(figsize=(6,6))

for k in k_vals:
    B = np.array([-4.0, 2.0*k]).reshape(-1,1)
    C = np.array([-k, -5.0]).reshape(-1,1)
    
    # Triangle coordinates (closed)
    tri = np.hstack((A, B, C, A))
    plt.plot(tri[0,:], tri[1,:], linestyle='-', marker='o', label=f'k={k}')
    
    # compute area using vector cross for verification
    u = (B - A).flatten()
    v = (C - A).flatten()
    cross = abs(u[0]*v[1] - u[1]*v[0])
    area = 0.5*cross
    print(f"k={k} => computed area = {area}")
    
    # annotate vertices
    plt.annotate(f'A(1,-1)', (A[0,0], A[1,0]), textcoords="offset points", xytext=(0,10), ha='center')
    plt.annotate(f'B(-4,{2*k:.2f})', (B[0,0], B[1,0]), textcoords="offset points", xytext=(0,10))
    plt.annotate(f'C({-k:.2f},-5)', (C[0,0], C[1,0]), textcoords="offset points", xytext=(0,-15))

plt.xlabel('x')
plt.ylabel('y')
plt.title('Triangles for real k values')
plt.legend()
plt.axis('equal')
plt.grid(True)
plt.savefig("../figs/triangle_area.png")
plt.show()

