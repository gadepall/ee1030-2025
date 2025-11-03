import numpy as np
import matplotlib.pyplot as plt
import ctypes
import os

def load_shared_library():
    """Load the shared library main.so"""
    try:
        # Load the shared library
        lib = ctypes.CDLL('./main.so')
        print("Successfully loaded main.so")
        return lib
    except Exception as e:
        print(f"Error loading main.so: {e}")
        return None

def read_points_from_dat():
    """Read point coordinates from main.dat file"""
    points = {}
    try:
        with open('main.dat', 'r') as f:
            for line in f:
                line = line.strip()
                if line.startswith('#') or not line:
                    continue
                parts = line.split()
                if len(parts) == 3:
                    point_name = parts[0]
                    x = float(parts[1])
                    y = float(parts[2])
                    points[point_name] = (x, y)
        print(f"Successfully read points from main.dat: {points}")
        return points
    except Exception as e:
        print(f"Error reading main.dat: {e}")
        return {}

def create_visualization(points):
    """Create the visualization with specified requirements"""
    # Create figure and axis
    fig, ax = plt.subplots(1, 1, figsize=(8, 8))

    # Remove title as requested
    # ax.set_title("")  # No title

    # Set up the coordinate system
    ax.set_xlim(-0.5, 1.5)
    ax.set_ylim(-0.5, 1.5)
    ax.set_aspect('equal')
    ax.grid(True, alpha=0.3)

    # Add x and y axis
    ax.axhline(y=0, color='k', linewidth=0.5)
    ax.axvline(x=0, color='k', linewidth=0.5)
    ax.set_xlabel('x')
    ax.set_ylabel('y')

    # Extract coordinates
    A = points.get('A', (1, 0))
    B = points.get('B', (0, 1))
    M = points.get('M', (0.5, 0.5))
    P = points.get('P', (0, 0))
    Q = points.get('Q', (1, 1))

    # Plot points
    ax.plot(A[0], A[1], 'ro', markersize=8)
    ax.plot(B[0], B[1], 'ro', markersize=8)
    ax.plot(M[0], M[1], 'bo', markersize=8)
    ax.plot(P[0], P[1], 'go', markersize=8)
    ax.plot(Q[0], Q[1], 'go', markersize=8)

    # Label points
    ax.text(A[0]+0.05, A[1]+0.05, 'A(1,0)', fontsize=12, fontweight='bold')
    ax.text(B[0]+0.05, B[1]+0.05, 'B(0,1)', fontsize=12, fontweight='bold')
    ax.text(M[0]+0.07, M[1]-0.05, 'M(0.5,0.5)', fontsize=12, fontweight='bold')
    ax.text(P[0]-0.05, P[1]-0.05, 'P(0,0)', fontsize=12, fontweight='bold')
    ax.text(Q[0]+0.05, Q[1]+0.05, 'Q(1,1)', fontsize=12, fontweight='bold')

    # Draw line segment AB as solid line
    ax.plot([A[0], B[0]], [A[1], B[1]], 'r-', linewidth=2, label='Line segment AB')

    # Draw line PQ as dotted line
    ax.plot([P[0], Q[0]], [P[1], Q[1]], 'g--', linewidth=2, label='Line PQ')

    # Add legend
    ax.legend(loc='upper right')

    # Save the figure as fig1.png
    plt.savefig('fig1.png', dpi=300, bbox_inches='tight')
    print("Visualization saved as fig1.png")

    # Show the plot
    plt.show()

def main():
    """Main function"""
    print("Python visualization program started...")

    # Load shared library
    lib = load_shared_library()

    # Read points from main.dat
    points = read_points_from_dat()

    if not points:
        print("Using default points since main.dat could not be read")
        points = {
            'A': (1.0, 0.0),
            'B': (0.0, 1.0),
            'M': (0.5, 0.5),
            'P': (0.0, 0.0),
            'Q': (1.0, 1.0)
        }

    # Create visualization
    create_visualization(points)

    print("Program completed successfully!")

if __name__ == "__main__":
    main()
