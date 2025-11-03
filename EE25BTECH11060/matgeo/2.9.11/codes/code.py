import numpy as np
import matplotlib.pyplot as plt
from matplotlib.patches import Arc

def plot_vectors_with_angle(a, b):
    a = np.array(a)
    b = np.array(b)

    # Calculate angle (in radians and degrees)
    dot_product = np.dot(a, b)
    norm_a = np.linalg.norm(a)
    norm_b = np.linalg.norm(b)
    cos_theta = dot_product / (norm_a * norm_b)
    theta_rad = np.arccos(np.clip(cos_theta, -1.0, 1.0))
    theta_deg = np.degrees(theta_rad)

    # Setup plot
    fig, ax = plt.subplots()
    ax.set_aspect('equal')
    ax.grid(True)

    # Calculate plot limits
    max_val = max(np.linalg.norm(a), np.linalg.norm(b)) + 1
    ax.set_xlim(-1, max_val)
    ax.set_ylim(-1, max_val)

    # Plot vectors
    origin = [0, 0]
    ax.quiver(*origin, *a, angles='xy', scale_units='xy', scale=1, color='r', label='a')
    ax.quiver(*origin, *b, angles='xy', scale_units='xy', scale=1, color='b', label='b')

    # Draw angle arc
    arc_radius = 0.5
    arc = Arc(origin, arc_radius*2, arc_radius*2, angle=0,
              theta1=0, theta2=theta_deg, color='green')
    ax.add_patch(arc)

    # Annotate angle
    mid_angle = theta_rad / 2
    label_radius = arc_radius * 1.4
    x_text = label_radius * np.cos(mid_angle)
    y_text = label_radius * np.sin(mid_angle)
    ax.text(x_text, y_text, f'θ = {theta_deg:.1f}°', fontsize=12, color='green')
    

    # Labels and title
    ax.legend()
    ax.set_xlabel('X-axis')
    ax.set_ylabel('Y-axis')
    ax.set_title('Angle Between Vectors a and b')
    plt.show()

# Example usage with any two 2D vectors:
# Replace these with your own vectors
a = [3, 2]
b = [2, 4]

plot_vectors_with_angle(a, b)
