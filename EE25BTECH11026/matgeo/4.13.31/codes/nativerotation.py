import numpy as np
import matplotlib.pyplot as plt
import matplotlib as mp
mp.use("TkAgg")

def line_intercepts_after_rotation(a, b, theta):
    m = np.array([1/a, 1/b])
    P = np.array([
        [np.cos(theta), -np.sin(theta)],
        [np.sin(theta),  np.cos(theta)]
    ])
    m_new = m @ P
    return 1/m_new[0], 1/m_new[1]   # p, q

# Parameters
a, b = 3, 4
theta = np.pi/3

# New intercepts
p, q = line_intercepts_after_rotation(a, b, theta)

# ========== BOOLEAN CHECK SECTION ==========
eps = 1e-8

optA = abs((a**2 + b**2) - (p**2 + q**2)) < eps
optB = abs((1/a**2 + 1/b**2) - (1/p**2 + 1/q**2)) < eps
optC = abs((a**2 + p**2) - (b**2 + q**2)) < eps
optD = abs((1/a**2 + 1/p**2) - (1/b**2 + 1/q**2)) < eps

print(f"Option A : {optA}")
print(f"Option B : {optB}")
print(f"Option C : {optC}")
print(f"Option D : {optD}")

# ========== PLOT ONLY IF TRUE ==========
if optB:   # Only plot when option B is satisfied
    # Original line
    x_vals = np.linspace(-1, max(a, 6), 400)
    y_vals = b*(1 - x_vals/a)

    # Original intercepts
    A = (a,0)
    B = (0,b)

    # Rotated axes directions
    e1_new = np.array([np.cos(theta), np.sin(theta)])
    e2_new = np.array([-np.sin(theta), np.cos(theta)])

    # Transform new intercepts (in rotated coords) back to old coords
    P = np.array([[np.cos(theta), -np.sin(theta)],
                  [np.sin(theta),  np.cos(theta)]])
    Pp = P @ np.array([p,0])   # (p,0) in rotated coords
    Pq = P @ np.array([0,q])   # (0,q) in rotated coords

    # Plot
    plt.figure(figsize=(7,7))
    plt.axhline(0, color='gray', lw=1)
    plt.axvline(0, color='gray', lw=1)

    # Original line
    plt.plot(x_vals, y_vals, 'b', label="Original line")

    # Original intercepts
    plt.scatter(*A, color='blue')
    plt.scatter(*B, color='blue')
    plt.text(A[0], A[1]-0.3, f"A({a},0)", ha='center')
    plt.text(B[0]-0.3, B[1], f"B(0,{b})", va='center')

    # Draw rotated axes as extended lines
    t = np.linspace(-6, 6, 200)
    plt.plot(t*e1_new[0], t*e1_new[1], 'r--', label="Rotated X'-axis")
    plt.plot(t*e2_new[0], t*e2_new[1], 'r--', label="Rotated Y'-axis")

    # New intercepts on rotated axes
    plt.scatter(*Pp, color='green')
    plt.scatter(*Pq, color='green')
    plt.text(Pp[0], Pp[1]-0.2, f"P({p:.2f},0)", color='green', ha='center')
    plt.text(Pq[0]-0.2, Pq[1], f"Q(0,{q:.2f})", color='green', va='center')

    plt.axis("equal")
    plt.legend()
    plt.title("Graph for the True Relation: 1/a² + 1/b² = 1/p² + 1/q²")
    plt.savefig("/home/user/Matrix/Matgeo_assignments/4.13.31/figs/Figure_1")
    plt.show()

