import numpy as np
import matplotlib.pyplot as plt

# All 4 cases of Problem 2.2.25
cases = [
    (np.array([3, 2, 6]), np.array([1, 2, 2]), "a"),
    (np.array([1, -1, -2]), np.array([3, -5, -4]), "b"),
    (np.array([2, 5, -3]), np.array([-1, 8, -4]), "c"),
    (np.array([2, 5, 1]), np.array([4, 1, 8]), "d")
]

# Print table header
print("Problem 2.2.25 - Angles between lines")
print("-------------------------------------")

for d1, d2, label in cases:
    # Compute angle using numpy
    cos_theta = (d1 @ d2) / (np.linalg.norm(d1) * np.linalg.norm(d2))
    cos_theta = np.clip(cos_theta, -1.0, 1.0)  # numerical safety
    theta = np.arccos(cos_theta)
    theta_deg = np.degrees(theta)

    # Print result in terminal
    print(f"Case ({label}): θ = {theta_deg:.2f}°")

    # Normalize for visualization
    d1 = d1 / np.linalg.norm(d1)
    d2 = d2 / np.linalg.norm(d2)

    # Generate shorter line segments
    t = np.linspace(-2, 2, 100)
    line1 = np.outer(t, d1)
    line2 = np.outer(t, d2)

    # Orthonormal basis for arc
    u1 = d1
    u2 = d2 - (d2 @ u1) * u1
    if np.linalg.norm(u2) > 1e-8:
        u2 /= np.linalg.norm(u2)

    # Arc between d1 and d2
    arc_t = np.linspace(0, theta, 50)
    arc_points = np.array([np.cos(a)*u1 + np.sin(a)*u2 for a in arc_t]) * 1.2

    # Plot
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')
    ax.plot(line1[:,0], line1[:,1], line1[:,2], color="blue", label="Line 1", lw=2)
    ax.plot(line2[:,0], line2[:,1], line2[:,2], color="red", label="Line 2", lw=2)
    ax.plot(arc_points[:,0], arc_points[:,1], arc_points[:,2],
            color="green", lw=3, ls="--")

    # Label θ
    mid = arc_points[len(arc_points)//2]
    ax.text(mid[0], mid[1], mid[2], r"$\theta$", fontsize=14, color="green")

    # Origin
    ax.scatter(0, 0, 0, color="black", s=40)

    # Title
    ax.set_title(f"Problem 2.2.25 ({label}) : θ = {theta_deg:.2f}°")
    ax.legend()

    # Adjust camera view
    ax.view_init(elev=25, azim=60)

    # Save and show
    plt.savefig(f"/sdcard/ee1030-2025/ai25btech11032/Matgeo/2.2.25/figs/newfigure_{label}_python.png", dpi=300)
    plt.show()
