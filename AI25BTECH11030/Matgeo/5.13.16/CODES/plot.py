import numpy as np
import matplotlib.pyplot as plt

# Vertices
A = np.array([2, -6])
B = np.array([5, 2])
C = np.array([-2, 2])

# Helper functions
def altitude_through_point(P, Q, R):
    """
    Returns coefficients a,b,c of the altitude through P
    which is perpendicular to QR, i.e. a*x + b*y = c
    """
    # Direction vector of QR
    d = Q - R
    # Normal vector for the altitude (perpendicular)
    n = np.array([-d[1], d[0]])
    c = n[0]*P[0] + n[1]*P[1]
    return n[0], n[1], c

def intersect_lines(a1, b1, c1, a2, b2, c2):
    """
    Finds the intersection point of two lines: a1*x+b1*y=c1 and a2*x+b2*y=c2
    """
    A = np.array([[a1, b1], [a2, b2]])
    b = np.array([c1, c2])
    return np.linalg.solve(A, b)

# Find two altitudes
a1, b1, c1 = altitude_through_point(A, B, C) # through A, perp to BC
a2, b2, c2 = altitude_through_point(B, A, C) # through B, perp to AC

# Orthocentre is intersection of two altitudes
O = intersect_lines(a1, b1, c1, a2, b2, c2)

# Print orthocentre
print("Orthocentre:", O)

# Plotting
plt.figure(figsize=(6,6))
plt.plot([A[0], B[0], C[0], A[0]], [A[1], B[1], C[1], A[1]], 'bo-', label='Triangle')

# Plot altitudes
def plot_altitude(P, n, c, label):
    # Generate points along the altitude for plot
    t = np.linspace(-10, 10, 100)
    if n[1] != 0:
        x = t
        y = (c - n[0]*x)/n[1]
    else:
        x = np.ones_like(t)*(c/n[0])
        y = t
    plt.plot(x, y, '--', label=label)

plot_altitude(A, np.array([a1, b1]), c1, 'Altitude from A')
plot_altitude(B, np.array([a2, b2]), c2, 'Altitude from B')

plt.plot(O[0], O[1], 'ro', label='Orthocentre')
plt.legend()
plt.grid(True)
plt.title('Triangle and Orthocentre')
plt.savefig("fig1.png")
plt.show()

