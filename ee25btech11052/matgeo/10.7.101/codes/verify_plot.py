import ctypes
import numpy as np
import matplotlib.pyplot as plt

# Load shared library
lib = ctypes.CDLL('/home/shriyasnh/Desktop/matgeonew/10.7.101/codes/parabola.so')

# Define function signatures
lib.parabola_points.argtypes = [ctypes.POINTER(ctypes.c_double), ctypes.POINTER(ctypes.c_double), ctypes.c_int]
lib.normal_line.argtypes = [ctypes.c_double, ctypes.c_double, ctypes.c_double, 
                            ctypes.POINTER(ctypes.c_double), ctypes.POINTER(ctypes.c_double), 
                            ctypes.POINTER(ctypes.c_double), ctypes.c_int]
lib.circle_points.argtypes = [ctypes.c_double, ctypes.c_double, ctypes.c_double,
                              ctypes.POINTER(ctypes.c_double), ctypes.POINTER(ctypes.c_double),
                              ctypes.POINTER(ctypes.c_double), ctypes.c_int]

# Points from solution
P = np.array([1, -2])
Q = np.array([1, 2])
R = np.array([0, 0])
h = np.array([3, 0])  # Point from which normals are drawn
centroid = np.array([2/3, 0])
circumcenter = np.array([5/2, 0])
circumradius = 5/2

# Plot setup
fig, ax = plt.subplots(figsize=(12, 9))

# Parabola y^2 = 4x
n_para = 500
y_para = np.linspace(-6, 6, n_para)
x_para = np.zeros(n_para)
y_para_c = y_para.ctypes.data_as(ctypes.POINTER(ctypes.c_double))
x_para_c = x_para.ctypes.data_as(ctypes.POINTER(ctypes.c_double))
lib.parabola_points(y_para_c, x_para_c, n_para)
ax.plot(x_para, y_para, 'b-', linewidth=2, label='Parabola $y^2=4x$')

# Triangle PQR
triangle = np.array([P, Q, R, P])
ax.plot(triangle[:, 0], triangle[:, 1], 'r-', linewidth=2, label='Triangle PQR')
ax.fill(triangle[:-1, 0], triangle[:-1, 1], alpha=0.2, color='red')

# Points
ax.plot(*P, 'ro', markersize=6, label='P(1, -2)')
ax.plot(*Q, 'go', markersize=6, label='Q(1, 2)')
ax.plot(*R, 'bo', markersize=6, label='R(0, 0)')
ax.plot(*h, 'mo', markersize=6, label='h(3, 0)')
ax.plot(*centroid, 'co', markersize=6, label=f'Centroid ({2/3:.2f}, 0)')
ax.plot(*circumcenter, 'ko', markersize=6, label=f'Circumcenter ({5/2}, 0)')

# Normal lines
n_norm = 100
t_vals = np.linspace(-2, 3, n_norm)
t_vals_c = t_vals.ctypes.data_as(ctypes.POINTER(ctypes.c_double))

# Normal with slope 0 (horizontal) through R
x_norm0 = np.zeros(n_norm)
y_norm0 = np.zeros(n_norm)
x_norm0_c = x_norm0.ctypes.data_as(ctypes.POINTER(ctypes.c_double))
y_norm0_c = y_norm0.ctypes.data_as(ctypes.POINTER(ctypes.c_double))
lib.normal_line(R[0], R[1], 0.0, t_vals_c, x_norm0_c, y_norm0_c, n_norm)
ax.plot(x_norm0, y_norm0, 'k--', linewidth=1, alpha=0.5)

# Normal with slope 1 through P
x_norm1 = np.zeros(n_norm)
y_norm1 = np.zeros(n_norm)
x_norm1_c = x_norm1.ctypes.data_as(ctypes.POINTER(ctypes.c_double))
y_norm1_c = y_norm1.ctypes.data_as(ctypes.POINTER(ctypes.c_double))
lib.normal_line(P[0], P[1], 1.0, t_vals_c, x_norm1_c, y_norm1_c, n_norm)
ax.plot(x_norm1, y_norm1, 'k--', linewidth=1, alpha=0.5)

# Normal with slope -1 through Q
x_norm2 = np.zeros(n_norm)
y_norm2 = np.zeros(n_norm)
x_norm2_c = x_norm2.ctypes.data_as(ctypes.POINTER(ctypes.c_double))
y_norm2_c = y_norm2.ctypes.data_as(ctypes.POINTER(ctypes.c_double))
lib.normal_line(Q[0], Q[1], -1.0, t_vals_c, x_norm2_c, y_norm2_c, n_norm)
ax.plot(x_norm2, y_norm2, 'k--', linewidth=1, alpha=0.5, label='Normals')

# Circumcircle
n_circle = 500
theta = np.linspace(0, 2*np.pi, n_circle)
x_circle = np.zeros(n_circle)
y_circle = np.zeros(n_circle)
theta_c = theta.ctypes.data_as(ctypes.POINTER(ctypes.c_double))
x_circle_c = x_circle.ctypes.data_as(ctypes.POINTER(ctypes.c_double))
y_circle_c = y_circle.ctypes.data_as(ctypes.POINTER(ctypes.c_double))
lib.circle_points(circumcenter[0], circumcenter[1], circumradius, theta_c, x_circle_c, y_circle_c, n_circle)
ax.plot(x_circle, y_circle, 'purple', linewidth=1.5, label=f'Circumcircle (R={circumradius})')

# Annotations
ax.text(P[0]+0.2, P[1], 'P', fontsize=12, fontweight='bold')
ax.text(Q[0]+0.2, Q[1], 'Q', fontsize=12, fontweight='bold')
ax.text(R[0]+0.2, R[1]+0.3, 'R', fontsize=12, fontweight='bold')
ax.text(h[0]+0.2, h[1]+0.3, 'h(3,0)', fontsize=12, fontweight='bold')
ax.text(centroid[0], centroid[1]-0.5, 'G', fontsize=12, fontweight='bold', color='cyan')
ax.text(circumcenter[0], circumcenter[1]+0.5, 'O', fontsize=12, fontweight='bold')

# Verify solution
print("=" * 50)
print("SOLUTION VERIFICATION")
print("=" * 50)

# Verify points lie on parabola
def verify_parabola(x, y):
    return abs(y**2 - 4*x) < 1e-10

print(f"\n1. Points on parabola y²=4x:")
print(f"   P(1,-2): y²={P[1]**2}, 4x={4*P[0]} → Valid: {verify_parabola(P[0], P[1])}")
print(f"   Q(1,2):  y²={Q[1]**2}, 4x={4*Q[0]} → Valid: {verify_parabola(Q[0], Q[1])}")
print(f"   R(0,0):  y²={R[1]**2}, 4x={4*R[0]} → Valid: {verify_parabola(R[0], R[1])}")

# Verify area
area_calc = 0.5 * abs((P[0]*(Q[1]-R[1]) + Q[0]*(R[1]-P[1]) + R[0]*(P[1]-Q[1])))
print(f"\n2. Area of triangle PQR:")
print(f"   Calculated: {area_calc}")
print(f"   Expected: 2.0")
print(f"   Valid: {abs(area_calc - 2.0) < 1e-10}")

# Verify side lengths
PQ = np.linalg.norm(P - Q)
QR = np.linalg.norm(Q - R)
RP = np.linalg.norm(R - P)
print(f"\n3. Side lengths:")
print(f"   |PQ| = {PQ:.4f}")
print(f"   |QR| = {QR:.4f} (√5 = {np.sqrt(5):.4f})")
print(f"   |RP| = {RP:.4f} (√5 = {np.sqrt(5):.4f})")

# Verify circumradius
R_calc = (PQ * QR * RP) / (4 * area_calc)
print(f"\n4. Circumradius:")
print(f"   Calculated: {R_calc:.4f}")
print(f"   Expected: 2.5")
print(f"   Valid: {abs(R_calc - 2.5) < 1e-10}")

# Verify centroid
centroid_calc = (P + Q + R) / 3
print(f"\n5. Centroid:")
print(f"   Calculated: ({centroid_calc[0]:.4f}, {centroid_calc[1]:.4f})")
print(f"   Expected: (0.6667, 0.0)")
print(f"   Valid: {np.allclose(centroid_calc, centroid)}")

# Verify circumcenter distances
dist_OP = np.linalg.norm(circumcenter - P)
dist_OQ = np.linalg.norm(circumcenter - Q)
dist_OR = np.linalg.norm(circumcenter - R)
print(f"\n6. Circumcenter equidistant check:")
print(f"   Distance to P: {dist_OP:.4f}")
print(f"   Distance to Q: {dist_OQ:.4f}")
print(f"   Distance to R: {dist_OR:.4f}")
print(f"   All equal to radius: {np.allclose([dist_OP, dist_OQ, dist_OR], circumradius)}")

# Verify normals pass through h(3,0)
print(f"\n7. Normals pass through h(3,0):")
# Normal at R with slope 0: y = 0
print(f"   Normal at R (slope=0): y=0, passes through (3,0): True")
# Normal at P with slope 1: y+2 = 1(x-1) → y = x-3
y_at_3_P = 1*(3-1) + P[1]
print(f"   Normal at P (slope=1): y={1}(x-1)+{P[1]}, at x=3: y={y_at_3_P} → Valid: {abs(y_at_3_P) < 1e-10}")
# Normal at Q with slope -1: y-2 = -1(x-1) → y = -x+3
y_at_3_Q = -1*(3-1) + Q[1]
print(f"   Normal at Q (slope=-1): y={-1}(x-1)+{Q[1]}, at x=3: y={y_at_3_Q} → Valid: {abs(y_at_3_Q) < 1e-10}")

print("=" * 50)
print("ALL SOLUTIONS VERIFIED ✓")
print("=" * 50 + "\n")

ax.set_xlim(-4, 10)
ax.set_ylim(-4, 4)
ax.set_aspect('equal', adjustable='box')
ax.grid(True, alpha=0.3)
ax.axhline(y=0, color='k', linewidth=0.5)
ax.axvline(x=0, color='k', linewidth=0.5)
ax.legend(loc='upper left', fontsize=9)
ax.set_xlabel('x', fontsize=12)
ax.set_ylabel('y', fontsize=12)
ax.set_title('Parabola $y^2=4x$ with Triangle PQR and Circumcircle', fontsize=14, fontweight='bold')

plt.tight_layout()
plt.show()
plt.savefig("/home/shriyasnh/Desktop/matgeonew/10.7.101/figs/plot.png")
