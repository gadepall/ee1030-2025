import numpy as np
import matplotlib.pyplot as plt
import math

def compute_kappa(V, u, f, h, m):
    u = u.reshape(-1,1)
    h = h.reshape(-1,1)
    m = m.reshape(-1,1)
    
    mT_V_m = float(m.T @ V @ m)
    mT_Vh_u = float(m.T @ (V @ h + u))
    g_h = float(h.T @ V @ h + 2*u.T @ h + f)
    
    term = mT_Vh_u**2 - g_h * mT_V_m
    if term < 0:
        raise ValueError("Negative sqrt term, no real intersections")
    
    k1 = ( -mT_Vh_u + np.sqrt(term) ) / mT_V_m
    k2 = ( -mT_Vh_u - np.sqrt(term) ) / mT_V_m
    return k1, k2

def compute_area(a, n=20000):
    analytic = 0.5 * math.pi * a * a
    if n % 2 == 1:
        n += 1
    x = np.linspace(-a, a, n+1)
    y = np.sqrt(np.maximum(0.0, a*a - x*x))
    h = (2*a) / n
    S = y[0] + y[-1] + 4*y[1:-1:2].sum() + 2*y[2:-1:2].sum()
    numeric = (h/3) * S
    return analytic, numeric

# ===== Example Case (a = 4) =====
V = np.array([[1,0],[0,1]])
u = np.array([0,0])
f = -16   # a=4 ⇒ f = -a^2
h = np.array([0,0])
m = np.array([1,0])
a = 4

# Compute results
kappa_vals = compute_kappa(V,u,f,h,m)
area_vals = compute_area(a)

print("κ values =", kappa_vals)
print("Area (analytic) =", area_vals[0])
print("Area (numeric)  =", area_vals[1])

# ===== Plot directly =====
x = np.linspace(-a, a, 500)
y = np.sqrt(np.maximum(0, a*a - x*x))

plt.figure(figsize=(10,10))
plt.plot(x, y, label=r"$y=\sqrt{a^2-x^2}$")
plt.fill_between(x, y, 0, alpha=0.3, label="Area")

# Mark intersections
for k in kappa_vals:
    plt.scatter(k, 0, color="red", zorder=5)
    plt.text(k, -0.3, f"{k:.2f}", ha="center")

plt.xlabel("x")
plt.ylabel("y")
plt.title(f"Semicircle with κ and Area\nAnalytic={area_vals[0]:.4f}, Numeric={area_vals[1]:.4f}")
plt.legend()
plt.gca().set_aspect('equal', 'box')
plt.grid(True)

plt.show()
