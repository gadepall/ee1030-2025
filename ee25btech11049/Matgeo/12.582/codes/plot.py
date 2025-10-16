import numpy as np
import matplotlib.pyplot as plt
from matplotlib.patches import Arc

def rotate_point(point, angle_degrees):
    """
    Rotates a 2D point anti-clockwise around the origin.

    Args:
        point (tuple or list): The (x, y) coordinates of the point to rotate.
        angle_degrees (float): The angle of rotation in degrees.

    Returns:
        numpy.ndarray: The new (x, y) coordinates after rotation.
    """
    # Convert the angle from degrees to radians for trigonometric functions
    angle_radians = np.radians(angle_degrees)

    # Define the initial point P as a column vector (2x1 matrix)
    p_vector = np.array([[point[0]], [point[1]]])

    # Create the 2D anti-clockwise rotation matrix
    cos_theta = np.cos(angle_radians)
    sin_theta = np.sin(angle_radians)
    rotation_matrix = np.array([
        [cos_theta, -sin_theta],
        [sin_theta,  cos_theta]
    ])

    # Perform the matrix multiplication: Q = R * P
    q_vector = np.dot(rotation_matrix, p_vector)

    return q_vector.flatten() # Flatten to a 1D array for easier reading

def plot_rotation(p, q, angle_degrees):
    """
    Generates a plot to visualize the rotation of point P to Q.
    """
    fig, ax = plt.subplots(figsize=(8, 8))

    # Plot origin
    ax.plot(0, 0, 'ko', markersize=10, label='Origin (O)')

    # Create formatted strings for the labels to ensure clean output
    p_label = f'({p[0]:.2f}, {p[1]:.2f})'
    q_label = f'({q[0]:.2f}, {q[1]:.2f})'

    # Plot vectors and points
    # Vector OP
    ax.arrow(0, 0, p[0], p[1], head_width=0.5, head_length=0.7, fc='blue', ec='blue', length_includes_head=True)
    ax.plot(p[0], p[1], 'bo', markersize=8, label=f'Point P {p_label}')
    ax.text(p[0] + 0.5, p[1] + 0.5, f'P {p_label}', fontsize=12, color='blue')

    # Vector OQ
    ax.arrow(0, 0, q[0], q[1], head_width=0.5, head_length=0.7, fc='red', ec='red', length_includes_head=True)
    ax.plot(q[0], q[1], 'ro', markersize=8, label=f'Point Q {q_label}')
    ax.text(q[0] + 0.5, q[1] + 0.5, f'Q {q_label}', fontsize=12, color='red')

    # Add the rotation arc
    radius = np.linalg.norm(p)
    # Angle for arc starts from the angle of vector P
    angle_p_rad = np.arctan2(p[1], p[0])
    angle_p_deg = np.degrees(angle_p_rad)
    arc = Arc((0, 0), radius*0.5, radius*0.5, angle=0,
              theta1=angle_p_deg, theta2=angle_p_deg + angle_degrees,
              color='green', linewidth=2, linestyle='--')
    ax.add_patch(arc)
    # Add theta label near the arc
    theta_label_rad = np.radians(angle_p_deg + angle_degrees / 2)
    ax.text(radius*0.3 * np.cos(theta_label_rad), radius*0.3 * np.sin(theta_label_rad),
            f'θ={angle_degrees}°', fontsize=12, color='green')


    # Set up the plot
    ax.axhline(0, color='black',linewidth=0.5)
    ax.axvline(0, color='black',linewidth=0.5)
    ax.grid(True, which='both', linestyle='--', linewidth=0.5)
    ax.set_aspect('equal', adjustable='box')
    ax.set_title('2D Vector Rotation', fontsize=16)
    ax.set_xlabel('X-axis', fontsize=12)
    ax.set_ylabel('Y-axis', fontsize=12)

    # Set axis limits to give some space around the vectors
    max_val = max(np.abs(p).max(), np.abs(q).max()) * 1.2
    ax.set_xlim(-5, max_val)
    ax.set_ylim(-5, max_val)

    ax.legend()
    plt.show()


# --- Main execution ---
if __name__ == "__main__":
    # Initial point P
    P = np.array([20, 10])

    # Angle of rotation in degrees
    theta = 30

    # Calculate the new position Q
    Q = rotate_point(P, theta)

    print(f"Original point P: {tuple(P)}")
    print(f"Rotation angle: {theta}°")
    print(f"New point Q (x, y): ({Q[0]:.2f}, {Q[1]:.2f})")

    # Visualize the rotation
    plot_rotation(P, Q, theta)


