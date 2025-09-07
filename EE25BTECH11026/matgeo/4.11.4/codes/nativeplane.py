import sympy as sp
import numpy as np
import matplotlib.pyplot as plt
import matplotlib as mp
mp.use("TkAgg")

# ------------------------
# Step 1: Define symbols
# ------------------------
lam = sp.symbols('lam')

# Given plane normals and constants
n1, d1 = sp.Matrix([1,2,3]), -4
n2, d2 = sp.Matrix([2,1,-1]), 5
n3, d3 = sp.Matrix([5,3,-6]), 8

# ------------------------
# Step 2: General plane through intersection
# ------------------------
n = n1 + lam*n2       # normal vector depends on λ
d = d1 + lam*d2       # constant term

# ------------------------
# Step 3: Perpendicular condition
# ------------------------
eq = sp.Eq(n.dot(n3), 0)
lam_val = sp.solve(eq, lam)[0]

# Substitute λ into plane equation
n_req = (n.subs(lam, lam_val))
d_req = d.subs(lam, lam_val)

# ------------------------
# Step 4: Scale to integers (fix applied here)
# ------------------------
all_vals = list(n_req) + [d_req]   # avoid .tolist()
mult = sp.lcm([sp.denom(val) for val in all_vals])
n_req = (n_req * mult).applyfunc(sp.simplify)
d_req = sp.simplify(d_req * mult)

# ------------------------
# Step 5: Vector form
# ------------------------
# Plane: n · (r - a) = 0  → r · n = a · n
# Find a point 'a' on plane (set y=0, z=0 solve for x)
x, y, z = sp.symbols('x y z')
plane_eq = n_req[0]*x + n_req[1]*y + n_req[2]*z + d_req
point_on_plane = sp.solve(plane_eq.subs({y:0, z:0}), x)

if point_on_plane:
    a = sp.Matrix([point_on_plane[0], 0, 0])  # take this as point
else:
    # fallback: try y instead
    point_on_plane = sp.solve(plane_eq.subs({x:0, z:0}), y)
    a = sp.Matrix([0, point_on_plane[0], 0])

vector_form = f"r · ({n_req[0]}, {n_req[1]}, {n_req[2]}) = {a.dot(n_req)}"
print("\nEquation of required plane:")
print(vector_form)

# ------------------------
# Step 6: Plot planes
# ------------------------
fig = plt.figure(figsize=(8,8))
ax = fig.add_subplot(111, projection='3d')

def plot_plane(ax, n, d, color, alpha=0.4):
    xx, yy = np.meshgrid(np.linspace(-5,5,15), np.linspace(-5,5,15))
    zz = (-n[0]*xx - n[1]*yy - d) / n[2]
    ax.plot_surface(xx, yy, zz, color=color, alpha=alpha)

# Convert sympy → float numpy
n1f, d1f = np.array(n1, dtype=float), float(d1)
n2f, d2f = np.array(n2, dtype=float), float(d2)
n3f, d3f = np.array(n3, dtype=float), float(d3)
nrf, drf = np.array([float(v) for v in n_req]), float(d_req)

# Plot given planes and required plane
plot_plane(ax, n1f, d1f, "red", 0.2)     # π1
plot_plane(ax, n2f, d2f, "blue", 0.2)    # π2
plot_plane(ax, n3f, d3f, "green", 0.2)   # π3
plot_plane(ax, nrf, drf, "purple", 0.6)  # Required plane

ax.set_xlabel("X")
ax.set_ylabel("Y")
ax.set_zlabel("Z")
ax.set_title(r"Required Plane through Intersection, $\perp$ to Given Plane")
plt.savefig("/home/user/Matrix/Matgeo_assignments/4.11.4/figs/Figure_1")
plt.show()

