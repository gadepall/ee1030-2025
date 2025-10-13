import numpy as np
import matplotlib.pyplot as plt
import ctypes

intersection = ctypes.CDLL('./intersection.so')

intersection.function.argtypes = [
    ctypes.POINTER(ctypes.c_double),
    ctypes.POINTER(ctypes.c_double),
    ctypes.c_double, 
    ctypes.POINTER(ctypes.c_double),
    ctypes.POINTER(ctypes.c_double),
    ctypes.POINTER(ctypes.c_double)
]
intersection.function.restype = None

def get_kappa(V, u, f, h, m):
    V_c = V.astype(np.float64).flatten()
    u_c = u.astype(np.float64).flatten()
    h_c = h.astype(np.float64).flatten()
    m_c = m.astype(np.float64).flatten()
    kappa_out = ctypes.c_double(0)
    intersection.function(
        V_c.ctypes.data_as(ctypes.POINTER(ctypes.c_double)),
        u_c.ctypes.data_as(ctypes.POINTER(ctypes.c_double)),
        f,
        h_c.ctypes.data_as(ctypes.POINTER(ctypes.c_double)),
        m_c.ctypes.data_as(ctypes.POINTER(ctypes.c_double)),
        ctypes.byref(kappa_out) # Pass the output variable by reference
    )
    return kappa_out.value

V = np.identity(2)
u = np.zeros(2, dtype=np.float64)
f = -32.0
h = np.zeros(2, dtype=np.float64)
m_line = np.array([1, 1], dtype=np.float64)
m_axis = np.array([1, 0], dtype=np.float64)

kappa_line = get_kappa(V, u, f, h, m_line)
kappa_axis = get_kappa(V, u, f, h, m_axis)

P_line = h + kappa_line * m_line
P_axis = h + kappa_axis * m_axis
P_origin = np.zeros(2, dtype=np.float64)

radius = np.sqrt(32)
theta = np.linspace(0, 2 * np.pi, 200)
x_circ = radius * np.cos(theta)
y_circ = radius * np.sin(theta)

plt.figure(figsize=(10, 10))
plt.plot(x_circ, y_circ, 'b-', label=r'Circle: $x^2+y^2=32$')
plt.plot([-radius, radius], [-radius, radius], 'r-', label=r'Line: $y=x$')
plt.axhline(0, color='g', label=r'Line: $y=0$ (x-axis)')

x_fill1 = np.linspace(0, P_line[0], 100)
plt.fill_between(x_fill1, 0, x_fill1, color='lightblue', alpha=0.6)
x_fill2 = np.linspace(P_line[0], P_axis[0], 100)
y_fill2_arg = np.clip(32 - x_fill2**2, 0, None)
y_fill2 = np.sqrt(y_fill2_arg)
plt.fill_between(x_fill2, 0, y_fill2, color='lightblue', alpha=0.6, label=r'Area = $4\pi$')

plt.plot(P_line[0], P_line[1], 'ko')
plt.plot(P_axis[0], P_axis[1], 'ko')
plt.text(P_line[0] + 0.2, P_line[1], f'({P_line[0]:.2f}, {P_line[1]:.2f})')
plt.text(P_axis[0], P_axis[1] - 0.4, f'({P_axis[0]:.2f}, {P_axis[1]:.2f})', ha='center')

plt.title("Area in First Quadrant")
plt.xlabel('$x$')
plt.ylabel('$y$')
plt.grid(True, linestyle='--')
plt.gca().set_aspect('equal', adjustable='box')
plt.legend(bbox_to_anchor=(1.02, 1), loc='upper left')
plt.tight_layout()
plt.savefig("../figs/plot_c.jpg")
plt.show()
