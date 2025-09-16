import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D  # registers 3D projection

# ---------- Problem data (change if you want to test other examples) ----------
P = (2.0, 2.0, 1.0)    # (Px, Py, Pz)
Q = (5.0, 1.0, -2.0)   # (Qx, Qy, Qz)
Rx_given = 4.0         # known x-coordinate of R (we pivot on x here)

# ---------- helper: row operation in Python ----------
def apply_row_op_py(r1, r2):
    """
    Perform R2 <- R2 - mult * R1 where mult = r2[0] / r1[0].
    r1, r2 are length-3 iterables of numbers.
    Returns (mult, new_r2) where new_r2 is a list of 3 floats.
    If r1[0] == 0, raises ValueError.
    """
    a11 = float(r1[0])
    if abs(a11) < 1e-15:
        raise ValueError("Pivot (r1[0]) is zero; cannot eliminate.")
    mult = float(r2[0]) / a11
    new_r2 = [r2[j] - mult * r1[j] for j in range(3)]
    return mult, new_r2

# ---------- compute direction and check pivot ----------
Px, Py, Pz = P
Qx, Qy, Qz = Q
Dx, Dy, Dz = Qx - Px, Qy - Py, Qz - Pz

if abs(Dx) < 1e-12:
    raise SystemExit("Pivot Dx is zero; this script is pivoting on x. Choose different input or pivot axis.")

# ---------- build M^T rows (numeric with symbolic part in r2 before solving) ----------
# r1 = [Dx, Dy, Dz]
# r2 (before knowing y,z) = [Rx_given - Px, (y-Py), (z-Pz)]
# we will compute t = (Rx_given - Px)/Dx via multiplier
r1 = [Dx, Dy, Dz]
r2_first = Rx_given - Px  # numeric pivot entry

# ---------- get multiplier t (same as parameter) ----------
t = r2_first / Dx   # Exactly same as compute_multiplier
print("Multiplier t = (Rx - Px)/Dx =", t)

# ---------- compute y and z from parametric form X = P + t*D ----------
y = Py + t * Dy
z = Pz + t * Dz
R = (Rx_given, y, z)
print("Computed R = (x, y, z) =", (R[0], R[1], R[2]))

# ---------- now form numeric second row and apply row op in Python to verify ----------
r2 = [r2_first, y - Py, z - Pz]   # numeric second row now
mult_used, new_r2 = apply_row_op_py(r1, r2)

print("\nRow operation details:")
print(" r1 =", r1)
print(" r2 (before) =", r2)
print(" multiplier used =", mult_used)
print(" r2 (after)  =", new_r2)

# check near-zero
tol = 1e-9
if all(abs(v) < tol for v in new_r2):
    print("Verification: second row reduced to zero (rank = 1) within tolerance.")
else:
    print("Warning: second row not exactly zero; values:", new_r2)

# ---------- Plotting (3D) with labels and coordinates ----------
def fmt_coords(pt):
    return f"({pt[0]:.2f}, {pt[1]:.2f}, {pt[2]:.2f})"

N = 101
ts = np.linspace(0.0, 1.0, N)
points = np.array([[Px + t*Dx, Py + t*Dy, Pz + t*Dz] for t in ts])

fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

# plot the line
ax.plot(points[:,0], points[:,1], points[:,2], label='Line PQ')

# plot points
ax.scatter(*P, color='red', s=60)
ax.text(P[0], P[1], P[2], f"  P {fmt_coords(P)}", color='red', fontsize=10, weight='bold')

ax.scatter(*Q, color='blue', s=60)
ax.text(Q[0], Q[1], Q[2], f"  Q {fmt_coords(Q)}", color='blue', fontsize=10, weight='bold')

ax.scatter(*R, color='green', s=60)
ax.text(R[0], R[1], R[2], f"  R {fmt_coords(R)}", color='green', fontsize=10, weight='bold')

# optional: draw dashed line from R down to x-y plane to help read z (uncomment if you like)
# ax.plot([R[0], R[0]], [R[1], R[1]], [0, R[2]], linestyle='--', linewidth=1)

ax.set_xlabel('x')
ax.set_ylabel('y')
ax.set_zlabel('z')
ax.set_title('Line through P and Q with computed R')
ax.legend()

# save and show
imgfile = "line_3d_python_only.png"
plt.savefig(imgfile, bbox_inches='tight')
print(f"Saved 3D image: {imgfile}")

plt.show()

