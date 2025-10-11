import os
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# (same computation as before)
p1 = np.array([2., 3., 2.])
p2 = np.array([-2., 3., 0.])
v  = np.array([2., -3., 6.])
dist = np.linalg.norm(np.cross(p2 - p1, v)) / np.linalg.norm(v)
print(f"Shortest distance = {dist:.4f}")

w = p2 - p1
proj_len = np.dot(w, v) / np.dot(v, v)
closest_on_l1 = p1 + proj_len * v
closest_on_l2 = p2 + proj_len * v

# Plot lines
fig = plt.figure()
ax = fig.add_subplot(111, projection="3d")
u_vals = np.linspace(-2, 2, 50)
l1_points = p1[:, None] + v[:, None]*u_vals
l2_points = p2[:, None] + v[:, None]*u_vals
ax.plot(l1_points[0], l1_points[1], l1_points[2], "b", label="Line 1")
ax.plot(l2_points[0], l2_points[1], l2_points[2], "g", label="Line 2")
ax.plot([closest_on_l1[0], closest_on_l2[0]],
        [closest_on_l1[1], closest_on_l2[1]],
        [closest_on_l1[2], closest_on_l2[2]],
        "r", linewidth=2, label="Shortest distance")
ax.view_init(elev=20, azim=45)
ax.legend()

# ---- Save image one directory up, inside a folder named 'figures' ----
save_dir = os.path.join("..", "figures")
os.makedirs(save_dir, exist_ok=True)   # create folder if it doesn't exist
save_path = os.path.join(save_dir, "shortest_distance.png")
plt.savefig(save_path, dpi=300, bbox_inches="tight")

print("Image saved to:", os.path.abspath(save_path))

