import ctypes
import numpy as np
import matplotlib.pyplot as plt

# load shared library
lib = ctypes.CDLL("./libcircle_solver.so")

# prepare result array (14 doubles: O,D,E,F,P,Q,R)
results = (ctypes.c_double * 14)()
lib.solve_geometry(results)

# unpack into numpy
vals = np.array(results)
O = vals[0:2]
D = vals[2:4]
E = vals[4:6]
F = vals[6:8]
P = vals[8:10]
Q = vals[10:12]
R = vals[12:14]

# circle parameters
h, k, r = O[0], O[1], 1.0
print("Equation of circle:")
print(f"(x-{h:.2f})^2+(y-{k:.2f})^2={r}")

# --- Plot ------------------------------------------------------------------
theta_vals = np.linspace(0, 2*np.pi, 600)
xc = O[0] + r * np.cos(theta_vals)
yc = O[1] + r * np.sin(theta_vals)

plt.figure(figsize=(7,7))
# incircle
plt.plot(xc, yc, label="Incircle (r=1)")

# triangle edges
tri_x = [P[0], Q[0], R[0], P[0]]
tri_y = [P[1], Q[1], R[1], P[1]]
plt.plot(tri_x, tri_y, 'm--', linewidth=1.8, label="Equilateral Triangle")

# --- Reconstruct lines PQ, QR, RP (same as native python version) ---
# PQ given: sqrt(3)x + y - 6 = 0
a, b, c = np.sqrt(3), 1.0, -6.0
xvals = np.linspace(min(P[0],Q[0],R[0],O[0]) - 3,
                    max(P[0],Q[0],R[0],O[0]) + 3, 400)
yvals_pq = -(a*xvals + c)/b
plt.plot(xvals, yvals_pq, 'g-', label="Given side PQ")

# lines QR, RP from tangency points
def line_from_points(A, B):
    # equation through points A,B : (y2-y1)x - (x2-x1)y + (x2-x1)y1 - (y2-y1)x1 = 0
    x1,y1 = A; x2,y2 = B
    a = y1 - y2
    b = x2 - x1
    c = x1*y2 - x2*y1
    return np.array([a,b,c])

def plot_line(L, style, label):
    aL,bL,cL = L
    if abs(bL) > 1e-8:
        y = -(aL*xvals + cL)/bL
        plt.plot(xvals, y, style, label=label)
    else:
        plt.axvline(-cL/aL, linestyle=style, label=label)

L_QR = line_from_points(Q,R)
L_RP = line_from_points(R,P)

plot_line(L_QR, 'k--', 'QR (tangent E)')
plot_line(L_RP, 'c--', 'RP (tangent F)')

# points
plt.scatter([D[0],E[0],F[0]], [D[1],E[1],F[1]], 
            c=['red','orange','purple'], zorder=5, label='Tangency points D,E,F')
plt.scatter(O[0], O[1], c='black', s=40, label='Center O')
plt.scatter([P[0],Q[0],R[0]],[P[1],Q[1],R[1]], c='blue', s=30, label='Vertices P,Q,R')
plt.scatter(0,0, c='green', s=40, label="Origin (0,0)")

# --- Labels ---
def add_label(pt, text, dx=0.15, dy=0.15):
    plt.text(pt[0]+dx, pt[1]+dy, text, fontsize=11, fontweight='bold',
             bbox=dict(facecolor='white', edgecolor='none', alpha=0.7))

add_label(P, "P")
add_label(Q, "Q")
add_label(R, "R")
add_label(D, "D")
add_label(E, "E")
add_label(F, "F")
add_label(O, "O", dx=0.2, dy=-0.2)
add_label([0,0], "Origin", dx=0.2, dy=-0.2)

# axes
plt.axhline(0, color='gray', linewidth=1)  # x-axis
plt.axvline(0, color='gray', linewidth=1)  # y-axis

plt.xlim(min(P[0],Q[0],R[0], O[0]) - 3, max(P[0],Q[0],R[0], O[0]) + 3)
plt.ylim(min(P[1],Q[1],R[1], O[1]) - 3, max(P[1],Q[1],R[1], O[1]) + 3)
plt.gca().set_aspect("equal", adjustable="box")
plt.grid(True, linestyle='--', alpha=0.6)
plt.legend()
plt.title("Equilateral triangle PQR with incircle C and tangency points D,E,F")
plt.savefig("/home/user/Matrix Theory: workspace/Matgeo_assignments/7.4.33/figs/figure_1.png")
plt.show()

