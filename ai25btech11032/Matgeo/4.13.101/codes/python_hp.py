# plot_hp_pure_python.py

import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D  # noqa: F401 (needed for 3D projection)

def row_reduce_3x4(A_in):
    A = np.asarray(A_in, dtype=float, order='C').copy()
    if A.shape != (3,4):
        raise ValueError("A_in must be shape (3,4)")
    # R2 <- R2 - 10 R1
    A[1,:] = A[1,:] - 10.0 * A[0,:]
    # R3 <- R3 - (qr) R1 (use qr from original A_in)
    qr = float(A_in[2,0])
    A[2,:] = A[2,:] - qr * A[0,:]
    # s = (pr - qr) / 90  (pr from original)
    pr = float(A_in[2,1])
    s = (pr - qr) / 90.0
    A[2,:] = A[2,:] - s * A[1,:]
    return A

def analyze_system(p, q, r, tol=1e-12):
    D = p*q - 11.0*p*r + 10.0*q*r
    E = (p*r - 10.0*q*r) / 9.0
    if abs(D) > tol:
        return 0, D, E
    if abs(E) > tol:
        return 1, D, E
    return 2, D, E

def parametric_solution(t):
    x = 10.0 * t + 10.0/9.0
    y = -11.0 * t - 1.0/9.0
    z = t
    return x, y, z

if __name__ == "__main__":
    # Choose (p,q,r). For consistent test use (100,10,1)
    p, q, r = 100.0, 10.0, 1.0

    # Build augmented matrix [M | b]
    A = np.array([
        [1.0,     1.0,    1.0,    1.0],
        [10.0,  100.0, 1000.0,    0.0],
        [q*r,   p*r,   p*q,       0.0]
    ], dtype=float)

    print("Input augmented matrix [M | b]:")
    np.set_printoptions(precision=6, suppress=True)
    print(A)

    # Row-reduce with the exact steps used in math writeup
    A_red = row_reduce_3x4(A)
    print("\nReduced augmented matrix after specified elimination steps:")
    print(A_red)

    # Analyze with D,E
    code, D, E = analyze_system(p, q, r)
    status = {0: "unique solution (D != 0)", 1: "inconsistent (no solution)", 2: "infinitely many solutions"}
    print(f"\nanalyze_system -> code={code}, D={D:.6g}, E={E:.6g}  => {status[code]}")

    # If consistent, plot only the 3D solution curve
    if code == 2:
        ts = np.linspace(-1.0, 1.0, 401)
        xs = np.empty_like(ts); ys = np.empty_like(ts); zs = np.empty_like(ts)
        for i,t in enumerate(ts):
            xs[i], ys[i], zs[i] = parametric_solution(t)

        fig = plt.figure(figsize=(7,7))
        ax = fig.add_subplot(111, projection='3d')
        ax.plot(xs, ys, zs, lw=2)
        ax.set_xlabel('x'); ax.set_ylabel('y'); ax.set_zlabel('z')
        ax.set_title(f'Solution curve (p={p}, q={q}, r={r})')
        plt.tight_layout()
        outname = "hp_3d_pure_python.png"
        fig.savefig(outname, dpi=200)
        print("\nSaved 3D plot:", outname)
    else:
        print("\nSystem not consistent — nothing to plot.")

