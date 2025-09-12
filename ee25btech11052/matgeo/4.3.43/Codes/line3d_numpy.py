import numpy as np
import matplotlib.pyplot as plt

def parametric_line(P1, P2, lambdas):
    P1, P2 = np.array(P1), np.array(P2)
    direction = P2 - P1
    return P1[0] + lambdas * direction[0], \
           P1[1] + lambdas * direction[1], \
           P1[2] + lambdas * direction[2]

if __name__ == "__main__":
    P1 = (3, -2, -5)
    P2 = (3, -2, 6)
    lambdas = np.linspace(-1, 2, 50)

    xs, ys, zs = parametric_line(P1, P2, lambdas)

    fig = plt.figure()
    ax = fig.add_subplot(111, projection="3d")
    ax.plot(xs, ys, zs, 'k--', label="Line")
    ax.scatter(*P1, color="red", label="P1 (3,-2,-5)")
    ax.scatter(*P2, color="blue", label="P2 (3,-2,6)")

    ax.set_xlabel("X")
    ax.set_ylabel("Y")
    ax.set_zlabel("Z")
    ax.legend()
    plt.show()
