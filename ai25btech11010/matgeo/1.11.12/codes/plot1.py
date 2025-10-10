import numpy as np
import matplotlib.pyplot as plt

def check_unit_sum_and_plot(a, b):
    # Ensure vectors are unit vectors
    a = a / np.linalg.norm(a)
    b = b / np.linalg.norm(b)
    
    # Compute vectors
    sum_vec = a + b
    diff_vec = a - b
    neg_b = -b
    
    # Magnitudes
    sum_mag = np.linalg.norm(sum_vec)
    diff_mag = np.linalg.norm(diff_vec)
    neg_b_mag = np.linalg.norm(neg_b)  # should be 1 since b is unit
    
    print(f"|a+b| = {sum_mag:.3f}")
    print(f"|a-b| = {diff_mag:.3f}")
    print(f"|−b|  = {neg_b_mag:.3f}")
    
    # Plot
    fig, ax = plt.subplots(figsize=(6,6))
    
    # Function to plot vectors
    def plot_vec(v, color, label):
        ax.arrow(0, 0, v[0], v[1], head_width=0.1, head_length=0.1,
                 fc=color, ec=color, length_includes_head=True)
        ax.text(v[0]*1.1, v[1]*1.1, f"{label}\n|{label}|={np.linalg.norm(v):.2f}", 
                color=color, fontsize=10, ha="center")
    
    # Plot all vectors
    plot_vec(a, "blue", "a")
    plot_vec(b, "green", "b")
    plot_vec(neg_b, "orange", "-b")
    plot_vec(sum_vec, "red", "a+b")
    plot_vec(diff_vec, "purple", "a-b")
    
    # Plot X and Y axes
    ax.axhline(0, color="black", linewidth=1)  # X-axis
    ax.axvline(0, color="black", linewidth=1)  # Y-axis
    
    ax.set_xlim(-2, 2)
    ax.set_ylim(-2, 2)
    ax.set_aspect("equal")
    ax.grid(True, linestyle="--", alpha=0.6)
    ax.set_title("Vectors a, b, -b, a+b, a-b with magnitudes and axes")
    
    # Save figure
    plt.savefig('../figs/vectors_plot.png', dpi=300, bbox_inches="tight")
    plt.show()

# Example: pick a along x-axis, b rotated by 120°
theta = 120 * np.pi / 180
a = np.array([1, 0])
b = np.array([np.cos(theta), np.sin(theta)])

check_unit_sum_and_plot(a, b)
