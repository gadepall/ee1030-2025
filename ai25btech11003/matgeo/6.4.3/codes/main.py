
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

def read_data_file():
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
    data = read_data_file()

    # Line parameters
    A = np.array([2, -5, 1])
    B = np.array([7, 0, -6])
    dir1 = np.array([3, 2, 6])
    dir2 = np.array([1, 2, 2])

    # Use the closest points as reference
    k1 = data['k1']
    k2 = data['k2']
    x1 = A + k1 * dir1
    x2 = B + k2 * dir2

    # Create longer line segments that are clearly separated
    # Extend lines in both directions from shifted centers
    t_range = np.linspace(-3, 3, 200)  # Much longer segments

    # Shift the centers to avoid visual overlap
    shift1 = 1.5
    shift2 = -1.5

    # Generate line segments
    seg1 = np.array([x1 + (shift1 + t) * dir1 for t in t_range])
    seg2 = np.array([x2 + (shift2 + t) * dir2 for t in t_range])

    # Create figure with white background like the reference image
    fig = plt.figure(figsize=(10, 8), facecolor='white')
    ax = fig.add_subplot(111, projection='3d')
    ax.set_facecolor('white')

    # Plot the two lines with orange and green colors, thick lines
    ax.plot(seg1[:, 0], seg1[:, 1], seg1[:, 2], 
            color='orange', linewidth=4, label='L1', solid_capstyle='round')
    ax.plot(seg2[:, 0], seg2[:, 1], seg2[:, 2], 
            color='green', linewidth=4, label='L2', solid_capstyle='round')

    # Set up the grid and axes similar to reference image
    ax.grid(True, alpha=0.3)
    ax.set_xlabel('X', fontsize=12)
    ax.set_ylabel('Y', fontsize=12)
    ax.set_zlabel('Z', fontsize=12)

    # Remove title to match reference image
    # ax.set_title('Two Skew Lines', fontsize=14)

    # Set viewing angle similar to reference image
    ax.view_init(elev=15, azim=-60)

    # Set axis limits to show the lines clearly separated
    all_points = np.vstack([seg1, seg2])

    # Extend the range slightly for better visualization
    x_range = all_points[:,0].max() - all_points[:,0].min()
    y_range = all_points[:,1].max() - all_points[:,1].min()
    z_range = all_points[:,2].max() - all_points[:,2].min()

    max_range = max(x_range, y_range, z_range) * 0.6

    mid_x = (all_points[:,0].max() + all_points[:,0].min()) * 0.5
    mid_y = (all_points[:,1].max() + all_points[:,1].min()) * 0.5
    mid_z = (all_points[:,2].max() + all_points[:,2].min()) * 0.5

    ax.set_xlim(mid_x - max_range, mid_x + max_range)
    ax.set_ylim(mid_y - max_range, mid_y + max_range)
    ax.set_zlim(mid_z - max_range, mid_z + max_range)

    # Add legend similar to reference image (but without Normal)
    ax.legend(loc='upper right', frameon=True, fancybox=True, shadow=True)

    # Make the plot look clean
    plt.tight_layout()
    plt.savefig('fig1.png', dpi=300, bbox_inches='tight', facecolor='white')
    plt.show()

    # Print calculation results
    distance = np.linalg.norm(x2 - x1)
    exact_distance = 17 * np.sqrt(5) / 5
    print(f"Calculated distance: {distance:.6f}")
    print(f"Exact distance: {exact_distance:.6f}")

    return distance, exact_distance

if __name__ == '__main__':
    solve_skew_lines_distance()
