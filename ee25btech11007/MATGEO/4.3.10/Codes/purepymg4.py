import numpy as np
import matplotlib.pyplot as plt

# ---- NumPy helpers ----
def dot(u, v):
    u = np.asarray(u, dtype=float)
    v = np.asarray(v, dtype=float)
    if u.shape != v.shape:
        raise ValueError("dot: shapes must match")
    return float(np.dot(u, v))

def norm(u):
    u = np.asarray(u, dtype=float)
    return float(np.sqrt(np.dot(u, u)))

def normalize(u):
    u = np.asarray(u, dtype=float)
    r = norm(u)
    return u / r if r != 0.0 else np.zeros_like(u)

def line_direction_normal(a, b, c):
    # For ax + by = c:
    #   normal    n = (a, b)
    #   direction d = (-b, a)  (perpendicular to normal)
    d = np.array([-b, a], dtype=float)
    n = np.array([a, b], dtype=float)
    return d, n

# ---- Solve for x - y = 2 ----
a, b, c = 1.0, -1.0, 2.0
d, n = line_direction_normal(a, b, c)
ud, un = normalize(d), normalize(n)

print("Direction (raw):", d.tolist())           # [1.0, 1.0]
print("Normal   (raw):", n.tolist())            # [1.0, -1.0]
print("dot(direction, normal) =", dot(d, n))    # 0.0
print("Unit direction:", ud.tolist())
print("Unit normal   :", un.tolist())

# ---- Plot the line and the vectors ----
x = np.linspace(-2, 6, 200)
y = x - 2  # since y = x - 2

# Anchor point on the line
x0, y0 = 2.0, 0.0
scale = 2.0

plt.figure()
plt.plot(x, y, label="x - y = 2")
plt.quiver([x0], [y0], [ud[0]*scale], [ud[1]*scale],
           angles='xy', scale_units='xy', scale=1, label="direction")
plt.quiver([x0], [y0], [un[0]*scale], [un[1]*scale],
           angles='xy', scale_units='xy', scale=1, label="normal")
plt.gca().set_aspect('equal', adjustable='box')
plt.xlabel("x"); plt.ylabel("y")
plt.title("NumPy: line x - y = 2 with direction and normal")
plt.grid(True); plt.legend()
plt.show()
