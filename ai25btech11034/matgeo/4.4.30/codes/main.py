import ctypes
import numpy as np
import matplotlib.pyplot as plt
import os

# Load C library
lib = ctypes.CDLL("./function.so")

# Define argument and return types
lib.are_coplanar.argtypes = [ctypes.c_double * 12]  # 4*3 = 12 doubles
lib.are_coplanar.restype = ctypes.c_int

def check_coplanarity(points):
    """Call C function to check coplanarity"""
    flat_points = (ctypes.c_double * 12)(*np.array(points).flatten())
    return lib.are_coplanar(flat_points)

def main():
    # Input 4 points
    points = []
    for i in range(4):
        coords = input(f"Enter point {i+1} (x y z): ").split()
        if len(coords) != 3:
            raise ValueError("Each point must have 3 coordinates")
        points.append([float(c) for c in coords])

    # Check coplanarity using C
    result = check_coplanarity(points)
    if result:
        print("✅ The 4 points are coplanar")
    else:
        print("❌ The 4 points are NOT coplanar")

    # Plot points
    pts = np.array(points)
    fig = plt.figure()
    ax = fig.add_subplot(111, projection="3d")
    labels = ["A", "B", "C", "D"]
    for i, p in enumerate(pts):
        ax.scatter(*p, s=60)
        ax.text(*p, f" {labels[i]}")

    # If coplanar, plot plane from first 3 points
    if result:
        p1, p2, p3 = pts[0], pts[1], pts[2]
        v1, v2 = p2 - p1, p3 - p1
        u, v = np.meshgrid(np.linspace(-1, 1, 10), np.linspace(-1, 1, 10))
        plane = p1 + u[..., None]*v1 + v[..., None]*v2
        ax.plot_surface(plane[...,0], plane[...,1], plane[...,2], alpha=0.3, color="cyan")

    ax.set_xlabel("X")
    ax.set_ylabel("Y")
    ax.set_zlabel("Z")

    # Save image
    os.makedirs("../figures", exist_ok=True)
    plt.savefig("../figures/points_plane.png", dpi=300)
    print("Plot saved as '../figures/points_plane.png'")

if __name__ == "__main__":
    main()

