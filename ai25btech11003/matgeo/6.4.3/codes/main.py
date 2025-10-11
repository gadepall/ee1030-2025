
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
            data['x1'] = np.array([float(x) for x in coords])
        elif line.startswith('x2:'):
            coords = line.split(':')[1].strip().split()
            data['x2'] = np.array([float(x) for x in coords])
        elif line.startswith('distance:'):
            data['distance'] = float(line.split(':')[1].strip())
    return data

def plot_skew_lines_with_normal():
    data = read_data_file()

    # Line parameters (from PDF)
    A = np.array([2, -5, 1])
    B = np.array([7, 0, -6])
    d1 = np.array([3, 2, 6])
    d2 = np.array([1, 2, 2])

    # Closest points X1 and X2 from C output
    x1 = data['x1'] if 'x1' in data else A + data['k1'] * d1
    x2 = data['x2'] if 'x2' in data else B + data['k2'] * d2

    # Long line segments centered away from closest approach to keep them visually separated
    t = np.linspace(-3.5, 3.5, 240)
    shift1 = 1.5
    shift2 = -1.5
    seg1 = np.array([x1 + (shift1 + ti) * d1 for ti in t])
    seg2 = np.array([x2 + (shift2 + ti) * d2 for ti in t])

    fig = plt.figure(figsize=(10, 8), facecolor='white')
    ax = fig.add_subplot(111, projection='3d')
    ax.set_facecolor('white')

    # Plot lines
    ax.plot(seg1[:,0], seg1[:,1], seg1[:,2], color='orange', linewidth=4, label='L1')
    ax.plot(seg2[:,0], seg2[:,1], seg2[:,2], color='green', linewidth=4, label='L2')

    # Plot X1 and X2 markers on respective lines
    ax.scatter(x1[0], x1[1], x1[2], color='orange', s=60, edgecolor='k', zorder=5)
    ax.text(x1[0], x1[1], x1[2], '  X1', color='black')
    ax.scatter(x2[0], x2[1], x2[2], color='green', s=60, edgecolor='k', zorder=5)
    ax.text(x2[0], x2[1], x2[2], '  X2', color='black')

    # Dotted normal segment between X1 and X2
    ax.plot([x1[0], x2[0]], [x1[1], x2[1]], [x1[2], x2[2]],
            linestyle=':', color='gray', linewidth=2, label='Normal')

    # Axes styling
    ax.grid(True, alpha=0.3)
    ax.set_xlabel('X', fontsize=12)
    ax.set_ylabel('Y', fontsize=12)
    ax.set_zlabel('Z', fontsize=12)
    ax.view_init(elev=15, azim=-60)

    # Limits
    all_pts = np.vstack([seg1, seg2, np.vstack([x1, x2])])
    xr = all_pts[:,0].ptp(); yr = all_pts[:,1].ptp(); zr = all_pts[:,2].ptp()
    mr = max(xr, yr, zr) * 0.6
    mx, my, mz = all_pts[:,0].mean(), all_pts[:,1].mean(), all_pts[:,2].mean()
    ax.set_xlim(mx - mr, mx + mr)
    ax.set_ylim(my - mr, my + mr)
    ax.set_zlim(mz - mr, mz + mr)

    # Legend without clutter
    ax.legend(loc='upper right', frameon=True, fancybox=True, shadow=True)

    plt.tight_layout()
    plt.savefig('fig1.png', dpi=300, bbox_inches='tight', facecolor='white')
    plt.show()

if __name__ == '__main__':
    plot_skew_lines_with_normal()
