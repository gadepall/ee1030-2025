import numpy as np
import matplotlib.pyplot as plt

def plane_equation(point):
    """Returns d for the plane x + y + z = d through point (a, b, c)."""
    a, b, c = point
    return a + b + c

def plot_planes(point):
    # Normal vector
    n = np.array([1, 1, 1])
    
    # Given plane: x + y + z = 2
    d1 = 2
    
    # Required plane: x + y + z = a+b+c
    d2 = plane_equation(point)
    
    # Meshgrid for plotting
    x = np.linspace(-5, 5, 20)
    y = np.linspace(-5, 5, 20)
    X, Y = np.meshgrid(x, y)
    
    # z for each plane
    Z1 = (d1 - X - Y) / n[2]
    Z2 = (d2 - X - Y) / n[2]
    
    # Plot
    fig = plt.figure(figsize=(8, 6))
    ax = fig.add_subplot(111, projection='3d')
    
    # Given plane
    ax.plot_surface(X, Y, Z1, alpha=0.4, color='cyan', label="x+y+z=2")
    ax.text(2, 2, (d1 - 2 - 2), "x+y+z=2", color='blue', fontsize=10)
    
    # Required plane
    ax.plot_surface(X, Y, Z2, alpha=0.4, color='orange', label=f"x+y+z={d2}")
    ax.text(-3, -3, (d2 - (-3) - (-3)), f"x+y+z={d2}", color='brown', fontsize=10)
    
    # Mark the given point with legend
    ax.scatter(point[0], point[1], point[2], color='red', s=50, label=f"Point {point}")
    
    # Normal vector arrow
    origin = np.array([0, 0, 0])
    ax.quiver(*origin, *n, length=2, color="green")
    
    # Axes labels
    ax.set_xlabel("X-axis")
    ax.set_ylabel("Y-axis")
    ax.set_zlabel("Z-axis")
    ax.set_title("Parallel Planes")
    
    # Show legend
    ax.legend()
    plt.savefig("/home/arsh-dhoke/ee1030-2025/ee25btech11010/matgeo/4.5.12/figs/q7.png")
    plt.show()

# Example usage
point = (2, 1, -3)  
plot_planes(point)
