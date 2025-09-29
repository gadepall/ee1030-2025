import ctypes as ct
import numpy as np
import matplotlib.pyplot as plt

# 1) load the shared library (same folder)
lib = ct.CDLL("./libradical_simple.so")

# 2) tell ctypes the C signature
# void radical_axis(double a1, const double u1[2], double f1,
#                   double a2, const double u2[2], double f2,
#                   double L_out[2], double *c_out);
lib.radical_axis.argtypes = [
    ct.c_double,                          # a1
    ct.POINTER(ct.c_double), ct.c_double, # u1, f1
    ct.c_double,                          # a2
    ct.POINTER(ct.c_double), ct.c_double, # u2, f2
    ct.POINTER(ct.c_double),              # L_out
    ct.POINTER(ct.c_double)               # c_out
]
lib.radical_axis.restype = None

# 3) problem data (Problem 9.8.34)
a1 = 3.0
u1 = np.array([-1.0, 6.0], dtype=np.double)
f1 = -9.0

a2 = 1.0
u2 = np.array([3.0, 1.0], dtype=np.double)
f2 = -15.0

# 4) outputs
L = np.zeros(2, dtype=np.double)
c = ct.c_double()   # <-- IMPORTANT: ctypes double, so we can pass byref

# 5) call C
lib.radical_axis(
    a1, u1.ctypes.data_as(ct.POINTER(ct.c_double)), f1,
    a2, u2.ctypes.data_as(ct.POINTER(ct.c_double)), f2,
    L.ctypes.data_as(ct.POINTER(ct.c_double)),
    ct.byref(c)  # pass the address of the ctypes double
)

print("Raw line from C: L =", L, "  c =", c.value)

# 6) scale to nice integers: (10, -3)^T x - 18 = 0
scale = -0.5  # because C gives L=[-20,6], c=36
L_scaled = L * scale
c_scaled = c.value * scale
print(f"Vector form: ({int(L_scaled[0])} \\\\ {int(L_scaled[1])})^T x {c_scaled:+.0f} = 0")

# 7) plot circles + line
def circle_center_radius(a, u, f):
    # V = a I; center = -u/a; r^2 = ||u||^2/a^2 - f/a
    center = -u / a
    r2 = (u @ u) / (a*a) - f / a
    return center, np.sqrt(r2)

c1, r1 = circle_center_radius(a1, u1, f1)
c2, r2 = circle_center_radius(a2, u2, f2)

theta = np.linspace(0, 2*np.pi, 400)
x1 = c1[0] + r1*np.cos(theta); y1 = c1[1] + r1*np.sin(theta)
x2 = c2[0] + r2*np.cos(theta); y2 = c2[1] + r2*np.sin(theta)

xmin = min(c1[0]-r1, c2[0]-r2) - 1
xmax = max(c1[0]+r1, c2[0]+r2) + 1
ymin = min(c1[1]-r1, c2[1]-r2) - 1
ymax = max(c1[1]+r1, c2[1]+r2) + 1

xx = np.linspace(xmin, xmax, 600)
if abs(L_scaled[1]) > 1e-12:
    yy = (-c_scaled - L_scaled[0]*xx) / L_scaled[1]
else:
    xx = np.full_like(xx, -c_scaled / L_scaled[0])
    yy = np.linspace(ymin, ymax, 600)

plt.figure()
plt.plot(x1, y1, label="C1: $3x^2+3y^2-2x+12y-9=0$")
plt.plot(x2, y2, label="C2: $x^2+y^2+6x+2y-15=0$")
plt.plot(xx, yy, label=r"Line: $(10,-3)^\top \vec{x} - 18 = 0$")
plt.gca().set_aspect('equal', adjustable='box')
plt.xlim(xmin, xmax); plt.ylim(ymin, ymax)
plt.grid(True); plt.legend()
plt.title("Radical axis through intersection points")
plt.xlabel("x"); plt.ylabel("y")
plt.savefig("radical.png")
plt.show()

