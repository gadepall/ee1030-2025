import ctypes
import os
import matplotlib.pyplot as plt
import numpy as np
from matplotlib.patches import Arc

# --- 1. Compile and Load C Library ---
c_file = "line.c"
so_file = "line.so"
if os.system(f"gcc -shared -o {so_file} -fPIC {c_file}") != 0:
    print(f"Error: C compilation failed. Ensure '{c_file}' exists and is correct.")
    exit()

try:
    line_lib = ctypes.CDLL(f'./{so_file}')
    reflect_line_c = line_lib.reflect_line
    reflect_line_c.argtypes = [
        ctypes.c_double, ctypes.c_double, ctypes.c_double,
        ctypes.c_double, ctypes.c_double, ctypes.c_double,
        ctypes.POINTER(ctypes.c_double),
        ctypes.POINTER(ctypes.c_double),
        ctypes.POINTER(ctypes.c_double)
    ]
except Exception as e:
    print(f"Error loading shared library: {e}")
    exit()

# --- 2. Define Lines & Find Reflected Line L ---
print("\n--- Problem Setup ---")
a, b, c = 0.0, 1.0, 0.0 # Line L1 (Mirror): y = 0
print(f"Line L1 (Mirror): {a:.1f}x + {b:.1f}y + {c:.1f} = 0")

l, m, n = -0.57, 0.82, 0.0 # Line L2 (Source)
print(f"Line L2 (Source): {l:.2f}x + {m:.2f}y + {n:.1f} = 0")

res_a, res_b, res_c = ctypes.c_double(), ctypes.c_double(), ctypes.c_double()
reflect_line_c(l, m, n, a, b, c,
               ctypes.byref(res_a),
               ctypes.byref(res_b),
               ctypes.byref(res_c))
print(f"Found Line L (Reflection): {res_a.value:.2f}x + {res_b.value:.2f}y + {res_c.value:.2f} = 0")

# --- 3. Verify Angles ---
def get_angle(coeffs1, coeffs2):
    a1, b1, _ = coeffs1
    a2, b2, _ = coeffs2
    dot = abs(a1 * a2 + b1 * b2)
    mag1 = np.sqrt(a1**2 + b1**2)
    mag2 = np.sqrt(a2**2 + b2**2)
    
    # SAFETY CHECK: Prevent division by zero if a line is degenerate (0x + 0y + c = 0)
    if mag1 * mag2 == 0:
        return np.nan # Return "Not a Number" to signify an issue
    
    return np.degrees(np.arccos(dot / (mag1 * mag2)))

angle_L1_L2 = get_angle((a, b, c), (l, m, n))
angle_L1_L = get_angle((a, b, c), (res_a.value, res_b.value, res_c.value))

print("\n--- Angle Verification ---")
print(f"Angle θ between L1 and L2: {angle_L1_L2:.2f}°")

# SAFETY CHECK: Only print and use the angle if it's a valid number
if not np.isnan(angle_L1_L):
    print(f"Angle θ between L1 and L:  {angle_L1_L:.2f}°")
else:
    print("Angle θ between L1 and L: Calculation failed (degenerate line).")

# --- 4. Find Intersection Point P ---
P = (0.0, 0.0)
print(f"\nIntersection Point P is at ({P[0]:.2f}, {P[1]:.2f})")

# --- 5. Generate Plot ---
print("\n--- Generating Plot ---")
plt.style.use('seaborn-v0_8-whitegrid')
fig, ax = plt.subplots(figsize=(8, 8))
x = np.linspace(-3, 3, 400)

def get_y(a_val, b_val, c_val, x_vals):
    if abs(b_val) < 1e-9: return np.full_like(x_vals, np.nan)
    return (-a_val * x_vals - c_val) / b_val

ax.plot(x, get_y(a, b, c, x), 'royalblue', label='Line $L_1$')
ax.plot(x, get_y(l, m, n, x), color='seagreen', label='Line $L_2$')

# Only plot the reflected line if it's valid
if not np.isnan(angle_L1_L):
    ax.plot(x, get_y(res_a.value, res_b.value, res_c.value, x), 'crimson', linestyle='--', label='Reflected Line $L$')
    # Add angle arcs
    arc1 = Arc(P, 1.5, 1.5, theta1=180-angle_L1_L2, theta2=180, color='gray')
    ax.add_patch(arc1)
    ax.text(0.8, 0.4, r'$\theta$', fontsize=16)
    arc2 = Arc(P, 1.5, 1.5, theta1=0, theta2=angle_L1_L, color='gray')
    ax.add_patch(arc2)
    ax.text(-0.9, 0.4, r'$\theta$', fontsize=16)

ax.plot(P[0], P[1], 'ko', markersize=10, label='Intersection Point P')

ax.set_title('Line Reflection', fontsize=16)
ax.set_xlabel('x-axis'), ax.set_ylabel('y-axis')
ax.legend(), ax.axis('equal'), ax.set_xlim(-3, 3), ax.set_ylim(-3, 3)
plt.show()
