
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

def read_data_file():
    """Read the results from main.dat file"""
    data = {}
    with open('main.dat', 'r') as f:
        lines = f.readlines()

    for line in lines:
        if line.startswith('k1:'):
            data['k1'] = float(line.split(':')[1].strip())
        elif line.startswith('k2:'):
            data['k2'] = float(line.split(':')[1].strip())
        elif line.startswith('x1:'):
            coords = line.split(':')[1].strip().split()
            data['x1'] = [float(x) for x in coords]
        elif line.startswith('x2:'):
            coords = line.split(':')[1].strip().split()
            data['x2'] = [float(x) for x in coords]
        elif line.startswith('distance:'):
            data['distance'] = float(line.split(':')[1].strip())

    return data

def solve_skew_lines_distance():
    """Solve the skew lines distance problem and visualize only the two lines"""

    # Read data from main.dat
    data = read_data_file()

    # Original line parameters from the PDF
    A = np.array([2, -5, 1])
    B = np.array([7, 0, -6])
    dir1 = np.array([3, 2, 6])
    dir2 = np.array([1, 2, 2])

    # Verify the solution
    k1 = data['k1']
    k2 = data['k2']

    x1 = A + k1 * dir1
    x2 = B + k2 * dir2

    distance = np.linalg.norm(x2 - x1)
    exact_distance = 17 * np.sqrt(5) / 5

    print(f"From C program: k1 = {k1:.6f}, k2 = {k2:.6f}")
    print(f"Distance = {distance:.6f}")
    print(f"Exact distance = 17√5/5 = {exact_distance:.6f}")

    # Create 3D visualization with only the two lines
    fig = plt.figure(figsize=(10, 8))
    ax = fig.add_subplot(111, projection='3d')

    # Generate points along both lines for visualization
    t1 = np.linspace(-4, 4, 200)
    t2 = np.linspace(-4, 4, 200)

    line1_points = np.array([A + t * dir1 for t in t1])
    line2_points = np.array([B + t * dir2 for t in t2])

    # Plot only the two lines
    ax.plot(line1_points[:, 0], line1_points[:, 1], line1_points[:, 2], 
            'b-', linewidth=3, label='Line 1')
    ax.plot(line2_points[:, 0], line2_points[:, 1], line2_points[:, 2], 
            'r-', linewidth=3, label='Line 2')

    # Set labels and title
    ax.set_xlabel('X', fontsize=12)
    ax.set_ylabel('Y', fontsize=12)
    ax.set_zlabel('Z', fontsize=12)
    ax.set_title('Two Skew Lines', fontsize=14, pad=20)

    # Remove legend and grid for cleaner look
    ax.grid(False)

    # Set viewing angle for better visualization
    ax.view_init(elev=20, azim=45)

    # Set equal aspect ratio
    all_points = np.vstack([line1_points, line2_points])
    max_range = np.array([all_points[:,0].max()-all_points[:,0].min(), 
                         all_points[:,1].max()-all_points[:,1].min(),
                         all_points[:,2].max()-all_points[:,2].min()]).max() / 2.0

    mid_x = (all_points[:,0].max()+all_points[:,0].min()) * 0.5
    mid_y = (all_points[:,1].max()+all_points[:,1].min()) * 0.5
    mid_z = (all_points[:,2].max()+all_points[:,2].min()) * 0.5

    ax.set_xlim(mid_x - max_range, mid_x + max_range)
    ax.set_ylim(mid_y - max_range, mid_y + max_range)
    ax.set_zlim(mid_z - max_range, mid_z + max_range)

    # Remove axes for cleaner appearance (optional)
    # ax.set_axis_off()

    plt.tight_layout()
    plt.savefig('fig1.png', dpi=300, bbox_inches='tight')
    plt.show()

    return distance, exact_distance

if __name__ == "__main__":
    distance, exact_distance = solve_skew_lines_distance()
