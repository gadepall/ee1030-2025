import numpy as np
import matplotlib.pyplot as plt

# Points
A = np.array([3.0, 6.0])
B = np.array([-12.0, -3.0])
X = np.array([-7.0, 0.0])  # Intersection with X-axis

# Calculate ratio AX : XB
AX = np.linalg.norm(A - X)
XB = np.linalg.norm(B - X)
ratio = AX / XB
print(f"The X-axis divides AB in the ratio {int(AX)}:{int(XB)} (i.e., {ratio:.2f}:1)")

# Equation of line AB
slope = (B[1] - A[1]) / (B[0] - A[0])
intercept = A[1] - slope * A[0]

x_min = min(A[0], B[0], X[0]) - 2
x_max = max(A[0], B[0], X[0]) + 2
x_line = np.linspace(x_min, x_max, 100)
y_line = slope * x_line + intercept

# Plot line AB
plt.plot(x_line, y_line, label='Line AB', color='black', linestyle='--')

# Plot points
all_points = np.vstack((A, B, X)).T
plt.scatter(all_points[0, :], all_points[1, :], color=['red', 'blue', 'green'], zorder=5)

# Labels
point_labels = [f'A({A[0]},{A[1]})', f'B({B[0]},{B[1]})', f'X({X[0]},{X[1]})']
for i, txt in enumerate(point_labels):
    plt.annotate(txt,
                 (all_points[0, i], all_points[1, i]),
                 textcoords="offset points",
                 xytext=(10, 5),
                 ha='center')

# Axes and formatting
plt.axhline(0, color='gray', linewidth=1)
plt.axvline(0, color='gray', linewidth=1)
plt.xlabel('$x$')
plt.ylabel('$y$')
plt.title('Division of Line Segment AB by X-axis')
plt.legend(loc='best')
plt.grid(True)
plt.axis('equal')

# Save figure
plt.savefig('division_AB.png', dpi=300)

# Show plot
plt.show()
