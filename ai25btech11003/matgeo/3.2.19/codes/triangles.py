import matplotlib.pyplot as plt
import numpy as np

def draw_segment_with_label(P, Q, label, style='k-', text_offset=(0.0, 0.0)):
    """Draw segment PQ and place a rotated length label near its midpoint."""
    P = np.array(P, dtype=float)
    Q = np.array(Q, dtype=float)
    plt.plot([P[0], Q[0]], [P[1], Q[1]], style, linewidth=2)

    mid = (P + Q) / 2.0
    dx, dy = Q - P
    angle_deg = np.degrees(np.arctan2(dy, dx))
    plt.text(
        mid[0] + text_offset[0],
        mid[1] + text_offset[1],
        label,
        ha='center',
        va='center',
        rotation=angle_deg,
        rotation_mode='anchor',
        fontsize=11,
        bbox=dict(boxstyle='round,pad=0.2', fc='white', ec='none', alpha=0.8)
    )

def plot_triangle_with_lengths(a, b, c, filename, incomplete=False):
    """
    Draw triangle with sides: AB=a, AC=b, BC=c.
    If incomplete=True, depict an impossible case by showing dashed partial sides from A and B.
    """
    # Fix base AB on x-axis
    A = np.array([0.0, 0.0])
    B = np.array([a,   0.0])

    plt.figure(figsize=(4.2, 4.0))

    # Always draw AB
    draw_segment_with_label(A, B, f"{a:.1f} cm", style='k-', text_offset=(0, -0.15))

    if not incomplete:
        # Compute C using law of cosines around A
        # cos(theta) = (a^2 + b^2 - c^2) / (2ab)
        cos_theta = (a*a + b*b - c*c) / (2.0*a*b)
        cos_theta = np.clip(cos_theta, -1.0, 1.0)
        theta = np.arccos(cos_theta)
        C = np.array([b*np.cos(theta), b*np.sin(theta)])

        # Draw AC and BC
        draw_segment_with_label(A, C, f"{b:.1f} cm", style='k-')
        draw_segment_with_label(B, C, f"{c:.1f} cm", style='k-')

        # Mark points
        plt.scatter([A[0], B[0], C[0]], [A[1], B[1], C[1]], c='k', s=18)
        plt.text(A[0], A[1]-0.28, 'A', ha='center')
        plt.text(B[0], B[1]-0.28, 'B', ha='center')
        plt.text(C[0], C[1]+0.18, 'C', ha='center')

    else:
        # Depict an impossible triangle: show partial (dashed) edges toward a "would-be" C
        # Choose a visual point above AB just for indicating direction
        Cg = np.array([a*0.30, b*0.90])  # purely for illustration

        # Partial dashed from A toward Cg
        A_dash = A + 0.55*(Cg - A)
        draw_segment_with_label(A, A_dash, f"{b:.1f} cm", style='k--')

        # Partial dashed from B toward Cg
        B_dash = B + 0.55*(Cg - B)
        draw_segment_with_label(B, B_dash, f"{c:.1f} cm", style='k--')

        # Mark points
        plt.scatter([A[0], B[0], A_dash[0], B_dash[0]], [A[1], B[1], A_dash[1], B_dash[1]], c='k', s=18)
        plt.text(A[0], A[1]-0.28, 'A', ha='center')
        plt.text(B[0], B[1]-0.28, 'B', ha='center')
        plt.text((A_dash[0]+B_dash[0])/2, (A_dash[1]+B_dash[1])/2 + 0.18, 'C ?', ha='center', color='crimson')

        # Add a note for impossibility
        plt.text(a*0.5, -0.75, 'Triangle cannot close', ha='center', color='crimson', fontsize=10)

    # Final touches
    plt.axis('equal')
    plt.axis('off')
    plt.tight_layout()
    plt.savefig(filename, dpi=180, bbox_inches='tight')
    plt.close()

# Given sides
a = 5.0   # AB
b = 1.5   # AC

# Options for BC
options = [3.6, 4.1, 3.8, 3.4]

# Generate four figures with side-length labels
for i, c in enumerate(options, start=1):
    out = f"fig{i}.png"
    plot_triangle_with_lengths(a, b, c, out, incomplete=(i == 4))

