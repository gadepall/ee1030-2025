import numpy as np
import matplotlib.pyplot as plt

def line_intersect(n1, c1, n2, c2):
    """
    Find intersection point of two lines:
    n1.T * x = c1
    n2.T * x = c2
    Inputs:
        n1, n2: (2,) or (2,1) normal vectors to lines
        c1, c2: scalars
    Returns:
        p: (2,1) intersection point
    """
    N = np.column_stack((n1.flatten(), n2.flatten()))  # 2x2 matrix
    C = np.array([c1, c2])
    p = np.linalg.solve(N, C)
    return p.reshape(2,1)

def line_dir_pt(direction, point, k1, k2, num=100):
    """
    Generate points on a line given direction and a point.
    direction: (2,) array
    point: (2,) array
    k1, k2: scalar parameters along the line
    num: number of points
    Returns: 2 x num array of points
    """
    k = np.linspace(k1, k2, num)
    line_pts = point.reshape(2,1) + direction.reshape(2,1) * k
    return line_pts

# Slopes
m = 1
n = -1

# Normals (for line: y = m x + c  => -m x + y = c)
n1 = np.array([-m, 1])
n2 = np.array([-m, 1])
n3 = np.array([-n, 1])
n4 = np.array([-n, 1])

# Constants c
c1 = 0
c2 = 1
c3 = 0
c4 = 1

# Find intersection points
P1 = line_intersect(n1, c1, n3, c3)
P2 = line_intersect(n1, c1, n4, c4)
P3 = line_intersect(n2, c2, n4, c4)
P4 = line_intersect(n2, c2, n3, c3)

# Parallelogram points array
parallelogram = np.hstack((P1, P2, P3, P4, P1))

# Calculate area via cross product
vec1 = P2 - P1
vec2 = P4 - P1
area = abs(np.cross(vec1.flatten(), vec2.flatten()))

# Direction vectors for lines (x direction)
dir_m = np.array([1, m])
dir_n = np.array([1, n])

# Generate line points for plotting
k1, k2 = -5, 5

line_m0 = line_dir_pt(dir_m, np.array([0,0]), k1, k2)
line_m1 = line_dir_pt(dir_m, np.array([0,1]), k1, k2)
line_n0 = line_dir_pt(dir_n, np.array([0,0]), k1, k2)
line_n1 = line_dir_pt(dir_n, np.array([0,1]), k1, k2)

# Plotting
plt.figure(figsize=(8,8))
plt.plot(line_m0[0], line_m0[1], label='y = m x', color='blue')
plt.plot(line_m1[0], line_m1[1], label='y = m x + 1', linestyle='--', color='blue')
plt.plot(line_n0[0], line_n0[1], label='y = n x', color='red')
plt.plot(line_n1[0], line_n1[1], label='y = n x + 1', linestyle='--', color='red')

plt.plot(parallelogram[0], parallelogram[1], 'k-', linewidth=2, label='Parallelogram')
plt.fill(parallelogram[0], parallelogram[1], 'grey', alpha=0.3)

for i, P in enumerate([P1, P2, P3, P4], 1):
    plt.plot(P[0], P[1], 'ko')
    plt.text(P[0] + 0.1, P[1] + 0.1, f'P{i}', fontsize=12)

plt.text(-4.5, 4, f'Area = {area:.3f}', fontsize=14, color='green',
         bbox=dict(facecolor='white', alpha=0.8))

plt.axhline(0, color='black', lw=0.5)
plt.axvline(0, color='black', lw=0.5)
plt.grid(True, linestyle='--', alpha=0.6)
plt.axis('equal')
plt.xlim(-5, 5)
plt.ylim(-5, 5)
plt.xlabel('x-axis')
plt.ylabel('y-axis')
plt.title('Parallelogram formed by lines y=mx, y=mx+1, y=nx, y=nx+1')
plt.legend()
plt.show()


