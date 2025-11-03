import numpy as np

# --- Script to verify the conic equation: 2y^2 - 9x = 0 ---

print("Verifying the equation: 2y^2 - 9x = 0\n")

# The conditions given in the problem
point_to_check = (2, 3)
vertex_to_check = (0, 0)

all_conditions_met = True

# --- Condition 1: Check if the vertex is on the curve ---
vx, vy = vertex_to_check
# Directly calculate the result of the equation for the vertex
vertex_result = 2 * vy**2 - 9 * vx
if not np.isclose(vertex_result, 0):
    print(f"FAILED: The vertex {vertex_to_check} is NOT on the curve.")
    all_conditions_met = False
else:
    print(f"PASSED: The vertex {vertex_to_check} is on the curve.")
    
# --- Condition 2: Check if the given point is on the curve ---
px, py = point_to_check
# Directly calculate the result of the equation for the point
point_result = 2 * py**2 - 9 * px
if not np.isclose(point_result, 0):
    print(f"FAILED: The point {point_to_check} is NOT on the curve.")
    all_conditions_met = False
else:
    print(f"PASSED: The point {point_to_check} is on the curve.")
    
# --- Condition 3: Check for X-axis symmetry ---
# An equation is symmetric about the x-axis if replacing y with -y
# does not change the equation. This is true for y^2 terms.
reflected_y = -py
# Directly calculate the result for the reflected point
reflected_point_result = 2 * reflected_y**2 - 9 * px
if not np.isclose(reflected_point_result, point_result):
    print("FAILED: The equation is not symmetric about the X-axis.")
    all_conditions_met = False
else:
    print("PASSED: The equation is symmetric about the X-axis.")
    
print("\n-------------------------------------")
if all_conditions_met:
    print("Conclusion: The solution is correct.")
else:
    print("Conclusion: The solution is incorrect.")

