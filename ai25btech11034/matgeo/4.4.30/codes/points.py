import os
import numpy as np
import sympy as sp
import matplotlib.pyplot as plt

def points_coplanarity_and_plot():
    print("Enter 4 points in 3D (space separated, fractions allowed), e.g.:")
    pts_sym = []
    for i in range(4):
        toks = input(f"Point {i+1}: ").split()
        if len(toks) != 3:
            raise ValueError("Each point must have 3 components.")
        pts_sym.append([sp.Rational(t) for t in toks])

    # Sympy matrix of points (rows) and augmented matrix with 1s
    M_aug = sp.Matrix([row + [1] for row in pts_sym])  # 4x4
    rank_aug = M_aug.rank()

    print("\nAugmented matrix [x y z 1]:")
    sp.pprint(M_aug)
    print(f"\nrank([x y z 1]) = {rank_aug}")

    coplanar = (rank_aug <= 3)
    if coplanar:
        print("✅ Points are coplanar (affine rank ≤ 3).")
    else:
        print("❌ Points are NOT coplanar (affine rank = 4).")

    # Convert to numpy floats for plotting
    pts = np.array([[float(v) for v in row] for row in pts_sym], dtype=float)

    # 3D plot
    fig = plt.figure(figsize=(7,6))
    ax = fig.add_subplot(111, projection='3d')

    # Plot points with labels A,B,C,D
    labels = ['A','B','C','D']
    colors = ['r','g','b','m']
    for i, p in enumerate(pts):
        ax.scatter(*p, color=colors[i], s=60)
        ax.text(p[0], p[1], p[2], f'  {labels[i]}{tuple(np.round(p,3))}', color=colors[i])

    # If coplanar, compute plane from first three non-collinear points
    plane_plotted = False
    if coplanar:
        # Find three non-collinear points among the four
        found = False
        for i in range(4):
            for j in range(i+1, 4):
                for k in range(j+1, 4):
                    v1 = pts[j] - pts[i]
                    v2 = pts[k] - pts[i]
                    if np.linalg.norm(np.cross(v1, v2)) > 1e-9:
                        P0 = pts[i]
                        basis1, basis2 = v1, v2
                        found = True
                        break
                if found: break
            if found: break

        if not found:
            # all points collinear -> make a plane from the line + small perp
            P0 = pts[0]
            basis1 = pts[1] - pts[0]
            # pick a perp vector
            perp = np.cross(basis1, np.array([1.0, 0.0, 0.0]))
            if np.linalg.norm(perp) < 1e-8:
                perp = np.cross(basis1, np.array([0.0, 1.0, 0.0]))
            basis2 = perp

        # make meshgrid for plane: P = P0 + s*basis1 + t*basis2
        max_len = max(np.linalg.norm(pts - pts.mean(axis=0), axis=1).max(), 1.0)
        s = np.linspace(-0.8, 0.8, 20) * max_len
        t = np.linspace(-0.8, 0.8, 20) * max_len
        S, T = np.meshgrid(s, t)
        P = P0.reshape(3,1) + np.outer(basis1, S.flatten()) + np.outer(basis2, T.flatten())
        X = P[0,:].reshape(S.shape)
        Y = P[1,:].reshape(S.shape)
        Z = P[2,:].reshape(S.shape)

        ax.plot_surface(X, Y, Z, alpha=0.35, color='cyan', linewidth=0, antialiased=True)
        plane_plotted = True

    # Nice axes limits & labels
    all_pts = pts.copy()
    if plane_plotted:
        plane_flat = np.column_stack((X.flatten(), Y.flatten(), Z.flatten()))
        all_pts = np.vstack([all_pts, plane_flat])
    mins = all_pts.min(axis=0)
    maxs = all_pts.max(axis=0)
    center = (mins + maxs)/2.0
    rng = (maxs - mins).max() / 2.0
    if rng == 0:
        rng = 1.0
    ax.set_xlim(center[0]-rng, center[0]+rng)
    ax.set_ylim(center[1]-rng, center[1]+rng)
    ax.set_zlim(center[2]-rng, center[2]+rng)

    ax.set_xlabel('X')
    ax.set_ylabel('Y')
    ax.set_zlabel('Z')
    ax.set_title('4 points in 3D — coplanarity test (augmented-rank method)')

    # Save image to ../figures
    save_dir = os.path.join("..", "figures")
    os.makedirs(save_dir, exist_ok=True)
    save_path = os.path.join(save_dir, "points_coplanarity.png")
    plt.tight_layout()
    plt.savefig(save_path, dpi=300, bbox_inches='tight')
    plt.close(fig)
    print(f"\nPlot saved as '{save_path}'")

if __name__ == "__main__":
    points_coplanarity_and_plot()

