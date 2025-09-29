import ctypes
import numpy as np
import matplotlib.pyplot as plt

# Load the shared library
lib = ctypes.CDLL('./mat.so')

# Define argument types
lib.compute_vectors.argtypes = [ctypes.c_double, ctypes.c_double,
                                np.ctypeslib.ndpointer(dtype=np.double, ndim=1, flags='C_CONTIGUOUS'),
                                np.ctypeslib.ndpointer(dtype=np.double, ndim=1, flags='C_CONTIGUOUS')]

def get_vectors(alpha_deg, theta_deg):
    P = np.zeros(2, dtype=np.double)
    Q = np.zeros(2, dtype=np.double)
    lib.compute_vectors(alpha_deg, theta_deg, P, Q)
    return P, Q

# Example angles
alpha_deg = 30.0
theta_deg = 45.0

P, Q = get_vectors(alpha_deg, theta_deg)

# Plot setup
plt.figure(figsize=(6,6))
plt.grid(True)
plt.gca().set_aspect('equal', adjustable='box')
max_val = max(np.linalg.norm(P), np.linalg.norm(Q)) + 0.3
plt.xlim(-max_val, max_val)
plt.ylim(-max_val, max_val)

plt.axhline(0, color='black', linewidth=1)
plt.axvline(0, color='black', linewidth=1)

plt.plot(0, 0, 'ko')
plt.quiver(0, 0, P[0], P[1], angles='xy', scale_units='xy', scale=1, color='blue', label=r'$\mathbf{P}$')
plt.quiver(0, 0, Q[0], Q[1], angles='xy', scale_units='xy', scale=1, color='red', label=r'$\mathbf{Q}$')

# Plot rotation arc
theta_rad = np.radians(theta_deg)
alpha_rad = np.radians(alpha_deg)
arc_theta = np.linspace(theta_rad, theta_rad - alpha_rad, 100)
arc_x = 0.5 * np.cos(arc_theta)
arc_y = 0.5 * np.sin(arc_theta)
plt.plot(arc_x, arc_y, 'green', linestyle='--', label=f'{alpha_deg:.1f}°')

plt.xlabel('X')
plt.ylabel('Y')
plt.legend()
plt.savefig('2.png')
plt.show()

