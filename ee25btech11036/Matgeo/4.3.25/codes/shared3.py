import numpy as np
import math
import matplotlib.pyplot as plt
from ctypes import CDLL, c_double, POINTER, byref
from math import gcd

# Load the C library
lib = CDLL('./libratio.so')

lib.yz_plane_ratio.argtypes = (c_double, c_double, c_double,
                              c_double, c_double, c_double,
                              POINTER(c_double), POINTER(c_double))
lib.yz_plane_ratio.restype = None

# Points A and B
A = (-2.0, 4.0, 7.0)
B = (3.0, -5.0, 8.0)

t = c_double()
omt = c_double()

# Call the C function to get t and 1-t
lib.yz_plane_ratio(A[0], A[1], A[2],
                  B[0], B[1], B[2],
                  byref(t), byref(omt))

if math.isnan(t.value):
    print("No finite intersection with YZ-plane (x=0)")
else:
    print(f"λ (t) = {t.value:.4f}")
    print(f"1 - λ = {omt.value:.4f}")

    # Correct ratio conversion from floats to simplest integer ratio
    def ratio_to_ints(t1, t2):
        precision = 10**6  # High precision to convert float to int safely
        a = int(round(t1 * precision))
        b = int(round(t2 * precision))
        g = gcd(a, b)
        return a // g, b // g

    a, b = ratio_to_ints(t.value, omt.value)
    print(f"Ratio AP:PB = {a}:{b}")

    # Calculate intersection point P
    P = tuple((1 - t.value)*A[i] + t.value*B[i] for i in range(3))
    print(f"Intersection point P on YZ-plane: ({P[0]:.2f}, {P[1]:.2f}, {P[2]:.2f})")

    # Calculate lengths AP and PB
    A_np = np.array(A)
    B_np = np.array(B)
    P_np = np.array(P)

    AP_len = np.linalg.norm(P_np - A_np)
    PB_len = np.linalg.norm(B_np - P_np)
    print(f"Length AP = {AP_len:.4f}")
    print(f"Length PB = {PB_len:.4f}")
    print(f"Length ratio AP:PB ≈ {AP_len/PB_len:.4f} (should be close to {a/b:.4f})")

    # Generate points for line AB (for plotting)
    points = np.array([np.linspace(A[i], B[i], 100) for i in range(3)])

    # Plot setup
    fig = plt.figure(figsize=(10, 8))
    ax = fig.add_subplot(111, projection='3d')

    # Plot line AB
    ax.plot(points[0], points[1], points[2], label='Line AB', color='blue')

    # Plot points A, B, P
    ax.scatter(*A, color='green', s=80, label='A')
    ax.scatter(*B, color='red', s=80, label='B')
    ax.scatter(*P, color='black', s=100, label='P (Intersection)')

    # Annotate points with coordinates
    def annotate_point(ax, point, label, color):
        ax.text(point[0], point[1], point[2] + 0.3,
                f"{label}\n({point[0]:.2f}, {point[1]:.2f}, {point[2]:.2f})",
                color=color, fontsize=10, ha='center')

    annotate_point(ax, A, 'A', 'green')
    annotate_point(ax, B, 'B', 'red')
    annotate_point(ax, P, 'P', 'black')

    # Plot YZ-plane (x=0)
    y = np.linspace(-6, 6, 30)
    z = np.linspace(5, 10, 30)
    Y, Z = np.meshgrid(y, z)
    X = np.zeros_like(Y)
    ax.plot_surface(X, Y, Z, color='cyan', alpha=0.3)

    # Add text box with ratio and lengths
    ratio_text = (
        f"λ = {t.value:.2f}\n"
        f"Ratio AP:PB = {a}:{b}\n"
        f"Length AP = {AP_len:.2f}\n"
        f"Length PB = {PB_len:.2f}"
    )
    ax.text2D(0.05, 0.95, ratio_text, transform=ax.transAxes,
              fontsize=12, bbox=dict(facecolor='white', alpha=0.7))

    # Equal aspect ratio (very important!)
    def set_axes_equal(ax):
        '''Set 3D plot axes to equal scale.'''
        limits = np.array([
            ax.get_xlim3d(),
            ax.get_ylim3d(),
            ax.get_zlim3d(),
        ])
        spans = limits[:,1] - limits[:,0]
        centers = np.mean(limits, axis=1)
        radius = 0.5 * max(spans)
        ax.set_xlim3d(centers[0] - radius, centers[0] + radius)
        ax.set_ylim3d(centers[1] - radius, centers[1] + radius)
        ax.set_zlim3d(centers[2] - radius, centers[2] + radius)

    set_axes_equal(ax)

    ax.set_xlabel('X-axis')
    ax.set_ylabel('Y-axis')
    ax.set_zlabel('Z-axis')
    ax.set_title('Intersection of line AB with YZ-plane (x=0)')
    ax.legend()
    ax.grid(True)
    ax.view_init(elev=20, azim=30)

    plt.tight_layout()
    plt.show()

