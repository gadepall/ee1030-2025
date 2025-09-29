import numpy as np
import matplotlib.pyplot as plt

def ellipse_params_from_foci(F1, F2, s):
    F1 = np.asarray(F1, dtype=float)
    F2 = np.asarray(F2, dtype=float)
    c  = 0.5 * (F1 + F2)
    a  = 0.5 * s
    d  = np.linalg.norm(F2 - F1)
    cf = 0.5 * d
    b2 = a*a - cf*cf
    if b2 <= 0:
        raise ValueError("Inputs do not define a real ellipse (b^2 <= 0).")
    b  = np.sqrt(b2)

    # Axis-aligned case (since foci are on a line here)
    V = np.diag([1.0/(a*a), 1.0/(b*b)])
    u = -V @ c
    f = float(c @ (V @ c) - 1.0)
    return V, u, f, c, a, b

def plot_ellipse(c, a, b, F1=None, F2=None, n=600):
    t = np.linspace(0, 2*np.pi, n)
    x = c[0] + a*np.cos(t)
    y = c[1] + b*np.sin(t)

    plt.plot(x, y, label="Locus")
    if F1 is not None and F2 is not None:
        plt.scatter([F1[0], F2[0]], [F1[1], F2[1]], label="Foci")
    plt.scatter([c[0]], [c[1]], label="Center")
    plt.gca().set_aspect("equal", adjustable="box")
    plt.grid(True)
    plt.legend(loc="upper left", bbox_to_anchor=(1.05, 1.0))
    plt.title("Locus from first principles → (V,u,f) → Plot")
    plt.tight_layout()
    plt.savefig("newellipse.png")
    plt.show()

# --- Given data ---
F1 = np.array([3.0, 0.0])
F2 = np.array([9.0, 0.0])
s  = 12.0  # sum of distances = 2a

V, u, f, c, a, b = ellipse_params_from_foci(F1, F2, s)

# Show results
print("V =\n", V)
print("u =", u)
print("f =", f)
print("center c =", c)
print("semi-axes a, b =", a, b)

# Plot
plot_ellipse(c, a, b, F1=F1, F2=F2)

