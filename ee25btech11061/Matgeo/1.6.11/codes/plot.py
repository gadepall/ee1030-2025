import argparse, os, ctypes
import numpy as np
import matplotlib
if not os.environ.get("DISPLAY"):
    matplotlib.use("Agg")
import matplotlib.pyplot as plt

# load C lib
lib = ctypes.CDLL("./collinear.so")
lib.relation.argtypes = [ctypes.c_int, ctypes.c_int]
lib.relation.restype  = ctypes.c_int

def main():
    ap = argparse.ArgumentParser(description="Plot A(1,2), O(0,0), C(a,b) and line y=2x")
    ap.add_argument("--a", type=float, default=3.0)
    ap.add_argument("--b", type=float, default=6.0)
    ap.add_argument("--save", type=str, default="collinearity_plot.png")
    ap.add_argument("--no-show", action="store_true")
    args = ap.parse_args()

    A = (1.0, 2.0)
    O = (0.0, 0.0)
    C = (args.a, args.b)

    # residual from shared lib (int API, for display)
    r_int = lib.relation(int(round(args.a)), int(round(args.b)))

    # line y = 2x through O and A
    x_min = min(-1.0, O[0], A[0], C[0]) - 0.5
    x_max = max(4.0,  O[0], A[0], C[0]) + 0.5
    xs = np.linspace(x_min, x_max, 400)
    ys = 2 * xs

    plt.figure(figsize=(7,5))
    plt.plot(xs, ys, label="Line through O and A: y = 2x")
    plt.scatter([O[0], A[0], C[0]], [O[1], A[1], C[1]], s=80, marker="x")
    plt.text(O[0]+0.05, O[1]+0.05, "O(0,0)")
    plt.text(A[0]+0.05, A[1]+0.05, "A(1,2)")
    plt.text(C[0]+0.05, C[1]+0.05, f"C({C[0]:.3g},{C[1]:.3g})")

    status = "COLLINEAR" if r_int == 0 else "NOT collinear"
    plt.title(f"A, O, C: {status}  (residual b-2a = {r_int})")
    plt.xlabel("x"); plt.ylabel("y"); plt.grid(True); plt.legend(); plt.axis("equal"); plt.tight_layout()

    plt.savefig(args.save, dpi=150)
    print(f"Residual (b - 2a) = {r_int}  ->  {status}")
    print(f"Plot saved to: {args.save}")

    if not args.no_show and matplotlib.get_backend().lower() not in {"agg"}:
        plt.show()

if __name__ == "__main__":
    main()

