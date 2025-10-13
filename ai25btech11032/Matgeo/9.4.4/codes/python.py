import numpy as np
import matplotlib.pyplot as plt

# ---------- Helpers ----------

def quadratic_to_conic(a, b, c):
    V = np.array([[a, 0.0],
                  [0.0, 0.0]], dtype=float)
    u = np.array([b/2.0, 0.0], dtype=float)   # so that 2 u^T x = b x
    f = float(c)
    return V, u, f

def line_conic_intersection(V, u, f, h, m, eps=1e-12):
    # m^T V m
    Vm = V @ m
    mTVm = float(m @ Vm)

    # Vh + u
    Vh_u = V @ h + u

    # m^T (Vh + u)
    mT_Vh_u = float(m @ Vh_u)

    # g(h) = h^T V h + 2 u^T h + f
    g = float(h @ (V @ h) + 2.0 * (u @ h) + f)

    disc = mT_Vh_u**2 - g * mTVm

    if disc > eps:
        r = np.sqrt(disc)
        k1 = (-mT_Vh_u + r) / mTVm
        k2 = (-mT_Vh_u - r) / mTVm
        X1 = h + k1 * m
        X2 = h + k2 * m
        return 2, np.array([k1, k2], dtype=float), np.vstack([X1, X2])
    elif abs(disc) <= eps:
        k = (-mT_Vh_u) / mTVm
        X = h + k * m
        return 1, np.array([k, k], dtype=float), np.vstack([X, X])
    else:
        return 0, np.array([np.nan, np.nan]), np.array([[np.nan, np.nan],
                                                        [np.nan, np.nan]])

# ---------- Problem setup ----------

# Given quadratic: x^2 - 3x - 10 = 0
a, b, c = 1.0, -3.0, -10.0

# Conic parameters (V, u, f)
V, u, f = quadratic_to_conic(a, b, c)

# x-axis as the line: y = 0  -> h = (0,0), m = (1,0)
h = np.array([0.0, 0.0], dtype=float)
m = np.array([1.0, 0.0], dtype=float)

# ---------- Solve via line–conic intersection ----------
status, kappa, X = line_conic_intersection(V, u, f, h, m)

# Roots are the x-coordinates of intersection points with y=0
roots = []
if status >= 1:
    roots = sorted([float(X[0, 0]), float(X[1, 0])]) if status == 2 else [float(X[0, 0])]

print("Status (2:two real, 1:tangent, 0:none):", status)
print("kappa values:", kappa)
print("Intersection points (x,y):\n", X)
print("Roots (x-intercepts):", roots)

# ---------- Plot ----------
xs = np.linspace(-10, 10, 600)
ys = a*xs**2 + b*xs + c

plt.figure()
plt.plot(xs, ys, label=rf"$y={a:.0f}x^2{b:+.0f}x{c:+.0f}$")
plt.axhline(0, linestyle="--", linewidth=1, label="x-axis")

if status >= 1:
    plt.scatter([X[0,0]], [0.0], s=60, zorder=3, label=f"root {X[0,0]:g}")
    if status == 2:
        plt.scatter([X[1,0]], [0.0], s=60, zorder=3, label=f"root {X[1,0]:g}")

plt.xlabel("x"); plt.ylabel("y")
plt.title("Roots via line–conic intersection (vectors & matrices)")
plt.grid(True)
plt.legend()
plt.savefig("newparabola.png")
plt.show()
 


