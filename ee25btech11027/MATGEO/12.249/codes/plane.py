import ctypes
import os
import numpy as np
import matplotlib.pyplot as plt

def plot_3d(p, q, r, normal):
    """Visualizes the plane, points, and normal vector with coordinate labels."""
    fig = plt.figure(figsize=(10, 8))
    ax = fig.add_subplot(111, projection='3d')

    points = np.array([p, q, r])
    ax.scatter(points[:,0], points[:,1], points[:,2], color='red', s=100)

    # Add text labels with coordinates
    ax.text(p[0], p[1], p[2] + 0.2, f' P({p[0]}, {p[1]}, {p[2]})', color='darkred')
    ax.text(q[0], q[1], q[2] + 0.2, f' Q({q[0]}, {q[1]}, {q[2]})', color='darkred')
    ax.text(r[0], r[1], r[2] + 0.2, f' R({r[0]}, {r[1]}, {r[2]})', color='darkred')
    
    # Create and plot the plane
    d = np.dot(normal, p)
    x_range = np.linspace(min(points[:,0])-2, max(points[:,0])+2, 10)
    y_range = np.linspace(min(points[:,1])-2, max(points[:,1])+2, 10)
    xx, yy = np.meshgrid(x_range, y_range)
    zz = (d - normal[0] * xx - normal[1] * yy) / normal[2]
    ax.plot_surface(xx, yy, zz, alpha=0.4, color='cyan')

    # Plot the normal vector
    ax.quiver(p[0], p[1], p[2], normal[0], normal[1], normal[2],
              length=4, normalize=True, color='black', arrow_length_ratio=0.2, label='Normal Vector')

    ax.set_xlabel('X-axis'); ax.set_ylabel('Y-axis'); ax.set_zlabel('Z-axis')
    ax.set_title('Plane and Perpendicular Vector')
    ax.legend()
    plt.savefig("/media/indhiresh-s/New Volume/Matrix/ee1030-2025/ee25btech11027/MATGEO/12.249/figs/figure1.png")
    plt.show()

class Vector3D(ctypes.Structure):
    _fields_ = [("x", ctypes.c_double), ("y", ctypes.c_double), ("z", ctypes.c_double)]

c_lib_file = 'plane.so'

c_lib = ctypes.CDLL(os.path.abspath(c_lib_file))
c_lib.find_normal_vector_lib.argtypes = [Vector3D, Vector3D, Vector3D, ctypes.POINTER(Vector3D)]
c_lib.find_normal_vector_lib.restype = None

p_pt, q_pt, r_pt = Vector3D(2, 1, 5), Vector3D(-1, 3, 4), Vector3D(3, 0, 6)
normal_out = Vector3D()
c_lib.find_normal_vector_lib(p_pt, q_pt, r_pt, ctypes.byref(normal_out))

normal_vector = np.array([normal_out.x, normal_out.y, normal_out.z])
p_np, q_np, r_np = np.array([p_pt.x, p_pt.y, p_pt.z]), np.array([q_pt.x, q_pt.y, q_pt.z]), np.array([r_pt.x, r_pt.y, r_pt.z])

print(f"Perpendicular vector (from C): {normal_vector}")
plot_3d(p_np, q_np, r_np, normal_vector)
