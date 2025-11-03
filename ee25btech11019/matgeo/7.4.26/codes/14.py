import ctypes
import numpy as np
import matplotlib.pyplot as plt

# Load C shared library
lib = ctypes.CDLL("./14.so")
lib.check_condition.argtypes = [ctypes.c_double, ctypes.c_double]
lib.check_condition.restype = ctypes.c_double

# Example satisfying p^2 = 8q^2
q = 1
p = np.sqrt(8)*q

# Check condition
result = lib.check_condition(p, q)
print("Condition (p^2 - 8q^2):", result)

# Circle parameters
center = (p/2, q/2)
r = np.sqrt(p**2 + q**2) / 2

# Circle points
theta = np.linspace(0, 2*np.pi, 400)
x = center[0] + r*np.cos(theta)
y = center[1] + r*np.sin(theta)

# Equation of circle: x^2 + y^2 = px + qy
# Chord bisected by x-axis => midpoint (a,0)
# Use geometry: intersection points satisfy y = m(x - a)
# Here we directly choose two bisecting chords manually

# Two chords bisected by x-axis when p^2 = 8q^2
# Their midpoints are symmetric about the y-axis
a1 = p/4
a2 = -p/4

def chord_points(a):
    """Return intersection points of chord with circle."""
    # Substitute y = m(x - a), but since midpoint is (a,0), chord is vertical reflection
    # Equation of chord perpendicular to y=0 at (a,0)
    # So x = a ± sqrt(r^2 - (a - p/2)^2)
    dy = np.sqrt(r**2 - (a - p/2)**2)
    x1, x2 = a, a
    y1, y2 = dy, -dy
    return np.array([[x1, y1], [x2, y2]])

# Compute chord endpoints
chord1 = chord_points(a1)
chord2 = chord_points(a2)

# Plot setup
plt.figure(figsize=(6,6))
plt.plot(x, y, 'b', label='Circle')
plt.scatter(p, q, color='r', label='Point (p,q)')
plt.scatter(center[0], center[1], color='g', label='Center (p/2,q/2)')
plt.axhline(0, color='k', linestyle='--', label='X-axis')

# Draw the two chords
plt.plot(chord1[:,0], chord1[:,1], 'm', linewidth=2, label='Chord 1')
plt.plot(chord2[:,0], chord2[:,1], 'orange', linewidth=2, label='Chord 2')

# Annotations
plt.text(p, q, f'({p:.2f},{q:.2f})', fontsize=10, ha='left')
plt.text(center[0], center[1], 'C', fontsize=10, ha='left')

plt.xlabel('x')
plt.ylabel('y')
plt.title('Two distinct chords bisected by X-axis')
plt.legend()
plt.axis('equal')
plt.grid(True)
plt.show()
