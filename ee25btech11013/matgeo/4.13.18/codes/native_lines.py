import numpy as np
import matplotlib.pyplot as plt

def distance_between_lines(c1, c2, nx, ny):
    return abs(c1 - c2) / np.hypot(nx, ny)

def projection_on_line(px, py, nx, ny, c):
    denom = nx*nx + ny*ny
    t = (c - (nx*px + ny*py)) / denom
    qx = px + nx*t
    qy = py + ny*t
    return qx, qy

px, py = 13.0, 32.0   # point on L
a = 5.0               # L: x/5 + y/b = 1


b = py / (1 - px / a)
print("Computed b:", b)   # expected -20.0


nL = np.array([1.0/a, 1.0/b])

scale = 20.0
nx, ny = (nL * scale).tolist()   # gives (4.0, -1.0)
c1 = 1.0 * scale                 # because original L: nL·x = 1 -> scaled: (scale*nL)·x = scale

c2 = -3.0


dist = distance_between_lines(c1, c2, nx, ny)
qx, qy = projection_on_line(px, py, nx, ny, c2)

print("Distance between L and K:", dist)
print("Foot Q on K:", (qx, qy))


# ---------- plotting ----------
x_vals = np.linspace(-20, 20, 400)
# CORRECT formula: y = (c - nx*x) / ny
y_L = (c1 - nx * x_vals) / ny
y_K = (c2 - nx * x_vals) / ny

plt.figure(figsize=(8, 8))
plt.plot(x_vals, y_L, label=f"L: {int(nx)}x + ({int(ny)})y = {int(c1)}")
plt.plot(x_vals, y_K, "--", label=f"K: {int(nx)}x + ({int(ny)})y = {int(c2)}")
plt.scatter(px, py, color="red", zorder=5, label=f"P=({int(px)},{int(py)}) on L")
plt.scatter(qx, qy, color="green", zorder=5, label=f"Q=({qx:.3f},{qy:.3f}) on K")
plt.plot([px, qx], [py, qy], "k--", linewidth=1.5, label=f"Perpendicular (dist={dist:.6f})")

plt.xlabel("x"); plt.ylabel("y")
plt.title("Parallel Lines L and K with Perpendicular")
plt.axis("equal")
plt.grid(True); plt.legend()
plt.savefig('/Users/bhargavkrish/Desktop/BackupMatrix/ee25btech11013/matgeo/4.13.18/figs/Figure_1.png')
plt.show()
