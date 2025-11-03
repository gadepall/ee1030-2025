import ctypes
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import os

# Load the shared library
try:
    lib = ctypes.CDLL('./main.so')
    print("Successfully loaded main.so")
except Exception as e:
    print(f"Error loading main.so: {e}")
    print("Make sure to compile the C code first with:")
    print("gcc -shared -fPIC -o main.so main.c -lm")

# Define function signatures
lib.find_minimum_value.restype = ctypes.c_double
lib.generate_parabola_data.restype = None

# Call the C function to find minimum value
min_value = lib.find_minimum_value()
print(f"Minimum value from C library: {min_value}")

# Generate data using C function
lib.generate_parabola_data()
print("Data generated using C library")

# Read the data from main.dat
try:
    data = pd.read_csv('main.dat')
    x_vals = data['x'].values
    y_vals = data['y'].values

    # Create the plot
    plt.figure(figsize=(10, 8))

    # Plot the parabola
    plt.plot(x_vals, y_vals, 'b-', linewidth=2, label=r'$y = x^2 - 2x + 4$')

    # Mark the minimum point
    plt.plot(1, 3, 'ro', markersize=10, label='Minimum point (1, 3)')

    # Add horizontal line at y = 3
    plt.axhline(y=3, color='r', linestyle='--', alpha=0.7, label='y = 3')

    # Add vertical line at x = 1
    plt.axvline(x=1, color='g', linestyle='--', alpha=0.7, label='x = 1')

    # Formatting
    plt.grid(True, alpha=0.3)
    plt.xlabel('x', fontsize=14)
    plt.ylabel('y', fontsize=14)
    plt.title('Parabola: y = x² - 2x + 4\nMinimum Value Analysis', fontsize=16)
    plt.legend(fontsize=12)

    # Set axis limits for better view
    plt.xlim(-2.5, 4.5)
    plt.ylim(2, 10)

    # Add text annotation
    plt.annotate(f'Minimum: ({1}, {min_value})', 
                xy=(1, 3), xytext=(2.5, 4),
                arrowprops=dict(arrowstyle='->', color='black'),
                fontsize=12, ha='center')

    # Save the figure
    plt.tight_layout()
    plt.savefig('fig1.png', dpi=300, bbox_inches='tight')
    print("Plot saved as fig1.png")

    plt.show()

except Exception as e:
    print(f"Error reading data or creating plot: {e}")

    # Alternative: create plot with numpy if data reading fails
    x = np.linspace(-2, 4, 100)
    y = x**2 - 2*x + 4

    plt.figure(figsize=(10, 8))
    plt.plot(x, y, 'b-', linewidth=2, label=r'$y = x^2 - 2x + 4$')
    plt.plot(1, 3, 'ro', markersize=10, label='Minimum point (1, 3)')
    plt.axhline(y=3, color='r', linestyle='--', alpha=0.7, label='y = 3')
    plt.axvline(x=1, color='g', linestyle='--', alpha=0.7, label='x = 1')

    plt.grid(True, alpha=0.3)
    plt.xlabel('x', fontsize=14)
    plt.ylabel('y', fontsize=14)
    plt.title('Parabola: y = x² - 2x + 4', fontsize=16)
    plt.legend(fontsize=12)
    plt.xlim(-2.5, 4.5)
    plt.ylim(2, 10)

    plt.annotate(f'Minimum: (1, 3)', 
                xy=(1, 3), xytext=(2.5, 4),
                arrowprops=dict(arrowstyle='->', color='black'),
                fontsize=12, ha='center')

    plt.tight_layout()
    plt.savefig('fig1.png', dpi=300, bbox_inches='tight')
    print("Alternative plot saved as fig1.png")
