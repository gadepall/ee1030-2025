import matplotlib.pyplot as plt

def solve_k():
    # Solve (1/2) * |12k + 14| = 52
    # => |12k + 14| = 104
    k1 = (104.0 - 14.0) / 12.0   # 7.5
    k2 = (-104.0 - 14.0) / 12.0  # -9.8333
    return k1, k2

if __name__ == "__main__":
    # Get possible k values
    k1, k2 = solve_k()
    print(f"Possible values of k: {k1:.2f}, {k2:.2f}")

    # Pick valid (positive) solution
    k = k1 if k1 > 0 else k2
    print(f"Chosen k = {k:.2f}")

    # Define triangle vertices
    A = (-2, 6)
    B = (2 * k, 4)
    C = (2 * k + 1, 10)

    # Plot triangle
    plt.figure(figsize=(7,7))
    plt.plot([A[0], B[0], C[0], A[0]],
             [A[1], B[1], C[1], A[1]],
             'b-', linewidth=2)

    # Red points for vertices
    plt.scatter([A[0], B[0], C[0]], [A[1], B[1], C[1]],
                color='red', s=80, zorder=5)

    # Annotate vertices
    plt.text(A[0]+0.2, A[1]+0.2, f"A{A}", fontsize=12)
    plt.text(B[0]+0.2, B[1]-0.4, f"B{B}", fontsize=12)
    plt.text(C[0]+0.2, C[1]+0.2, f"C{C}", fontsize=12)

    plt.title(f"Triangle with k = {k:.2f}")
    plt.grid(True)
    plt.axis("equal")

    # Save as fig4.png
    filename = "fig4.png"
    plt.savefig(filename, dpi=200)

    plt.show()
