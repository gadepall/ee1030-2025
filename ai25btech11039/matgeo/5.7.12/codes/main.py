

import numpy as np
import matplotlib.pyplot as plt

# domain and polynomial
lam = np.linspace(0, 5, 400)
f = lam**2 - 5*lam + 6  # (lam-2)(lam-3)

plt.figure(figsize=(7, 4.5))
plt.plot(lam, f, linewidth=2)             # curve
plt.axhline(0, linewidth=1)               # x-axis
plt.axvline(0, linewidth=1)               # y-axis

# mark the roots
for r in (2, 3):
    plt.scatter([r], [0])
    plt.annotate(rf"$\lambda={r}$", (r, 0),
                 textcoords="offset points", xytext=(0, 8), ha="center")

plt.title(r"Characteristic Polynomial $f(\lambda)=\lambda^2-5\lambda+6$")
plt.xlabel(r"$\lambda$")
plt.ylabel(r"$f(\lambda)$")
plt.tight_layout()
plt.savefig("cayley_hamilton_parabola.png", dpi=200)
plt.show()
