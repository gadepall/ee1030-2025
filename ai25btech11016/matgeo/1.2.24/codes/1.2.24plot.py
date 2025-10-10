import numpy as np
import matplotlib.pyplot as plt

# Given speeds (m/s)
v_rain_down = 35       # rain relative to air (vertical down)
v_wind_ew   = 12       # wind from East to West (negative x)

# Vectors (x to East, y to North)
v_rw = np.array([0, -v_rain_down])   # rain wrt wind/air
v_w  = np.array([-v_wind_ew, 0])     # wind wrt ground
v_r  = v_rw + v_w                    # rain wrt ground (what we feel)

# Angle of tilt from vertical (in degrees)
theta = np.degrees(np.arctan2(abs(v_w[0]), abs(v_rw[1])))  # = arctan(12/35)

# Plot
fig, ax = plt.subplots(figsize=(7,7))
ax.set_aspect('equal', 'box')
ax.grid(True, linestyle='--', linewidth=0.6)
ax.set_xlim(-45, 15)
ax.set_ylim(-50, 15)

# Axes labels/title
ax.set_xlabel('East  →   (m/s)')
ax.set_ylabel('North ↑   (m/s)')
ax.set_title('Rain & Wind: Resultant Velocity and Umbrella Direction')

# Draw vectors from origin
def arrow(v, color, label):
    ax.quiver(0, 0, v[0], v[1], angles='xy', scale_units='xy', scale=1,
              width=0.007, color=color, label=label)

arrow(v_rw, 'tab:blue',   r'$\vec v_{r/w}=(0,-35)$')
arrow(v_w,  'tab:orange', r'$\vec v_{w}=(-12,0)$')
arrow(v_r,  'tab:red',    r'$\vec v_{r}=(-12,-35)$')

# Umbrella should be held opposite to rain's motion (i.e., into the apparent rain)
arrow(-v_r, 'tab:green', 'Hold umbrella this way')

# Annotate deflection angle from vertical
ax.annotate(fr'$\theta=\arctan\!\left(\frac{{12}}{{35}}\right)\approx{theta:.1f}^\circ$',
            xy=(0,0), xytext=(-6,-5), textcoords='offset points',
            fontsize=11, bbox=dict(boxstyle='round,pad=0.3', fc='white', ec='gray', alpha=0.8))

# Reference vertical (dashed) to show tilt
ax.plot([0,0], [0,-40], linestyle=':', color='gray')

ax.legend(loc='upper right')
plt.savefig("/sdcard/Matrix/ee1030-2025/ai25btech11016/Matgeo/1.2.24/figs/1.2.24.png")
plt.show()
