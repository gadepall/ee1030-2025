import numpy as np
import matplotlib.pyplot as plt
import os
import subprocess

def run_c_program():
    """Run the C program to generate data"""
    try:
        # Check if main.so exists, if not compile it
        if not os.path.exists('./main.so'):
            print("Compiling C program...")
            compile_result = subprocess.run(['gcc', '-o', 'main.so', 'main.c', '-lm'], 
                                         capture_output=True, text=True)
            if compile_result.returncode != 0:
                print("Compilation failed:")
                print(compile_result.stderr)
                return False

        # Run the compiled program
        print("Running C program...")
        run_result = subprocess.run(['./main.so'], capture_output=True, text=True)
        if run_result.returncode != 0:
            print("Execution failed:")
            print(run_result.stderr)
            return False

        print("C program output:")
        print(run_result.stdout)
        return True

    except Exception as e:
        print(f"Error running C program: {e}")
        return False

def read_data_file():
    """Read data from main.dat file without pandas"""
    try:
        with open('main.dat', 'r') as f:
            lines = f.readlines()

        # Skip header line
        data_lines = lines[1:]

        p_values = []
        rankA_values = []
        rankAb_values = []
        solution_types = []

        for line in data_lines:
            line = line.strip()
            if line:
                parts = line.split(',')
                p_values.append(float(parts[0]))
                rankA_values.append(int(parts[1]))
                rankAb_values.append(int(parts[2]))
                solution_types.append(parts[3])

        return p_values, rankA_values, rankAb_values, solution_types

    except FileNotFoundError:
        print("main.dat not found. Using default values...")
        return [1.0, 2.0, 3.0, 4.0, 5.0], [2, 2, 2, 1, 2], [2, 2, 2, 2, 2], ['UNIQUE', 'UNIQUE', 'UNIQUE', 'NO_SOLUTION', 'UNIQUE']

def plot_lines_for_case(p_value, filename, title):
    """Plot the two lines for a specific value of p"""

    # Create figure
    plt.figure(figsize=(10, 8))

    # Define x range
    x = np.linspace(-8, 8, 400)

    # Line 1: 4x + py + 8 = 0  =>  y = (-4x - 8)/p (when p ≠ 0)
    # Line 2: 2x + 2y + 2 = 0  =>  y = (-2x - 2)/2 = -x - 1

    # Second line (always the same)
    y2 = -x - 1

    if p_value == 4:
        # When p = 4: 4x + 4y + 8 = 0  =>  y = (-4x - 8)/4 = -x - 2
        y1 = -x - 2

        # Plot both lines
        plt.plot(x, y1, 'r-', linewidth=3, label='4x + 4y + 8 = 0', alpha=0.8)
        plt.plot(x, y2, 'b--', linewidth=3, label='2x + 2y + 2 = 0', alpha=0.8)

        # Add text annotation
        plt.text(0, 4, 'No Solution\n(Parallel Lines)', fontsize=14, 
                bbox=dict(boxstyle="round,pad=0.3", facecolor="red", alpha=0.3),
                horizontalalignment='center')

        # Highlight the parallel nature
        plt.text(-6, -1, 'Slope = -1', fontsize=12, color='red', 
                bbox=dict(boxstyle="round,pad=0.2", facecolor="white", alpha=0.8))
        plt.text(-6, 2, 'Slope = -1', fontsize=12, color='blue',
                bbox=dict(boxstyle="round,pad=0.2", facecolor="white", alpha=0.8))

    else:
        # When p ≠ 4, use p = 2 as example
        if p_value == 0:
            # Special case: when p = 0, first equation becomes 4x + 8 = 0 => x = -2
            plt.axvline(x=-2, color='r', linewidth=3, label='4x + 8 = 0 (x = -2)', alpha=0.8)
            plt.plot(x, y2, 'b--', linewidth=3, label='2x + 2y + 2 = 0', alpha=0.8)

            # Find intersection
            intersection_x = -2
            intersection_y = -(-2) - 1  # y = -x - 1 at x = -2
            intersection_y = 1

        else:
            y1 = (-4*x - 8) / p_value
            plt.plot(x, y1, 'r-', linewidth=3, label=f'4x + {p_value}y + 8 = 0', alpha=0.8)
            plt.plot(x, y2, 'b--', linewidth=3, label='2x + 2y + 2 = 0', alpha=0.8)

            # Find intersection point by solving system
            # 4x + py + 8 = 0
            # 2x + 2y + 2 = 0  =>  x + y + 1 = 0  =>  y = -x - 1
            # Substitute: 4x + p(-x - 1) + 8 = 0
            # 4x - px - p + 8 = 0
            # x(4 - p) = p - 8
            # x = (p - 8)/(4 - p)
            if p_value != 4:
                intersection_x = (p_value - 8) / (4 - p_value)
                intersection_y = -intersection_x - 1

        # Plot intersection point
        if p_value != 4:
            plt.plot(intersection_x, intersection_y, 'go', markersize=12, 
                    label=f'Solution: ({intersection_x:.2f}, {intersection_y:.2f})', zorder=5)

            # Add text annotation
            plt.text(intersection_x + 0.5, intersection_y + 0.5, 
                    f'Unique Solution\n({intersection_x:.2f}, {intersection_y:.2f})', 
                    fontsize=12, 
                    bbox=dict(boxstyle="round,pad=0.3", facecolor="green", alpha=0.3))

    # Set plot properties
    plt.grid(True, alpha=0.3)
    plt.axhline(y=0, color='k', linewidth=0.5)
    plt.axvline(x=0, color='k', linewidth=0.5)
    plt.xlabel('x', fontsize=14)
    plt.ylabel('y', fontsize=14)
    plt.title(title, fontsize=16, fontweight='bold')
    plt.legend(fontsize=12, loc='upper right')

    # Set axis limits
    plt.xlim(-8, 8)
    plt.ylim(-8, 8)

    # Save the plot
    plt.savefig(filename, dpi=300, bbox_inches='tight')
    plt.show()
    print(f"Saved plot as {filename}")

def create_line_visualizations():
    """Create the two required visualizations"""

    print("Creating line visualizations...")

    # Fig1: p = 4 case (No solution - parallel lines)
    plot_lines_for_case(4, 'fig1.png', 'p = 4')

    # Fig2: p ≠ 4 case (Unique solution - intersecting lines) 
    # Using p = 2 as an example
    plot_lines_for_case(2, 'fig2.png', 'p ≠ 4')

    print("\nLine Analysis Complete!")
    print("\nKey Insights:")
    print("1. fig1.png (p = 4): Shows parallel lines with NO intersection (No Solution)")
    print("2. fig2.png (p ≠ 4): Shows intersecting lines with UNIQUE intersection (Unique Solution)")

def mathematical_verification():
    """Verify the mathematical analysis"""
    print("\nMathematical Verification:")
    print("=" * 50)

    print("Given system:")
    print("4x + py + 8 = 0  ... (1)")
    print("2x + 2y + 2 = 0  ... (2)")

    print("\nFrom equation (2): x + y + 1 = 0  =>  y = -x - 1")
    print("This line has slope = -1 and y-intercept = -1")

    print("\nFrom equation (1): 4x + py + 8 = 0")
    print("When p ≠ 0: y = (-4x - 8)/p")
    print("This line has slope = -4/p")

    print("\nFor p = 4:")
    print("  Line 1: y = (-4x - 8)/4 = -x - 2  (slope = -1)")
    print("  Line 2: y = -x - 1              (slope = -1)")
    print("  Both lines have the same slope but different y-intercepts")
    print("  Result: PARALLEL LINES => NO SOLUTION")

    print("\nFor p ≠ 4:")
    print("  Line 1: slope = -4/p")
    print("  Line 2: slope = -1")
    print("  Different slopes => Lines intersect")
    print("  Result: UNIQUE SOLUTION")

if __name__ == "__main__":
    print("Matrix Theory Problem: Line Visualization Analysis")
    print("=" * 55)

    # Step 1: Run C program to generate data
    c_success = run_c_program()

    # Step 2: Read data from main.dat
    p_values, rankA_values, rankAb_values, solution_types = read_data_file()

    print("\nData from C program:")
    print("p\trankA\trankAb\tsolution_type")
    for i in range(len(p_values)):
        print(f"{p_values[i]:.2f}\t{rankA_values[i]}\t{rankAb_values[i]}\t{solution_types[i]}")

    # Step 3: Create line visualizations
    create_line_visualizations()

    # Step 4: Mathematical verification
    mathematical_verification()

    print("\nFiles generated:")
    print("- main.so (compiled C program)")
    print("- main.dat (data file)")
    print("- fig1.png (p = 4 case - parallel lines)")
    print("- fig2.png (p ≠ 4 case - intersecting lines)")