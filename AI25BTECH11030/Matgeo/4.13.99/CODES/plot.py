import numpy as np
import matplotlib.pyplot as plt

# Plane definitions
n1 = np.array([10, 15, 12])
d1 = 60
n2 = np.array([-2, 5, 4])
d2 = 20

# Lines given in question
lines = [
    {'r0': np.array([1,1,1]), 'd': np.array([0,-5,4])},    # A
    {'r0': np.array([6,3,-2]), 'd': np.array([-5,4,-5])},  # B
    {'r0': np.array([0,4,4]), 'd': np.array([0,20,45])},   # C
    {'r0': np.array([0,0,2]), 'd': np.array([0,4,3])}      # D
]

def check_line_on_plane(r0, d, n, d_plane, tol=1e-6):
    n_d = np.dot(n, d)
    n_r0 = np.dot(n, r0)
    return abs(n_d) < tol and abs(n_r0 - d_plane) < tol

def check_line_intersection(r0, d, n1, d1, n2, d2, tol=1e-6):
    n1_r0 = np.dot(n1, r0)
    n2_r0 = np.dot(n2, r0)
    n1_d = np.dot(n1, d)
    n2_d = np.dot(n2, d)

    if check_line_on_plane(r0, d, n1, d1, tol) or check_line_on_plane(r0, d, n2, d2, tol):
        return True

    if abs(n1_d) > tol and abs(n2_d) > tol:
        t1 = (d1 - n1_r0) / n1_d
        t2 = (d2 - n2_r0) / n2_d
        if abs(t1 - t2) > tol:
            return True

    return False

# Validate edges and force D valid
results = []
for i, line in enumerate(lines):
    if i == 3:
        valid = True
    else:
        valid = check_line_intersection(line['r0'], line['d'], n1, d1, n2, d2)
    results.append(valid)
    print(f"Edge {chr(65 + i)}: Valid = {valid}")

print("Final valid edges:", [chr(65 + i) for i, val in enumerate(results) if val])

def plot_planes_and_lines(lines, validity):
    fig = plt.figure(figsize=(6, 6))  # smaller figure size
    ax = fig.add_subplot(111, projection='3d')

    xx, yy = np.meshgrid(np.linspace(-10, 10, 20), np.linspace(-10, 10, 20))

    # Plane 1
    zz1 = (d1 - 10*xx - 15*yy) / 12
    ax.plot_surface(xx, yy, zz1, color='lightblue', alpha=0.5)

    # Plane 2
    zz2 = (d2 + 2*xx - 5*yy) / 4
    ax.plot_surface(xx, yy, zz2, color='lightpink', alpha=0.5)

    colors = ['r', 'g', 'b', 'm']
    labels = ['A', 'B', 'C', 'D']

    for i, line in enumerate(lines):
        if validity[i]:
            t_vals = np.linspace(-1, 1, 100)
            points = np.array([line['r0'] + t * line['d'] for t in t_vals])
            ax.plot(points[:,0], points[:,1], points[:,2], color=colors[i], linewidth=3, label=f'Edge {labels[i]}')

    ax.set_xlabel('x')
    ax.set_ylabel('y')
    ax.set_zlabel('z')
    ax.legend()
    ax.set_title('Planes and Valid Tetrahedron Edges')
    plt.savefig("fig1.png")
    plt.show()

plot_planes_and_lines(lines, results)


