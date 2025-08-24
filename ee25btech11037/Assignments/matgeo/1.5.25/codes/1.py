import ctypes
import os
import matplotlib.pyplot as plt

# Define the path to the shared object file.
so_file_path = "1.so"

lib = ctypes.CDLL("1.so")

# Define the argument and return types for the C function.
lib.calculate_lambda.argtypes = [ctypes.c_double, ctypes.c_double, ctypes.c_double]
lib.calculate_lambda.restype = ctypes.c_double

# Define the coordinates for the points from the problem.
# P = (2, -2)
# Q = (3, 7)
# R = (24/11, y)
xp, yp = 2.0, -2.0
xq, yq = 3.0, 7.0
xr = 24.0 / 11.0

# Call the C function from Python to calculate lambda.
lambda_value = lib.calculate_lambda(xp, xq, xr)

# Now, we use the value of lambda to calculate the y-coordinate of point R.
# From the problem, y = (-2 + lambda * 7) / (1 + lambda)
if lambda_value != -1.0:
    yr = (yp + lambda_value * yq) / (1 + lambda_value)
    
    
    # Store all point coordinates for plotting.
    points_x = [xp, xq, xr]
    points_y = [yp, yq, yr]
    
    # Create the plot.
    plt.figure(figsize=(8, 6)) # Set the figure size for a better view
    
    # Plot the line segment PQ.
    plt.plot([xp, xq], [yp, yq], 'b-', label='Line segment PQ')
    
    # Plot the points with labels.
    plt.plot(xp, yp, 'ro', label='Point P') # 'ro' for red circles
    plt.text(xp, yp, f' P({xp:.2f}, {yp:.2f})', fontsize=12, ha='right')
    
    plt.plot(xq, yq, 'go', label='Point Q') # 'go' for green circles
    plt.text(xq, yq, f' Q({xq:.2f}, {yq:.2f})', fontsize=12, ha='left')
    
    plt.plot(xr, yr, 'yo', label='Point R') # 'yo' for yellow circles
    plt.text(xr, yr, f' R({xr:.2f}, {yr:.2f})', fontsize=12, ha='left')
    
    # Add titles and labels for clarity.
    plt.title('Visualization of Points P, Q, and R')
    plt.xlabel('X-axis')
    plt.ylabel('Y-axis')
    plt.legend()
    plt.grid(True)
    plt.axis('equal') # Ensure the x and y axes have the same scale
    plt.savefig('1.png')
    plt.show()
    