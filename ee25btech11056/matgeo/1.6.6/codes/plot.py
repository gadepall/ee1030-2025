
import numpy as np
import matplotlib.pyplot as plt

def plot_points(filename, labels, title, output_file):
    points = np.loadtxt(filename, delimiter=',', usecols=(0,1))
    x = points[:,0]
    y = points[:,1]

    plt.plot(x, y, 'o-', label='Collinear Points')

    for i, txt in enumerate(labels):
        plt.annotate(f"{txt}{tuple(points[i])}", (x[i], y[i]),
                     xytext=(5,-5), textcoords="offset points")

    plt.xlabel("X-axis")
    plt.ylabel("Y-axis")
    plt.title(title)
    plt.legend()
    plt.grid(True)

    plt.savefig(output_file)
    print(f"Saved figure as {output_file}")
    plt.close()

# ---- Part (a) ----
plot_points("points_a.dat", ["A","B","C"],
            "Collinear Points (Q1.6.6 a)", "fig_a.png")

# ---- Part (b) ----
plot_points("points_b.dat", ["A","B","C"],
            "Collinear Points (Q1.6.6 b)", "fig_b.png")

