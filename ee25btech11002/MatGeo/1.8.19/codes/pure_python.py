import numpy as np
import matplotlib.pyplot as plt
from numpy import linalg as LA

# --- Defines the points from the problem ---
# Center of the circle
Q = np.array([0, 1]).reshape(-1, 1)

# A point on the circumference of the circle
P = np.array([5, -3]).reshape(-1, 1)

# --- Calculations for plotting ---

# The radius 'r' is the distance between Q and P.
# This is required to generate the circle plot.
r = LA.norm(P - Q)

# The two possible points for R are the intersections of the circle and the line y=6.
# x^2 + (6-1)^2 = r^2  => x^2 + 25 = 41 => x^2 = 16 => x = +/- 4
R1 = np.array([4, 6]).reshape(-1, 1)
R2 = np.array([-4, 6]).reshape(-1, 1)

# --- Helper function to generate circle points ---
def circ_gen(O, r):
    """
    Generates points for a circle with center O and radius r.
    """
    len = 50
    theta = np.linspace(0, 2*np.pi, len)
    x_circ = np.zeros((2, len))
    x_circ[0, :] = r * np.cos(theta)
    x_circ[1, :] = r * np.sin(theta)
    x_circ = (x_circ.T + O.T).T
    return x_circ

# --- Generate shapes for plotting ---

# Generate the circle with center Q passing through P
x_circ = circ_gen(Q, r)

# Generate the line y = 6
x_line = np.linspace(-8, 8, 100)
y_line = np.full_like(x_line, 6)


# --- Plotting ---

# Plot the circle and the line
plt.plot(x_circ[0, :], x_circ[1, :], label='Circle centered at Q')
plt.plot(x_line, y_line, label='Line y = 6')


# Plot and label the points
points = np.hstack((P, Q, R1, R2))
plt.scatter(points[0, :], points[1, :], s=50, color='red') # s for size
point_labels = ['P(5, -3)', 'Q(0, 1)', r'$R_1$(4, 6)', r'$R_2$(-4, 6)']

for label, (x, y) in zip(point_labels, points.T):
    plt.annotate(
        label,
        (x, y),
        textcoords="offset points",
        xytext=(0, 10), # Position text above the point
        ha='center'
    )

# --- Plot formatting ---
plt.xlabel("x-axis")
plt.ylabel("y-axis")
plt.title("Visual Representation of Question 1.8.19")
plt.legend(loc='bottom,right')
plt.grid(True)
plt.axis('equal') # Ensures the circle is not distorted
plt.show()