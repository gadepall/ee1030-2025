import numpy as np
import matplotlib.pyplot as plt
import matplotlib as mp 
mp.use("TkAgg")

# --- Given data ---
a, b, c = np.sqrt(3), 1.0, -6.0           # line PQ: sqrt(3)x + y - 6 = 0
D = np.array([3*np.sqrt(3)/2.0, 3.0/2.0])  # tangency point D
r = 1.0

def unit(v):
    n = np.linalg.norm(v)
    return v / n if n != 0 else v

def line_from_normal_and_point(nvec, P):
    # a x + b y + c = 0 with normal nvec = [a,b]; c = -(a*Px + b*Py)
    a,b = nvec[0], nvec[1]
    c = -(a*P[0] + b*P[1])
    return np.array([a,b,c])

def intersect(L1, L2):
    A = np.array([[L1[0], L1[1]], [L2[0], L2[1]]])
    B = -np.array([L1[2], L2[2]])
    return np.linalg.solve(A, B)

def rotate(v, theta):
    c,s = np.cos(theta), np.sin(theta)
    R = np.array([[c,-s],[s,c]])
    return R @ v

n = np.array([a,b])
n_unit = unit(n)

# two candidate centers:
C1 = D + r * n_unit
C2 = D - r * n_unit

# Choose centre on same side of PQ as origin
def side_sign(point):
    return np.sign(a*point[0] + b*point[1] + c)

origin_side = side_sign(np.array([0.0,0.0]))
if side_sign(C1) == origin_side:
    O = C1
else:
    O = C2

h,k = O[0], O[1]


vD = D - O  # vector from centre to D
theta = 2*np.pi/3.0  # 120 degrees
vE = rotate(vD,  theta)
vF = rotate(vD, -theta)

E = O + vE
F = O + vF

assert np.allclose(np.linalg.norm(vD), r, atol=1e-8)
assert np.allclose(np.linalg.norm(vE), r, atol=1e-8)
assert np.allclose(np.linalg.norm(vF), r, atol=1e-8)

L_PQ_from_tangent = line_from_normal_and_point(vD, D)
# normalize to same scale as input for nicer printing (divide by sqrt(a^2+b^2))
scale_given = np.sqrt(a*a + b*b)
L_PQ_normed = L_PQ_from_tangent / scale_given

L_QR = line_from_normal_and_point(vE, E)
L_RP = line_from_normal_and_point(vF, F)

# --- Intersections → vertices P, Q, R -------------------------------------
# side names: PQ (tangent at D), QR (tangent at E), RP (tangent at F)
P = intersect(L_PQ_from_tangent, L_RP)   # P = PQ ∩ RP
Q = intersect(L_PQ_from_tangent, L_QR)   # Q = PQ ∩ QR
R = intersect(L_QR, L_RP)                # R = QR ∩ RP

u_vec = np.array([h,k])
f_const = h*h + k*k - r*r

print("\nExpanded scalar form:")
print(f"x^2 + y^2 - 2*{h:.2g}*x - 2*{k:.2g}*y + {f_const:.2g} = 0")

# Print the three tangent lines in normalized readable form
def pretty_line(L):
    # scale to unit normal for readability
    nrm = np.linalg.norm(L[:2])
    La = L / nrm
    a_s,b_s,c_s = La[0], La[1], La[2]
    return f"{a_s:.12g} x + {b_s:.12g} y + {c_s:.12g} = 0"



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

# tangency lines (extended for visibility)
xlim_min = min(P[0],Q[0],R[0], O[0]) - 3
xlim_max = max(P[0],Q[0],R[0], O[0]) + 3
xvals = np.linspace(xlim_min, xlim_max, 400)
# PQ from given coeffs
yvals_pq = -(a*xvals + c)/b
plt.plot(xvals, yvals_pq, 'g-', label="Given side PQ")

# ---- function to plot any line ----
def plot_line(L, style, label):
    aL,bL,cL = L
    if abs(bL) > 1e-8:
        y = -(aL*xvals + cL)/bL
        plt.plot(xvals, y, style, label=label)
    else:
        xconst = -cL/aL
        plt.axvline(x=xconst, linestyle=style, label=label)

# tangent lines via their normals
plot_line(L_QR, 'k--', 'QR (tangent E)')
plot_line(L_RP, 'c--', 'RP (tangent F)')

# points
plt.scatter([D[0], E[0], F[0]], [D[1], E[1], F[1]], 
            c=['red','orange','purple'], zorder=5, label='Tangency points D,E,F')
plt.scatter(O[0], O[1], c='black', s=40, label='Center O')
plt.scatter([P[0],Q[0],R[0]],[P[1],Q[1],R[1]], c='blue', s=30, label='Vertices P,Q,R')
plt.scatter(0,0, c='green', s=40, label="Origin (0,0)")

# --- Add labels near points ---
def add_label(pt, text, dx=0.1, dy=0.1):
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

plt.xlim(xlim_min, xlim_max)
plt.ylim(min(P[1],Q[1],R[1], O[1]) - 3, max(P[1],Q[1],R[1], O[1]) + 3)
plt.gca().set_aspect("equal", adjustable="box")
plt.grid(True, linestyle='--', alpha=0.6)
plt.legend()
plt.title("Equilateral triangle PQR with incircle C and tangency points D,E,F")
plt.savefig("/home/user/Matrix Theory: workspace/Matgeo_assignments/7.4.33/figs/Figure_1.png")
plt.show()

