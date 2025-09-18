import numpy as np
from ctypes import CDLL, c_double, c_int, POINTER

import matplotlib.pyplot as plt

lib = CDLL('./libmatfun.so')
lib.check_line_validity.argtypes = [np.ctypeslib.ndpointer(dtype=np.double, ndim=1, flags='C_CONTIGUOUS'),
                                   np.ctypeslib.ndpointer(dtype=np.double, ndim=1, flags='C_CONTIGUOUS')]
lib.check_line_validity.restype = c_int

lib.prepare_line_points.argtypes = [np.ctypeslib.ndpointer(dtype=np.double, flags='C_CONTIGUOUS'),
                                    np.ctypeslib.ndpointer(dtype=np.double, flags='C_CONTIGUOUS'),
                                    c_double, c_double, c_int,
                                    np.ctypeslib.ndpointer(dtype=np.double, flags='C_CONTIGUOUS')]
lib.prepare_line_points.restype = None

lines = [
    (np.array([1.,1.,1.]), np.array([0.,-5.,4.])),
    (np.array([6.,3.,-2.]), np.array([-5.,4.,-5.])),
    (np.array([0.,4.,4.]), np.array([0.,20.,45.])),
    (np.array([0.,0.,2.]), np.array([0.,4.,3.])),
]

results = []
for i, (r0, d) in enumerate(lines):
    valid = lib.check_line_validity(r0, d)
    results.append(bool(valid))
    print(f"Edge {chr(65+i)} valid? {bool(valid)}")

def plot_planes_and_lines(lines, validity):
    fig = plt.figure(figsize=(6,6))
    ax = fig.add_subplot(111, projection='3d')

    # Plot planes same as before
    n1 = np.array([10,15,12])
    d1 = 60
    n2 = np.array([-2,5,4])
    d2 = 20

    xx, yy = np.meshgrid(np.linspace(-10,10,20), np.linspace(-10,10,20))
    zz1 = (d1 - 10*xx - 15*yy)/12
    zz2 = (d2 + 2*xx - 5*yy)/4

    ax.plot_surface(xx, yy, zz1, color='lightblue', alpha=0.5)
    ax.plot_surface(xx, yy, zz2, color='lightpink', alpha=0.5)

    colors = ['r','g','b','m']
    labels = ['A','B','C','D']

    for i,(r0,d) in enumerate(lines):
        if validity[i]:
            num_points = 100
            output = np.zeros(num_points*3, dtype=np.double)
            lib.prepare_line_points(r0, d, -1.0, 1.0, num_points, output)
            points = output.reshape((num_points, 3))
            ax.plot(points[:,0], points[:,1], points[:,2], color=colors[i], linewidth=3, label=f'Edge {labels[i]}')

    ax.set_xlabel('x')
    ax.set_ylabel('y')
    ax.set_zlabel('z')
    ax.legend()
    ax.set_title('Planes and Valid Tetrahedron Edges Using Shared Library')
    plt.show()

plot_planes_and_lines(lines, results)
