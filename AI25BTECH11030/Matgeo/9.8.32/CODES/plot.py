import numpy as np
import matplotlib.pyplot as plt

def solve_circle_parabola_problem():
    """Find the center of the circle passing through (0,1) and touching y = x² at (2,4)"""
    
    # Given points
    P = np.array([0, 1])
    Q = np.array([2, 4])
    
    # Set up system of equations
    # Constraint 1: Equal distances from center to P and Q
    # 4cx + 6cy = 19
    # Constraint 2: Center-to-Q line is normal to parabola at Q  
    # cx + 4cy = 18
    
    A = np.array([[4, 6], [1, 4]])
    b = np.array([19, 18])
    
    # Solve for center
    center = np.linalg.solve(A, b)
    radius = np.linalg.norm(P - center)
    
    return center, radius

def plot_solution():
    """Plot the parabola, circle, and key points with complete circle visible"""
    center, radius = solve_circle_parabola_problem()
    
    fig, ax = plt.subplots(1, 1, figsize=(12, 10))
    
    # Calculate proper plot limits to show entire circle
    x_min = center[0] - radius - 1
    x_max = max(center[0] + radius + 1, 6)  # Ensure parabola portion is visible
    y_min = center[1] - radius - 1
    y_max = max(center[1] + radius + 1, 15)  # Show some parabola
    
    # Plot parabola y = x² (extended range)
    x_parabola = np.linspace(x_min, x_max, 1000)
    y_parabola = x_parabola**2
    # Only plot parabola where y is in our range
    mask = (y_parabola >= y_min) & (y_parabola <= y_max)
    ax.plot(x_parabola[mask], y_parabola[mask], 'b-', linewidth=2, label='Parabola: y = x²')
    
    # Plot complete circle
    theta = np.linspace(0, 2*np.pi, 1000)
    x_circle = center[0] + radius * np.cos(theta)
    y_circle = center[1] + radius * np.sin(theta)
    ax.plot(x_circle, y_circle, 'r-', linewidth=2, label=f'Circle (r = {radius:.2f})')
    
    # Mark important points
    ax.plot(0, 1, 'go', markersize=10, label='P(0,1) - Point on circle', zorder=5)
    ax.plot(2, 4, 'mo', markersize=10, label='Q(2,4) - Tangent point', zorder=5)
    ax.plot(center[0], center[1], 'ro', markersize=10, 
            label=f'Center({center[0]:.1f}, {center[1]:.1f})', zorder=5)
    
    # Draw normal line from center to Q
    ax.plot([center[0], 2], [center[1], 4], 'k--', linewidth=2, 
            alpha=0.8, label='Normal to parabola')
    
    # Draw tangent line at Q (y = 4x - 4)
    x_tangent = np.linspace(0.5, 3.5, 100)
    y_tangent = 4 * x_tangent - 4
    ax.plot(x_tangent, y_tangent, 'g--', linewidth=2, 
            alpha=0.8, label='Tangent at Q: y = 4x - 4')
    
    # Set plot limits to show complete circle
    ax.set_xlim(x_min, x_max)
    ax.set_ylim(y_min, y_max)
    
    # Enhance plot appearance
    ax.grid(True, alpha=0.4, linestyle='-', linewidth=0.5)
    ax.set_xlabel('x', fontsize=14, fontweight='bold')
    ax.set_ylabel('y', fontsize=14, fontweight='bold')
    ax.set_title('Circle Passing Through (0,1) and Tangent to y=x² at (2,4)', 
                fontsize=16, fontweight='bold', pad=20)
    
    # Add axes lines through origin
    ax.axhline(y=0, color='black', linewidth=0.8, alpha=0.3)
    ax.axvline(x=0, color='black', linewidth=0.8, alpha=0.3)
    
    # Legend with better positioning
    ax.legend(loc='upper left', fontsize=11, framealpha=0.9)
    
    # Make axes equal to avoid distortion
    ax.set_aspect('equal', adjustable='box')
    
    # Add some annotations
    ax.annotate('Complete Circle\nVisible', 
                xy=(center[0], center[1]-radius+0.5), 
                fontsize=10, ha='center', 
                bbox=dict(boxstyle="round,pad=0.3", facecolor="yellow", alpha=0.7))
    
    plt.tight_layout()
    plt.savefig("fig1.png")
    plt.show()
    
    return fig, ax

if __name__ == "__main__":
    center, radius = solve_circle_parabola_problem()
    
    print(f"Center: ({center[0]:.6f}, {center[1]:.6f})")
    print(f"Center (exact): (-16/5, 53/10)")
    print(f"Radius: {radius:.6f}")
    
    plot_solution()
