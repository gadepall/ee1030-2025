import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

def check_parallel(a, b, c, d, tol=1e-9):
    a, b, c, d = map(np.array, (a, b, c, d))
    u = a - 2*d
    v = 2*b - c
    cross = np.cross(u, v)
    return np.linalg.norm(cross) < tol, u, v

def plot_vectors(a, b, c, d, u, v):
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')

    # Helper function to draw vector + label
    def draw_vector(vec, name, color, style="-", scale=1.2, offset=(0,0,0), lw=2.0):
        ax.quiver(0, 0, 0, vec[0], vec[1], vec[2],
                  color=color, linestyle=style,
                  arrow_length_ratio=0.08, linewidth=lw)
        ax.text(vec[0]*scale + offset[0],
                vec[1]*scale + offset[1],
                vec[2]*scale + offset[2],
                name, fontsize=10, weight="bold", color=color,
                bbox=dict(facecolor="white", alpha=0.7, edgecolor="none"))

    # Base vectors (unique colors + offsets to avoid overlap)
    draw_vector(a, "a", "red",    style="-",   offset=(0.4,  0.2, 0))
    draw_vector(c, "c", "blue",   style=":",   offset=(-0.4, -0.2, 0))
    draw_vector(b, "b", "green",  style="--",  offset=(0.3, -0.5, 0.3))   # shifted away
    draw_vector(d, "d", "purple", style="-.",  offset=(-0.3, 0.5, -0.3))  # opposite shift

    # Special vectors u and v (thicker lines)
    draw_vector(u, "u=a-2d", "black",   style="--", lw=2.5, scale=1.25, offset=(0.3,0.3,0))
    draw_vector(v, "v=2b-c", "orange",  style=":",  lw=2.5, scale=1.25, offset=(-0.3,-0.3,0))

    # Axis scaling
    all_vecs = np.array([a, b, c, d, u, v])
    max_range = np.max(np.abs(all_vecs)) * 1.5 + 1
    ax.set_xlim([-max_range, max_range])
    ax.set_ylim([-max_range, max_range])
    ax.set_zlim([-max_range, max_range])

    ax.set_xlabel("X-axis")
    ax.set_ylabel("Y-axis")
    ax.set_zlabel("Z-axis")
    ax.set_title("3D Vectors with Clear Labels and Colors")

    plt.show()

# ---------------- Example ----------------
if __name__ == "__main__":
    a = np.array([1, 2, 3])
    b = np.array([2, -1, 0])
    c = np.array([0, 4, 1])
    d = np.array([1, 0, -1])

    is_parallel, u, v = check_parallel(a, b, c, d)
    print("Parallel?", is_parallel)

    plot_vectors(a, b, c, d, u, v)

