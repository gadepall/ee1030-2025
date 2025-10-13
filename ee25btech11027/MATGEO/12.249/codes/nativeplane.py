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

# Define the three points on the plane as NumPy arrays
p = np.array([2.0, 1.0, 5.0])
q = np.array([-1.0, 3.0, 4.0])
r = np.array([3.0, 0.0, 6.0])

# 1. Create two vectors on the plane
vec_pq = q - p
vec_pr = r - p

# 2. Calculate the cross product using NumPy
normal_vector = np.cross(vec_pq, vec_pr)

print(f"Perpendicular vector (native Python): {normal_vector}")
plot_3d(p, q, r, normal_vector)
