import numpy as np
import matplotlib.pyplot as plt

# Vertices of the triangle
A = np.array([2, -6])
B = np.array([5, 2])
C = np.array([-2, 2])

def foot_of_perpendicular(P, Q, R):
    """
    Calculate foot of perpendicular from point P to line QR.
    
    Returns the point (x,y) on line QR closest to P.
    """
    # Vector from Q to R
    QR = R - Q
    # Vector from Q to P
    QP = P - Q
    # Projection scalar of QP onto QR
    t = np.dot(QP, QR) / np.dot(QR, QR)
    # Foot point
    foot = Q + t * QR
    return foot

def plot_altitude(vertex, foot, label):
    """
    Plot altitude segment from vertex to foot point.
    """
    plt.plot([vertex[0], foot[0]], [vertex[1], foot[1]], linestyle='--', label=label)

# Calculate feet of perpendiculars (altitudinal feet)
footA = foot_of_perpendicular(A, B, C)  # from A to BC
footB = foot_of_perpendicular(B, A, C)  # from B to AC
footC = foot_of_perpendicular(C, A, B)  # from C to AB

# Plot triangle
triangle_x = [A[0], B[0], C[0], A[0]]
triangle_y = [A[1], B[1], C[1], A[1]]
plt.plot(triangle_x, triangle_y, 'bo-', label='Triangle')

# Plot altitudes
plot_altitude(A, footA, 'Altitude from A')
plot_altitude(B, footB, 'Altitude from B')
plot_altitude(C, footC, 'Altitude from C')

# Compute orthocenter as intersection of two altitudes
# Use line parameter form: for line segment vertex-foot
def line_params(P, Q):
    # Line vector:
    v = Q - P
    # Line coefficients: a*x + b*y = c form
    a = v[1]
    b = -v[0]
    c = a*P[0] + b*P[1]
    return a, b, c

a1, b1, c1 = line_params(A, footA)
a2, b2, c2 = line_params(B, footB)
A_mat = np.array([[a1, b1], [a2, b2]])
b_vec = np.array([c1, c2])

O = np.linalg.solve(A_mat, b_vec)

# Plot orthocenter
plt.plot(O[0], O[1], 'ro', label='Orthocenter')

plt.axis('equal')
plt.title('Triangle and Orthocenter with Altitudes')
plt.legend()
plt.savefig("fig1.png")
plt.grid(True)
plt.show()

