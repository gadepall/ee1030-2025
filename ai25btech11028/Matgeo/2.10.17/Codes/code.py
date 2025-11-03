import numpy as np
import matplotlib.pyplot as plt

# === Vector analysis functions ===
def magnitude(v):
    return np.sqrt(v.T @ v)   # sqrt(v^T v)

def is_parallel(v, u, tol=1e-9):
    """Check if v is parallel to u. Return scalar t if v = t u, else None."""
    if np.allclose(u, 0):   # u is zero vector
        return None
    ratios = []
    for vi, ui in zip(v, u):
        if abs(ui) > tol:
            ratios.append(vi / ui)
        elif abs(vi) > tol:
            return None  # ui = 0 but vi =! 0 --> not parallel
    if len(ratios) == 0:
        return None
    t = ratios[0]
    if all(abs(r - t) < tol for r in ratios):
        return t
    return None

def dot_product(v, w):
    return v.T @ w   # v^T w

# === Example usage ===
v = np.array([2/3, -2/3, 1/3])
u = np.array([-1, 1, -0.5])
w = np.array([3, 2, -2])

# Analysis
mag_v = magnitude(v)
t = is_parallel(v, u)
dot_vw = dot_product(v, w)
 print("||v|| =", mag_v)
if t is None:
    print("v is NOT parallel to u")
else:
    print(f"v is parallel to u, scalar t = {t}")
print("v^T w =", dot_vw)

# === Plotting ===
fig = plt.figure(figsize=(6,6))
ax = fig.add_subplot(111, projection="3d")

origin = np.array([0,0,0])

# Draw vectors
ax.quiver(*origin, *v, color="r", linewidth=2, label="v")
ax.quiver(*origin, *u, color="g", linewidth=2, label="u")
ax.quiver(*origin, *w, color="b", linewidth=2, label="w")
    # Axes
ax.plot([0,1.5],[0,0],[0,0], color="k")
ax.plot([0,0],[0,1.5],[0,0], color="k")
ax.plot([0,0],[0,0],[0,1.5], color="k")
ax.text(1.6,0,0,"X",color="k")
ax.text(0,1.6,0,"Y",color="k")
ax.text(0,0,1.6,"Z",color="k")
ax.set_xlim([-1.5,1.5])
ax.set_ylim([-1.5,1.5])
ax.set_zlim([-1.5,1.5])
ax.set_xlabel("X-axis")
ax.set_ylabel("Y-axis")
ax.set_zlabel("Z-axis")
ax.legend()

     # Save before show
plt.savefig("/storage/emulated/0/matrix/Matgeo/2.10.17/figs/Figure_1.png", dpi=300, bbox_inches='tight')
plt.show()   
