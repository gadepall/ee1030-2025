import numpy as np
import matplotlib.pyplot as plt
import matplotlib.patches as patches
from libs.funcs import * 

P = np.array([[0], [0]])
theta_deg = 35
theta_rad = np.deg2rad(theta_deg)

# --- 2. Construct the Lines Geometrically ---
n1 = np.array([[0], [1]])
n2 = rotmat(theta_rad) @ n1
n_L = rotmat(-theta_rad) @ n1

# --- 3. Generate Points for Plotting ---
m1 = omat @ n1
m2 = omat @ n2
m_L = omat @ n_L
line_length = 5
x_L1 = line_dir_pt(m1, P, -line_length, line_length)
x_L2 = line_dir_pt(m2, P, -line_length, line_length)
x_L = line_dir_pt(m_L, P, -line_length, line_length)

# --- 4. Create a Clean and Clear Plot ---
plt.style.use('seaborn-v0_8-whitegrid')
fig, ax = plt.subplots(figsize=(10, 10))

ax.plot(x_L1[0, :], x_L1[1, :], color='royalblue', linewidth=2.5, label='Line $L_1$')
ax.plot(x_L2[0, :], x_L2[1, :], color='seagreen', linewidth=2.5, label='Line $L_2$')
ax.plot(x_L[0, :], x_L[1, :], color='crimson', linestyle='--', linewidth=2.5, label='Reflected Line $L$')
ax.plot(P[0], P[1], 'o', color='black', markersize=9, label='Intersection Point P')

# --- 5. Add Line Equation Labels ---
eq1 = "$y = 0$"
eq2 = f"${n2[0,0]:.2f}x + {n2[1,0]:.2f}y = 0$"
eqL = f"${n_L[0,0]:.2f}x + {n_L[1,0]:.2f}y = 0$"

ax.text(1.5, 0.15, eq1, color='royalblue', fontsize=12, va='bottom', backgroundcolor='white')
ax.text(-2.4, 1.7, eq2, color='seagreen', fontsize=12, rotation=-theta_deg, va='bottom', backgroundcolor='white')
ax.text(-2.4, -2.0, eqL, color='crimson', fontsize=12, rotation=theta_deg, va='bottom', backgroundcolor='white')

# --- 6. Add Angle Annotations ---
arc_radius = 1.5
arc1 = patches.Arc(P.flatten(), arc_radius, arc_radius, angle=90, 
                   theta1=0, theta2=theta_deg, color='gray', linewidth=2)
arc2 = patches.Arc(P.flatten(), arc_radius, arc_radius, angle=90, 
                   theta1=-theta_deg, theta2=0, color='gray', linewidth=2)
ax.add_patch(arc1)
ax.add_patch(arc2)
ax.text(0.8 * np.cos(np.deg2rad(18)), 0.8 * np.sin(np.deg2rad(18)), r'$\theta$', fontsize=18)
ax.text(0.8 * np.cos(np.deg2rad(-18)), 0.8 * np.sin(np.deg2rad(-18)), r'$\theta$', fontsize=18)

# --- 7. Finalize and Show the Plot ---
ax.set_title(f'Line Reflection with Angle $\\theta = {theta_deg}^\\circ$', fontsize=16)
ax.set_xlabel('x-axis', fontsize=12)
ax.set_ylabel('y-axis', fontsize=12)
ax.set_aspect('equal', adjustable='box')
lim = 2.8
ax.set_xlim(-lim, lim)
ax.set_ylim(-lim, lim)
ax.legend(fontsize=11)


plt.show()
