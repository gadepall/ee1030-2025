import ctypes
import numpy as np
import matplotlib.pyplot as plt
import math
import os

# ---- load the shared library (must be in same folder) ----
lib_path = "./umbrella.so"
if not os.path.exists(lib_path):
    raise FileNotFoundError(f"{lib_path} not found. Compile umbrella.c to umbrella.so first.")

lib = ctypes.CDLL(lib_path)
lib.umbrella_angle.argtypes = [ctypes.c_double * 2, ctypes.c_double * 2]
lib.umbrella_angle.restype = ctypes.c_double

# ---- input vectors (same as your problem) ----
vrw_np = np.array([0.0, -35.0])   # rain relative to wind (x east, y up)
vw_np  = np.array([-12.0, 0.0])   # wind (east->west is -12)

# prepare ctypes arrays and call C function
vrw_ct = (ctypes.c_double * 2)(*vrw_np)
vw_ct  = (ctypes.c_double * 2)(*vw_np)

theta = lib.umbrella_angle(vrw_ct, vw_ct)   # radians returned from C
theta_deg = math.degrees(theta)

print(f"Angle from vertical (radians): {theta:.6f}")
print(f"Angle from vertical (degrees): {theta_deg:.3f}")

# ---- prepare plotting data ----
v_r = vrw_np + vw_np                 # resultant rain velocity (ground frame)
umbrella_dir = -v_r                  # umbrella points opposite to rain motion
# scale umbrella arrow so it's visible on the plot (preserve direction)
if np.linalg.norm(umbrella_dir) > 0:
    umbrella_vis = umbrella_dir / np.linalg.norm(umbrella_dir) * 20.0
else:
    umbrella_vis = np.array([0.0, 0.0])

# ---- plotting ----
fig, ax = plt.subplots(figsize=(7,7))

ax.quiver(0, 0, vrw_np[0], vrw_np[1], angles='xy', scale_units='xy', scale=1,
          color='tab:blue', width=0.006, label=r'$\vec v_{r/w}=(0,-35)$')
ax.quiver(0, 0, vw_np[0], vw_np[1], angles='xy', scale_units='xy', scale=1,
          color='tab:green', width=0.006, label=r'$\vec v_w=(-12,0)$')
ax.quiver(0, 0, v_r[0], v_r[1], angles='xy', scale_units='xy', scale=1,
          color='tab:red', width=0.006, label=r'$\vec v_r$ (resultant)')

# umbrella direction (longer, visible)
ax.quiver(0, 0, umbrella_vis[0], umbrella_vis[1], angles='xy', scale_units='xy', scale=1,
          color='tab:purple', width=0.01, label='Hold umbrella (into rain)')

# dashed vertical reference (downward)
ax.plot([0, 0], [0, -45], linestyle=':', color='gray', linewidth=1)

# annotate angle value near origin
ax.text(0.5, -8, f"θ = {theta_deg:.1f}° from vertical", fontsize=12,
        bbox=dict(facecolor='white', alpha=0.8, edgecolor='gray'))

# axis limits and labels
ax.set_xlim(-40, 10)
ax.set_ylim(-50, 10)
ax.set_aspect('equal', 'box')
ax.set_xlabel("x-axis (East-West)  (m/s)")
ax.set_ylabel("y-axis (Up-Down)   (m/s)")
ax.set_title("Rain & Wind: Resultant Velocity and Umbrella Direction")
ax.grid(True, linestyle='--', linewidth=0.6)
ax.legend(loc='upper right')

# Save as PDF
out_pdf = "rain_velocity_with_c.pdf"
plt.savefig("/sdcard/Matrix/ee1030-2025/ai25btech11016/Matgeo/1.2.24/figs/1.2.24.png", bbox_inches='tight')
plt.show()


