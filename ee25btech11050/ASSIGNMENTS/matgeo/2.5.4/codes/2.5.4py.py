import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

def compute_vectors(y):
    # Define vectors
    a = np.array([2, y, 1])
    b = np.array([1, 2, 3])
    apb = a + b
    amb = a - b
    return a, b, apb, amb

def plot_vectors(y):
    a, b, apb, amb = compute_vectors(y)
    
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')

    # Plot origin
    ax.scatter(0,0,0, color='k')
    ax.text(0,0,0, "O")

    # Plot vectors
    ax.quiver(0,0,0, *a, color='r', label="a")
    ax.quiver(0,0,0, *b, color='b', label="b")
    ax.quiver(0,0,0, *apb, color='g', label="a+b")
    ax.quiver(0,0,0, *amb, color='m', label="a-b")

    # Mark vector tips with coordinates
    ax.scatter(*a, color='r')
    ax.text(*a, f"{tuple(a)}", color='r')

    ax.scatter(*b, color='b')
    ax.text(*b, f"{tuple(b)}", color='b')

    ax.scatter(*apb, color='g')
    ax.text(*apb, f"{tuple(apb)}", color='g')

    ax.scatter(*amb, color='m')
    ax.text(*amb, f"{tuple(amb)}", color='m')

    # Axis labels
    ax.set_xlabel("X")
    ax.set_ylabel("Y")
    ax.set_zlabel("Z")
    plt.title(f"Vectors for y = {y}")
    plt.legend()
    plt.show()

# Example usage
plot_vectors(3)
plot_vectors(-3)

