import numpy as np
import matplotlib.pyplot as plt

# --- choose 2D unit vectors (you can edit these) ---
theta_true = np.deg2rad(45)           # 45°
a = np.array([1.0, 0.0])              # unit along +x
b = np.array([np.cos(theta_true), np.sin(theta_true)])  # unit at 45°

# --- compute angle θ (in degrees) ---
dot = float(np.dot(a, b))
na  = float(np.linalg.norm(a))
nb  = float(np.linalg.norm(b))
cos_theta = dot / (na * nb)
cos_theta = max(-1.0, min(1.0, cos_theta))  # clamp for safety
theta_deg = float(np.degrees(np.arccos(cos_theta)))

# --- check the condition ||a||=||b||=||a-√2 b||=1 ---
c = a - np.sqrt(2.0) * b
print(f"θ = {theta_deg:.2f}°,  ||a||={na:.2f}, ||b||={nb:.2f}, ||a-√2 b||={np.linalg.norm(c):.2f}")

# --- plot unit circle + vectors ---
t = np.linspace(0, 2*np.pi, 400)
plt.figure(figsize=(6,6))
plt.plot(np.cos(t), np.sin(t), label="Unit circle")
plt.quiver(0,0, a[0], a[1], angles='xy', scale_units='xy', scale=1, label="a")
plt.quiver(0,0, b[0], b[1], angles='xy', scale_units='xy', scale=1, label="b")
plt.quiver(0,0, c[0], c[1], angles='xy', scale_units='xy', scale=1, label="a − √2 b")

# angle arc (purely for illustration)
arc = np.linspace(0, np.deg2rad(theta_deg), 100)
plt.plot(0.25*np.cos(arc), 0.25*np.sin(arc))
plt.text(0.32*np.cos(np.deg2rad(theta_deg)/2),
         0.32*np.sin(np.deg2rad(theta_deg)/2),
         rf"$\theta={theta_deg:.0f}^\circ$")

plt.gca().set_aspect('equal', adjustable='box')
plt.grid(True, linewidth=0.4, alpha=0.5)
plt.xlim(-1.6, 1.6); plt.ylim(-1.6, 1.6)
plt.legend(); plt.title("a, b, and a − √2 b"); plt.tight_layout()
plt.show()
