import ctypes
import matplotlib.pyplot as plt
import sys

c_library = ctypes.CDLL('./mat.so')



POINTER_TO_DOUBLE = ctypes.POINTER(ctypes.c_double)
c_library.GSM.argtypes = [POINTER_TO_DOUBLE, POINTER_TO_DOUBLE, POINTER_TO_DOUBLE, POINTER_TO_DOUBLE, POINTER_TO_DOUBLE]
c_library.GSM.restype = None


DoubleArray3 = ctypes.c_double * 3


x_result = DoubleArray3(1.0, 1.0, 1.0)

# Coefficients for the system of equations
a = DoubleArray3(5.0, -2.0, -1.0)
b = DoubleArray3(2.0, 5.0, 2.0)
c = DoubleArray3(1.0, 2.0, 8.0)
d = DoubleArray3(13.0, -22.0, 14.0)


c_library.GSM(x_result, a, b, c, d)


# Extract the final point for clarity
final_point = (x_result[0], x_result[1], x_result[2])
print(f"Calculated point (x0, x1, x2): ({final_point[0]:.4f}, {final_point[1]:.4f}, {final_point[2]:.4f})")


start_point = (1.0, 1.0, 1.0) # The initial guess

fig = plt.figure(figsize=(9, 8))
ax = fig.add_subplot(111, projection='3d')

# Plot the starting point
ax.scatter(start_point[0], start_point[1], start_point[2], c='blue', s=100, label='Start Point', depthshade=True)
ax.text(start_point[0], start_point[1], start_point[2], f'  ({start_point[0]:.1f}, {start_point[1]:.1f}, {start_point[2]:.1f})', color='blue', fontsize=12)

# Plot the calculated point
ax.scatter(final_point[0], final_point[1], final_point[2], c='red', s=100, label='Calculated Point (1 Iteration)', depthshade=True)
ax.text(final_point[0], final_point[1], final_point[2], f'  ({final_point[0]:.2f}, {final_point[1]:.2f}, {final_point[2]:.2f})', color='red', fontsize=12)

# Setting labels and title
ax.set_xlabel('X Axis')
ax.set_ylabel('Y Axis')
ax.set_zlabel('Z Axis')
ax.set_title('3D Plot of Start vs. Calculated Point')
ax.legend()
ax.grid(True)

# Improve layout
plt.tight_layout()
print("Displaying plot...")
plt.savefig('1.png')
plt.show()


