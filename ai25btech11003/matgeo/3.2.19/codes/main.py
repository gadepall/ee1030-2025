import subprocess
import numpy as np
import matplotlib.pyplot as plt
import math
from matplotlib.patches import Arc

# Re-run the C executable to regenerate main.dat
#subprocess.run(["./main.so"], check=True)

# Read alphas (degrees) from main.dat
alphas = []
with open("main.dat") as f:
    for line in f:
        val = line.strip()
        alphas.append(None if val.lower() == "nan" else float(val))

# Side lengths
b = 1.5
c = 5.0

for i, alpha in enumerate(alphas, start=1):
    fig, ax = plt.subplots()
    ax.set_aspect("equal")
    ax.axhline(0, color="black", linewidth=0.5)
    ax.axvline(0, color="black", linewidth=0.5)

    # Point A shifted slightly left; label shifted slightly right
    A = np.array([-0.0, 0.0])
    ax.plot(*A, "ko")
    ax.text(A[0] + 0.1, A[1]-0.2, "A(0,0)", ha="left")

    # Point C
    C = np.array([b, 0.0])
    ax.plot(*C, "ko")
    ax.text(C[0], C[1] - 0.2, "C(1.5,0)", ha="center")

    if alpha is not None:
        rad = math.radians(alpha)
        B = np.array([c * math.cos(rad), c * math.sin(rad)])
        ax.plot(*B, "ko")
        ax.text(B[0], B[1] + 0.1, f"B({B[0]:.2f},{B[1]:.2f})", ha="center")

        # Draw triangle edges
        ax.plot([A[0], B[0], C[0], A[0]],
                [A[1], B[1], C[1], A[1]], "b-")

        # Draw angle arc at A
        arc = Arc(A, width=1.0, height=1.0, angle=0,
                  theta1=0, theta2=alpha, color="red")
        ax.add_patch(arc)

        # Place alpha label inside triangle near A
        mid_angle = math.radians(alpha / 2)
        lx = A[0] + 0.6 * math.cos(mid_angle)
        ly = A[1] + 0.6 * math.sin(mid_angle)
        ax.text(lx, ly, f"α={alpha:.2f}°", color="red",
                fontsize=10, ha="center", va="center")
    else:
        # Still plot B at horizontal projection and label it
        B = np.array([c, 0.0])
        ax.plot(*B, "ko")
        ax.text(B[0], B[1] + 0.1, f"B({B[0]:.2f},{B[1]:.2f})", ha="center")

        ax.text(0.5, 0.5, "No valid\ntriangle",
                transform=ax.transAxes,
                ha="center", va="center",
                fontsize=12, color="red")

    ax.set_xlabel("X")
    ax.set_ylabel("Y")
    ax.set_xlim(-1, 6)
    ax.set_ylim(-1, 4)
    ax.set_xticks(np.arange(-1, 7, 1))
    ax.set_yticks(np.arange(-1, 5, 1))
    plt.tight_layout()
    plt.savefig(f"fig{i}.png", dpi=300)
    plt.close()

