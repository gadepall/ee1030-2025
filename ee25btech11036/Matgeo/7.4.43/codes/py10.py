import numpy as np
import matplotlib.pyplot as plt
from numpy import linalg as LA
from conics.funcs import circ_gen
from line.funcs import line_gen
from matplotlib.patches import Arc

# === Step 1: Circle with diameter AC ===
A = np.array([0.0,0.0]).reshape(-1,1)
C = np.array([4.0,0.0]).reshape(-1,1)
O = (A + C)/2
R = LA.norm(C - O)

# === Step 2: Choose B on circle (not collinear with AC) ===
theta = np.deg2rad(60)
B = O + R * np.array([[np.cos(theta)], [np.sin(theta)]])

# === Step 3: Angle alpha at A ===
alpha = np.deg2rad(30)  # angle DAB
slope_AD = np.tan(alpha)

# === Step 4: Compute intersection D on BC segment ===
dx = C[0,0] - B[0,0]
dy = C[1,0] - B[1,0]
t = (slope_AD*(A[0,0]-B[0,0]) + (B[1,0]-A[1,0])) / (dy - slope_AD*dx)
t = np.clip(t, 0.15, 0.85)  # ensure D inside BC
D = (B + t*(C-B)).reshape(-1,1)

# === Step 5: Midpoint M of DC ===
M = (D + C)/2

# === Step 6: Compute distance d = AM ===
d = LA.norm(A - M)

# === Step 7: Generate circle and lines using your functions ===
x_circ = circ_gen(O,R)
x_AB = line_gen(A,B)
x_AC = line_gen(A,C)
x_BC = line_gen(B,C)
x_AD = line_gen(A,D)
x_DM = line_gen(D,M)

# === Step 8: Plot setup ===
plt.figure(figsize=(8,8))
plt.plot(x_circ[0,:], x_circ[1,:], 'b', lw=2, label='Circle')
plt.plot(x_AB[0,:], x_AB[1,:], 'g', label='AB')
plt.plot(x_AC[0,:], x_AC[1,:], 'k', label='AC (diameter)')
plt.plot(x_BC[0,:], x_BC[1,:], 'c', lw=2, label='BC (chord)')
plt.plot(x_AD[0,:], x_AD[1,:], 'r', lw=2, label='AD')
plt.plot(x_DM[0,:], x_DM[1,:], 'm--', lw=2, label='DC midpoint line')

# === Step 9: Plot points ===
points = {'A':A,'B':B,'C':C,'D':D,'M':M,'O':O}
for name,p in points.items():
    plt.scatter(p[0,0], p[1,0], s=70, zorder=5)
    offset = 0.15
    if name in ['D','B','M']:
        offset = 0.25
    plt.text(p[0,0]+offset, p[1,0]+offset, name, fontsize=12, fontweight='bold')

# === Step 10: Draw angles alpha (DAB) and beta (CAB) clearly ===
def plot_angle(center, p1, p2, radius, color, label):
    v1, v2 = p1-center, p2-center
    ang1 = np.degrees(np.arctan2(v1[1,0], v1[0,0]))
    ang2 = np.degrees(np.arctan2(v2[1,0], v2[0,0]))
    if ang2 < ang1: ang1, ang2 = ang2, ang1
    arc = Arc((center[0,0], center[1,0]), 2*radius, 2*radius,
              angle=0, theta1=ang1, theta2=ang2, color=color, lw=3)
    plt.gca().add_patch(arc)
    mid = np.radians((ang1+ang2)/2)
    plt.text(center[0,0]+1.4*radius*np.cos(mid),
             center[1,0]+1.4*radius*np.sin(mid),
             label, fontsize=16, color=color, fontweight='bold')

plot_angle(A,D,B,0.5,'r',r'$\alpha$')  # DAB
plot_angle(A,C,B,0.8,'b',r'$\beta$')   # CAB

# === Step 11: Annotate distance d = AM ===
plt.plot([A[0,0], M[0,0]], [A[1,0], M[1,0]], 'k--', lw=1.5)
mid_label = (A + M)/2
plt.text(mid_label[0,0], mid_label[1,0]+0.15, f'd={d:.2f}', fontsize=12, fontweight='bold', color='k')

# === Step 12: Finalize plot ===
plt.axis('equal')
plt.grid(True)
plt.legend(fontsize=12)
plt.title('Circle with AC as diameter, D on BC, midpoint M, angles α and β, distance d', fontsize=14)
plt.show()

