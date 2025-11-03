import numpy as np
import matplotlib.pyplot as plt

# Fixed vectors
A = np.array([1, 1, 2])
B = np.array([1, 2, 1])
C = np.array([1, 1, 1])   # updated C vector

def check_and_plot(D, save_path="../figures/plane.png"):
    """
    Check conditions for vector D and plot the plane with vectors A, B, C, D.
    Saves the figure at the given save_path.
    """
    # ---- Check conditions ----
    scalar_triple = np.dot(A, np.cross(B, D))   # coplanarity
    is_coplanar = np.isclose(scalar_triple, 0)

    dot_cd = np.dot(D, C)   # perpendicularity
    is_perpendicular = np.isclose(dot_cd, 0)

    print(f"\nVector D = {D}")
    print(f"Coplanar with A & B? {'Yes' if is_coplanar else 'No'}")
    print(f"Perpendicular to C (1,1,1)? {'Yes' if is_perpendicular else 'No'}")

    # ---- Plot ----
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')
    origin = np.array([0,0,0])

    # Plot vectors
    ax.quiver(*origin, *A, color='r', label='A (1,1,2)')
    ax.quiver(*origin, *B, color='g', label='B (1,2,1)')
    ax.quiver(*origin, *C, color='y', label='C (1,1,1)')
    ax.quiver(*origin, *D, color='b', label=f'D {D.tolist()}')

    # Plane formed by A & B
    normal = np.cross(A, B)
    xx, yy = np.meshgrid(range(-2, 3), range(-2, 3))
    z_plane = (-normal[0]*xx - normal[1]*yy) / normal[2]
    ax.plot_surface(xx, yy, z_plane, alpha=0.3, color='cyan')

    # Labels & formatting
    ax.set_xlabel('X')
    ax.set_ylabel('Y')
    ax.set_zlabel('Z')
    ax.legend()
    ax.set_title("Plane with A, B and D vector")

    # ---- Save ----
    plt.savefig(save_path, dpi=300)
    print(f"Figure saved at: {save_path}")
    plt.close()


# --------------- Example Usage ---------------
if __name__ == "__main__":
    D_vectors = [
        np.array([0, 1, -1]),
        np.array([1, 1, 0]),
        np.array([1, -1, 0]),
        np.array([0, 1, 1])
    ]

    for i, D in enumerate(D_vectors, start=1):
        save_path = f"../figures/plane_{i}.png"
        check_and_plot(D, save_path)

