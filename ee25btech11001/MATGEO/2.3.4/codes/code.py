import numpy as np
import matplotlib.pyplot as plt
import math

if __name__ == "__main__":
    # Define two unit vectors directly
    a = np.array([1, 0])                   # along x-axis
    b = np.array([0, 1])                   # along y-axis (90° from a)

    # Scale them like in the specific case
    a_scaled = 2 * a
    b_scaled = 3 * b

    # Compute angle
    dot_product = np.dot(a, b)
    theta = math.acos(dot_product / (np.linalg.norm(a) * np.linalg.norm(b)))

    print("Angle (radians):", theta)
    print("Angle (degrees):", math.degrees(theta))

    plt.figure(figsize=(6,6))
    ax = plt.gca()
    ax.set_aspect('equal')

    # Plot vectors
    plt.quiver(0, 0, a_scaled[0], a_scaled[1], angles='xy', scale_units='xy', scale=1,
               color='r', label='2a')
    plt.quiver(0, 0, b_scaled[0], b_scaled[1], angles='xy', scale_units='xy', scale=1,
               color='b', label='3b')

    # Draw angle arc
    angle_arc = np.linspace(0, theta, 100)
    plt.plot(0.7*np.cos(angle_arc), 0.7*np.sin(angle_arc), 'k--')
    plt.text(0.9*math.cos(theta/2), 0.9*math.sin(theta/2), f"{math.degrees(theta):.0f}°")

    # Axes
    plt.axhline(0, color='black', linewidth=0.5)
    plt.axvline(0, color='black', linewidth=0.5)
    plt.xlim(-1, 5)
    plt.ylim(-1, 5)
    plt.legend()
    plt.title("Vectors and angle between them (Python only)")
    plt.grid(True)
    plt.show()
