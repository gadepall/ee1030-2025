import ctypes
import numpy as np
import matplotlib.pyplot as plt

# Load the shared library
lib_conic = ctypes.CDLL("./code14.so") 


# Define the argument types and return type for the C function
lib_conic.calculateEllipseProperties.argtypes = [
    ctypes.c_double,  # a_val
    ctypes.c_double,  # b_val
    ctypes.POINTER(ctypes.c_double), # focus_y_ptr
    ctypes.POINTER(ctypes.c_double), # vertex_y_ptr
    ctypes.POINTER(ctypes.c_double), # eccentricity_ptr
    ctypes.POINTER(ctypes.c_double), # directrix_y_ptr
    ctypes.POINTER(ctypes.c_double)  # latus_rectum_ptr
]
lib_conic.calculateEllipseProperties.restype = None

# --- Analyze the Ellipse: 16x^2 + y^2 = 16 ---
# From 16x^2 + y^2 = 16, divide by 16: x^2/1 + y^2/16 = 1
# This is an ellipse centered at (0,0) with major axis along y.
# a^2 = 16 => a = 4 (major semi-axis)
# b^2 = 1 => b = 1 (minor semi-axis)
a_val = 4.0
b_val = 1.0
center = np.array([0.0, 0.0]) # Center is (0,0)

# Create ctypes doubles to hold the results from the C function
focus_y_result = ctypes.c_double()
vertex_y_result = ctypes.c_double()
eccentricity_result = ctypes.c_double()
directrix_y_result = ctypes.c_double()
latus_rectum_result = ctypes.c_double()

# Call the C function to get the ellipse properties
lib_conic.calculateEllipseProperties(
    a_val,
    b_val,
    ctypes.byref(focus_y_result),
    ctypes.byref(vertex_y_result),
    ctypes.byref(eccentricity_result),
    ctypes.byref(directrix_y_result),
    ctypes.byref(latus_rectum_result)
)

# Extract the values from the ctypes doubles
focus_y = focus_y_result.value
vertex_y = vertex_y_result.value
eccentricity = eccentricity_result.value
directrix_y = directrix_y_result.value
latus_rectum = latus_rectum_result.value

# Calculate the other points needed for plotting and printing
# Vertices (along major axis, y-axis)
vertex1 = np.array([0.0, vertex_y])
vertex2 = np.array([0.0, -vertex_y])

# Foci (along major axis, y-axis)
focus1 = np.array([0.0, focus_y])
focus2 = np.array([0.0, -focus_y])


print(f"--- Conic Section Properties (Ellipse: 16x^2 + y^2 = 16) ---")
print(f"Center: ({center[0]:.0f}, {center[1]:.0f})")
print(f"Vertices: ({vertex1[0]:.0f}, {vertex1[1]:.0f}) and ({vertex2[0]:.0f}, {vertex2[1]:.0f})")
print(f"Foci: ({focus1[0]:.2f}, {focus1[1]:.2f}) and ({focus2[0]:.2f}, {focus2[1]:.2f})")
print(f"Eccentricity: {eccentricity:.4f}")
print(f"Axis of the conic section: y-axis (x=0) is the major axis")
print(f"Equation of Directrices: y = {directrix_y:.2f} and y = {-directrix_y:.2f}")
print(f"Length of Latus Rectum: {latus_rectum:.2f}")


# --- Plotting the Ellipse with improved aesthetics ---
plt.figure(figsize=(10, 10))
ax = plt.gca()

# Generate points for the ellipse
theta = np.linspace(0, 2 * np.pi, 200)
x_ellipse = b_val * np.cos(theta)
y_ellipse = a_val * np.sin(theta)
plt.plot(x_ellipse, y_ellipse, "blue", linewidth=2, label='Ellipse $16x^2 + y^2 = 16$')

# Plot Center (Black dot)
plt.scatter(0, 0, color='black', s=30, zorder=5, label='Center (0,0)')

# Plot Vertices (Red dots)
plt.scatter(0, vertex_y, color='red', s=30, zorder=5, label=f'Vertices (0, $\\pm${vertex_y:.0f})')
plt.scatter(0, -vertex_y, color='red', s=30, zorder=5)
# Annotations for vertices
plt.annotate(f'(0, {vertex_y:.0f})', (0, vertex_y), textcoords="offset points", xytext=(5, 5), ha='left', color='red', fontsize=10)
plt.annotate(f'(0, {-vertex_y:.0f})', (0, -vertex_y), textcoords="offset points", xytext=(5, 5), ha='left', color='red', fontsize=10)


# Plot Foci (Green dots)
plt.scatter(0, focus_y, color='green', s=30, zorder=5, label=f'Foci (0, $\\pm${focus_y:.2f})')
plt.scatter(0, -focus_y, color='green', s=30, zorder=5)
# Annotations for foci
plt.annotate(f'(0, {focus_y:.2f})', (0, focus_y), textcoords="offset points", xytext=(5, -15), ha='left', color='green', fontsize=10)
plt.annotate(f'(0, {-focus_y:.2f})', (0, -focus_y), textcoords="offset points", xytext=(5, 5), ha='left', color='green', fontsize=10)


# Plot Directrices (Magenta dashed lines)
x_plot_limits = np.array([-b_val * 2.5, b_val * 2.5]) # Set x limits for directrix lines
plt.plot(x_plot_limits, [directrix_y, directrix_y], 'b--', linewidth=1.5, label=f'Directrices y = $\\pm${directrix_y:.2f}')
plt.plot(x_plot_limits, [-directrix_y, -directrix_y], 'b--', linewidth=1.5)

# Plot Latus Rectum (Cyan dotted lines)
lr_half = latus_rectum / 2
plt.plot([-lr_half, lr_half], [focus_y, focus_y], 'g-', linewidth=2, label=f'Latus Rectum Length={latus_rectum:.2f}')
plt.plot([-lr_half, lr_half], [-focus_y, -focus_y], 'g-', linewidth=2)


ax.set_aspect('equal', adjustable='box')
plt.xlabel('X-axis')
plt.ylabel('Y-axis')
plt.title('Properties of the Ellipse $16x^2 + y^2 = 16$')
plt.grid(True)

# Place the legend outside the plot area, bottom left, with styling
plt.legend(loc='center left', bbox_to_anchor=(1.05, 0.5), fancybox=True, shadow=True, ncol=1, fontsize='small')

# Set explicit plot limits
plt.xlim(-2.5, 2.5)
plt.ylim(-5, 5)

# Use tight_layout to adjust plot parameters, leaving space at the bottom for the legend
plt.tight_layout(rect=[0, 0.2, 1, 1])

# Save the figure
plt.savefig("fig1.png")
plt.show()

print("\nFigure saved as fig1.png")
