# 4.13.4 — Plot y = log10(x), y = 10^x, and the mirror line y = x
# Saves: figs/4.13.4.png
import os
import numpy as np
import matplotlib.pyplot as plt

# Domain for log10(x) and exp base-10
x1 = np.linspace(1e-3, 3, 400)        # for y = log10(x)
x2 = np.linspace(-3, 3, 400)          # for y = 10^x
y_log = np.log10(x1)
y_exp = 10**x2

# Sample pair to illustrate reflection through y=x
t = 2.0
Q = np.array([t, np.log10(t)])        # (t, log10 t)
R = np.array([np.log10(t), t])        # (log10 t, t)

plt.figure(figsize=(7.2, 5.2))
# Curves
plt.plot(x1, y_log, label=r"$y=\log_{10}x$", linewidth=2)
plt.plot(x2, y_exp, label=r"$y=10^{x}$", linewidth=2)
plt.plot(x2, x2,  '--', label=r"$y=x$", linewidth=1.5)   # mirror line

# Mark example points and the segment
plt.scatter(Q[0], Q[1], color='C0')
plt.text(Q[0]+0.05, Q[1], r"$\vec{Q}=(t,\log_{10}t)$", fontsize=10)
plt.scatter(R[0], R[1], color='C1')
plt.text(R[0]+0.05, R[1], r"$\vec{R}=(\log_{10}t,t)$", fontsize=10)
plt.plot([Q[0], R[0]], [Q[1], R[1]], color='0.3', linewidth=1)

plt.xlim(-3, 3)
plt.ylim(-3, 10)
plt.grid(True, alpha=0.3)
plt.xlabel("$x$")
plt.ylabel("$y$")
plt.legend()
plt.title("Reflection of $y=\\log_{10}x$ to $y=10^x$ about $y=x$")

os.makedirs("figs", exist_ok=True)
plt.tight_layout()
plt.savefig("figs/4.13.4.png", dpi=300, bbox_inches='tight')
plt.show()
