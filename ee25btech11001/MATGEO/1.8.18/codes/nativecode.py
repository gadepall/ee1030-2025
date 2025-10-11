# findy_plot.py
import ctypes
from ctypes import c_double, POINTER, byref, c_int
import numpy as np
import matplotlib.pyplot as plt
from pathlib import Path
import sys

# load the shared library (libfindy.so must be in the same directory)
lib_path = Path(__file__).with_name('code.so')
lib = ctypes.CDLL(str(lib_path))

# declare argument and return types
lib.find_y.argtypes = [c_double, c_double, c_double, c_double, POINTER(c_double), POINTER(c_double)]
lib.find_y.restype = c_int

def find_y_py(x1, y1, x2, d):
    """Wrapper around the C function. Returns a list of real solutions (possibly empty)."""
    out1 = c_double()
    out2 = c_double()
    n = lib.find_y(x1, y1, x2, d, byref(out1), byref(out2))
    if n == 0:
        return []
    elif n == 1:
        return [out1.value]
    else:
        return [out1.value, out2.value]

def plot_solution(x1, y1, x2, sols, d, savefile='findy_plot.png'):
    """Plot circle (center P, radius d), the vertical x=x2 line and solution points."""
    theta = np.linspace(0, 2*np.pi, 400)
    circ_x = x1 + d * np.cos(theta)
    circ_y = y1 + d * np.sin(theta)

    plt.figure(figsize=(6,6))
    plt.plot(circ_x, circ_y, label=f'Circle center P({x1},{y1}), r={d}')
    plt.axvline(x=x2, linestyle=':', label=f'x = {x2}')

    # plot P
    plt.scatter([x1], [y1], zorder=5)
    plt.annotate(f'P({x1},{y1})', (x1, y1), textcoords="offset points", xytext=(6,6))

    # plot Q solutions
    for i, yq in enumerate(sols):
        plt.scatter([x2], [yq], zorder=6)
        plt.annotate(f'Q{i+1}({x2},{yq})', (x2, yq), textcoords="offset points", xytext=(6,6))
        # line between P and Q
        plt.plot([x1, x2], [y1, yq], linestyle='--')

    plt.gca().set_aspect('equal', 'box')
    plt.grid(True)
    plt.legend()
    plt.title(f'Solutions y = {sols}' if sols else 'No real solution')
    plt.savefig(savefile, dpi=150)
    plt.show()

if __name__ == '__main__':
    # Usage:
    #   python3 findy_plot.py x1 y1 x2 d
    # If no args supplied, a default example is used: P(2,-3), x2=10, d=10
    if len(sys.argv) == 5:
        x1 = float(sys.argv[1])
        y1 = float(sys.argv[2])
        x2 = float(sys.argv[3])
        d  = float(sys.argv[4])
    else:
        x1, y1, x2, d = 2.0, -3.0, 10.0, 10.0
        print("No arguments provided — using default example P(2,-3), x2=10, d=10.")
        print("To specify custom values run: python3 findy_plot.py x1 y1 x2 d")

    sols = find_y_py(x1, y1, x2, d)
    if not sols:
        print("No real solutions for the given inputs.")
    else:
        print("y solutions:", sols)

    plot_solution(x1, y1, x2, sols, d)

