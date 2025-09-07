import ctypes
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import os

# Load the shared library
lib = ctypes.CDLL('./plane.so')

# Define the Point3D structure for ctypes
class Point3D(ctypes.Structure):
    _fields_ = [("x", ctypes.c_double),
                ("y", ctypes.c_double), 
                ("z", ctypes.c_double)]

class Vector3D(ctypes.Structure):
    _fields_ = [("x", ctypes.c_double),
                ("y", ctypes.c_double),
                ("z", ctypes.c_double)]

# Define function signatures
lib.solve_point_to_plane_distance.argtypes = [Point3D, Point3D, Point3D, Point3D, ctypes.POINTER(Point3D)]
lib.solve_point_to_plane_distance.restype = ctypes.c_double

def read_points_from_file(filename):
    """Read points from the data file"""
    points = {}

    if not os.path.exists(filename):
        print(f"File {filename} not found. Running C program first...")
        # If points.dat doesn't exist, we need to run the C program
        os.system('make main')

    with open(filename, 'r') as f:
        for line in f:
            parts = line.strip().split()
            if len(parts) == 4:
                label = parts[0]
                x, y, z = map(float, parts[1:])
                points[label] = (x, y, z)

    return points

def create_visualization(points):
    """Create 3D visualization of points and plane"""
    fig = plt.figure(figsize=(12, 10))
    ax = fig.add_subplot(111, projection='3d')

    # Extract point coordinates
    A = np.array(points['A'])
    B = np.array(points['B'])
    C = np.array(points['C'])
    P = np.array(points['P'])
    Q = np.array(points['Q'])

    # Plot the points
    ax.scatter(*A, color='red', s=100, label='A(3,-1,2)')
    ax.scatter(*B, color='green', s=100, label='B(5,2,4)')
    ax.scatter(*C, color='blue', s=100, label='C(-1,-1,6)')
    ax.scatter(*P, color='orange', s=150, label='P(6,5,9)', marker='^')
    ax.scatter(*Q, color='purple', s=120, label='Q (foot of perpendicular)', marker='s')

    # Add text labels for points
    ax.text(A[0], A[1], A[2], '  A', fontsize=12)
    ax.text(B[0], B[1], B[2], '  B', fontsize=12)
    ax.text(C[0], C[1], C[2], '  C', fontsize=12)
    ax.text(P[0], P[1], P[2], '  P', fontsize=12)
    ax.text(Q[0], Q[1], Q[2], '  Q', fontsize=12)

    # Draw line from P to Q (perpendicular distance)
    ax.plot([P[0], Q[0]], [P[1], Q[1]], [P[2], Q[2]], 'k--', linewidth=2, label='Perpendicular distance')

    # Create the plane surface
    # We need to create a grid for the plane
    # The plane equation is 3x - 4y + 3z = 19
    # Solving for z: z = (19 - 3x + 4y) / 3

    # Create a grid around the points
    all_points = np.array([A, B, C, P, Q])
    x_min, x_max = all_points[:, 0].min() - 2, all_points[:, 0].max() + 2
    y_min, y_max = all_points[:, 1].min() - 2, all_points[:, 1].max() + 2

    xx, yy = np.meshgrid(np.linspace(x_min, x_max, 20), np.linspace(y_min, y_max, 20))
    zz = (19 - 3*xx + 4*yy) / 3

    # Plot the plane
    ax.plot_surface(xx, yy, zz, alpha=0.3, color='lightblue')

    # Draw triangle ABC on the plane to show the plane boundary
    triangle_x = [A[0], B[0], C[0], A[0]]
    triangle_y = [A[1], B[1], C[1], A[1]]
    triangle_z = [A[2], B[2], C[2], A[2]]
    ax.plot(triangle_x, triangle_y, triangle_z, 'r-', linewidth=2, label='Triangle ABC')

    # Set labels and title
    ax.set_xlabel('X')
    ax.set_ylabel('Y')
    ax.set_zlabel('Z')
    ax.set_title('4.7.64')
    ax.legend()

    # Set equal aspect ratio
    ax.set_box_aspect([1,1,1])

    # Save the figure
    plt.tight_layout()
    plt.savefig('fig1.png', dpi=300, bbox_inches='tight')
    plt.close()

    print("Visualization saved as fig1.png")

def main():
    """Main function"""
    # Define the points from the problem
    A = Point3D(3.0, -1.0, 2.0)
    B = Point3D(5.0, 2.0, 4.0)
    C = Point3D(-1.0, -1.0, 6.0)
    P = Point3D(6.0, 5.0, 9.0)
    Q = Point3D()

    print("Using shared library to solve the problem...")
    print("Points:")
    print(f"A = ({A.x}, {A.y}, {A.z})")
    print(f"B = ({B.x}, {B.y}, {B.z})")
    print(f"C = ({C.x}, {C.y}, {C.z})")
    print(f"P = ({P.x}, {P.y}, {P.z})")

    try:
        # Call the C function
        distance = lib.solve_point_to_plane_distance(A, B, C, P, ctypes.byref(Q))
        print(f"\nCalculated distance: {distance:.6f} units")
        print(f"Foot of perpendicular Q: ({Q.x:.6f}, {Q.y:.6f}, {Q.z:.6f})")

        # Read points from file and create visualization
        points_dict = read_points_from_file('points.dat')
        print(f"\nPoints read from file: {points_dict}")

        create_visualization(points_dict)

    except Exception as e:
        print(f"Error: {e}")
        print("Make sure to compile the shared library first with: make plane.so")

if __name__ == "__main__":
    main()
