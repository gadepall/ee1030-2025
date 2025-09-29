import numpy as np
import matplotlib.pyplot as plt

p1, d1 = np.array([1, 2, 3]), np.array([2, 3, 4])
p2, d2 = np.array([4, 1, 0]), np.array([5, 2, 1])

A = np.array([d1[:2], -d2[:2]]).T
b = p2[:2] - p1[:2]

try:
    lambda_val, mu_val = np.linalg.solve(A, b)
    intersection_point = p1 + lambda_val * d1
    print(f"The lines intersect at the point: {intersection_point}")

    # Line equations for legend
    eq1 = f"L1: (x,y,z) = ({p1[0]},{p1[1]},{p1[2]}) + t({d1[0]},{d1[1]},{d1[2]})"
    eq2 = f"L2: (x,y,z) = ({p2[0]},{p2[1]},{p2[2]}) + t({d2[0]},{d2[1]},{d2[2]})"

    fig = plt.figure(figsize=(10, 8))
    ax = fig.add_subplot(111, projection='3d')

    t = np.linspace(-2, 2, 50)
    line1_points = p1 + t[:, np.newaxis] * d1
    line2_points = p2 + t[:, np.newaxis] * d2

    # Use equations in legend
    ax.plot(line1_points[:, 0], line1_points[:, 1], line1_points[:, 2], label=eq1)
    ax.plot(line2_points[:, 0], line2_points[:, 1], line2_points[:, 2], label=eq2)

    # Mark and label the intersection point
    ax.scatter(intersection_point[0], intersection_point[1], intersection_point[2],
               color='red', s=100, zorder=5, label=f'Intersection {intersection_point}')
    ax.text(intersection_point[0], intersection_point[1], intersection_point[2],
            f'{intersection_point}', color='red', fontsize=10)

    ax.set_xlabel('X axis')
    ax.set_ylabel('Y axis')
    ax.set_zlabel('Z axis')
    ax.set_title('Intersection of Two Lines in 3D')
    ax.legend()
    plt.savefig('/Users/bhargavkrish/Desktop/BackupMatrix/ee25btech11013/matgeo/4.10.15/figs/Figure_1.png')
    plt.show()

except np.linalg.LinAlgError:
    print("The lines are parallel or skew; they do not intersect.")
