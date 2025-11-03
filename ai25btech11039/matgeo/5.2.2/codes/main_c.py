import ctypes, os
import numpy as np
import matplotlib.pyplot as plt

# ---- load the shared object (change to .dll on Windows) ----
lib = ctypes.CDLL(os.path.abspath("libsolve522.so"))

# void solve_522(double *u, double *v)
lib.solve_522.argtypes = [ctypes.POINTER(ctypes.c_double),
                          ctypes.POINTER(ctypes.c_double)]
lib.solve_522.restype  = None

# ---- call the C function to get (u0, v0) ----
u0 = ctypes.c_double()
v0 = ctypes.c_double()
lib.solve_522(ctypes.byref(u0), ctypes.byref(v0))
u0 = u0.value; v0 = v0.value
print(f"Solution from C: u = {u0}, v = {v0}")

# ---- plot the two lines and their intersection ----
u = np.linspace(-3, 3, 400)
v1 = (5*u + 8)/4.0          # 5u - 4v + 8 = 0
v2 = (9 - 7*u)/6.0          # 7u + 6v - 9 = 0

plt.figure(figsize=(7,5))
plt.plot(u, v1, label=r"$5u-4v+8=0$", linewidth=2)
plt.plot(u, v2, label=r"$7u+6v-9=0$", linewidth=2)

# mark the intersection returned by C
plt.scatter([u0], [v0], zorder=5)
plt.annotate(fr"$\left({u0:.3f},\,{v0:.3f}\right)$",
             (u0, v0), textcoords="offset points", xytext=(8, 8))

plt.axhline(0, linewidth=1); plt.axvline(0, linewidth=1)
plt.xlim(-3,3); plt.ylim(-2,4)
plt.grid(True, alpha=0.3)
plt.xlabel("$u$"); plt.ylabel("$v$")
plt.legend()
plt.title("Intersection of $5u-4v+8=0$ and $7u+6v-9=0$")

os.makedirs("figs", exist_ok=True)
plt.tight_layout()
plt.savefig("figs/5.2.2.png", dpi=300, bbox_inches="tight")
plt.show()

