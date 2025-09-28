import numpy as np
import matplotlib.pyplot as plt


def ellipse_vuf_from_foci(F1, F2, sum_dist):
    """
    Build (V, u, f) from foci and sum of distances (2a).
    Assumes axis-aligned ellipse when foci are collinear on x- or y-axis.
    """
    F1 = np.asarray(F1, dtype=float)
    F2 = np.asarray(F2, dtype=float)

    # Center and axes lengths
    c = (F1 + F2) / 2.0                   # center
    a = sum_dist / 2.0                    # semi-major
    cf = np.linalg.norm(F2 - F1) / 2.0    # half focal distance
    b2 = a * a - cf * cf
    if b2 <= 0:
        raise ValueError("Invalid inputs: b^2 <= 0 (no real ellipse).")
    b = np.sqrt(b2)

    # D = diag(1/a^2, 1/b^2), axis-aligned for this problem → V = D
    V = np.diag([1.0 / (a * a), 1.0 / (b * b)])

    # u = -V c,  f = c^T V c - 1
    u = -V @ c
    f = float(c @ (V @ c) - 1.0)

    return V, u, f, c, a, b


def recover_from_Vuf(V, u, f):
    """
    From (V, u, f), recover:
      c = -V^{-1} u
      f0 = u^T V^{-1} u - f
      eigendecomposition V = P diag(lam) P^T
      semi-axes via theory: a^2 = f0 / lam_min, b^2 = f0 / lam_max
    """
    V = np.asarray(V, dtype=float)
    u = np.asarray(u, dtype=float)

    # center
    c = -np.linalg.solve(V, u)

    # f0
    Vinv_u = np.linalg.solve(V, u)
    f0 = float(u @ Vinv_u - f)

    # eigen
    lam, P = np.linalg.eigh(V)  # lam sorted ascending, columns of P are eigenvectors

    # semi-axes from theory
    if np.any(lam <= 0):
        raise ValueError("V must be positive definite for an ellipse.")
    a = np.sqrt(f0 / lam[0])
    b = np.sqrt(f0 / lam[1])

    return c, f0, lam, P, a, b


def sample_ellipse_points(c, P, a, b, num=600):
    """
    Parametric ellipse in principal coordinates, then rotate+shift:
      z(t) = [a cos t; b sin t],  x(t) = P z(t) + c
    """
    t = np.linspace(0.0, 2.0 * np.pi, num)
    ellipse_local = np.vstack([a * np.cos(t), b * np.sin(t)])  # shape (2, N)
    ellipse_global = (P @ ellipse_local).T + c                 # shape (N, 2)
    return ellipse_global


def main():
    # ----- Problem data -----
    F1 = np.array([3.0, 0.0])
    F2 = np.array([9.0, 0.0])
    sum_dist = 12.0  # 2a

    # ----- Build V, u, f as per the align-derivation -----
    V, u, f, c_direct, a_direct, b_direct = ellipse_vuf_from_foci(F1, F2, sum_dist)

    print("From direct construction (D, V=D, u=-Vc, f=c^T V c - 1):")
    print("V =\n", V)
    print("u =", u)
    print("f =", f)
    print("center c (from foci) =", c_direct)
    print("a (from foci,sum) =", a_direct, "   b =", b_direct)
    print()

    # ----- Recover via theory from (V, u, f) -----
    c, f0, lam, P, a, b = recover_from_Vuf(V, u, f)

    print("Recovered from (V,u,f) via theory:")
    print("c = -V^{-1}u =", c)
    print("f0 = u^T V^{-1} u - f =", f0)
    print("Eigenvalues lam =", lam)
    print("Eigenvectors P =\n", P)
    print("Semi-axes from f0/lam: a =", a, " b =", b)
    print()

    # ----- Plot using principal-axis parametric form + transform -----
    pts = sample_ellipse_points(c, P, a, b, num=600)

    plt.plot(pts[:, 0], pts[:, 1], label="Ellipse")
    plt.scatter([F1[0], F2[0]], [F1[1], F2[1]], label="Foci")
    plt.scatter([c[0]], [c[1]], label="Center")
    plt.gca().set_aspect("equal", adjustable="box")
    plt.legend(loc="upper left", bbox_to_anchor=(1.05, 1.0))
    plt.grid(True)
    plt.title("Ellipse from (V,u,f) — theory-consistent build")
    plt.tight_layout()
    plt.savefig("newellipse.png")
    plt.show()


if __name__ == "__main__":
    main()

