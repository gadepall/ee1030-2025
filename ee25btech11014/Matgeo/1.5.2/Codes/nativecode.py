import numpy as np
import matplotlib.pyplot as plt

# --- Define points ---
A = np.array([6.0, -4.0])
B = np.array([-2.0, -7.0])

# --- Function to generate a line segment between two points ---
def generate_line_segment(point1, point2, num_points=50):
    line_segment = np.zeros((2, num_points))
    lambda_vals = np.linspace(0, 1, num_points)
    for i in range(num_points):
        temp = point1 + lambda_vals[i] * (point2 - point1)
        line_segment[:, i] = temp.T
    return line_segment

# --- Generate line AB ---
x_AB = generate_line_segment(A, B)

# --- Plot line AB ---
plt.plot(x_AB[0, :], x_AB[1, :], label='$AB$')

# --- Plot points A and B ---
all_points = np.vstack((A, B)).T
plt.scatter(all_points[0, :], all_points[1, :], color='red')

# --- Add labels ---
point_labels = [f'A {tuple(A)}', f'B {tuple(B)}']
offsets = [(10, 5), (-30, -10)]
for i, txt in enumerate(point_labels):
    plt.annotate(txt,
                 (all_points[0, i], all_points[1, i]),
                 textcoords="offset points",
                 xytext=offsets[i],
                 ha='center')

# --- Plot settings ---
plt.xlabel('$x$')
plt.ylabel('$y$')
plt.title('Line segment AB')
plt.legend(loc='best')
plt.grid(True)
plt.axis('equal')

# --- Save and show plot ---
plt.savefig('graph.png')
plt.show()
