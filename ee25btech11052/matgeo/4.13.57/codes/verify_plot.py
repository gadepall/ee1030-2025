import ctypes
import numpy as np
import matplotlib.pyplot as plt
import os

# --- 1. Load C Library and Define Function Signature ---
# Load the newly named shared library (libverify.so)
lib_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'libverify.so')
lib = ctypes.CDLL(lib_path)

# Tell Python what kind of arguments the C function expects and what it returns
lib.calculate_intercept_length.argtypes = [ctypes.c_double] * 9
lib.calculate_intercept_length.restype = ctypes.c_double

# --- 2. Define Problem Parameters ---
# Parallel lines in Ax + By = C form
line1 = {'A': 2, 'B': 1, 'C': 3, 'label': '$y+2x=3$'}
line2 = {'A': 2, 'B': 1, 'C': 5, 'label': '$y+2x=5$'}
# The point the solution lines must pass through
P = (2, 3)
# The two solution lines to be verified
solution1_coeffs = {'A': 1, 'B': 0, 'C': 2}
solution2_coeffs = {'A': 3, 'B': 4, 'C': 18}

# --- 3. Call C Function and Verify ---
print("--- Verifying Solutions using C function ---")

# Verify the first solution: x = 2
length1 = lib.calculate_intercept_length(
    solution1_coeffs['A'], solution1_coeffs['B'], solution1_coeffs['C'],
    line1['A'], line1['B'], line1['C'],
    line2['A'], line2['B'], line2['C']
)
print("Solution 'x = 2':")
print(f"  Calculated intercept length = {length1:.4f}")
print("  Result: PASS\n") if np.isclose(length1, 2.0) else print("  Result: FAIL\n")

# Verify the second solution: 3x + 4y = 18
length2 = lib.calculate_intercept_length(
    solution2_coeffs['A'], solution2_coeffs['B'], solution2_coeffs['C'],
    line1['A'], line1['B'], line1['C'],
    line2['A'], line2['B'], line2['C']
)
print("Solution '3x + 4y = 18':")
print(f"  Calculated intercept length = {length2:.4f}")
print("  Result: PASS\n") if np.isclose(length2, 2.0) else print("  Result: FAIL\n")

# --- 4. Plotting ---
fig, ax = plt.subplots(figsize=(9, 8))
x_range = np.linspace(-2, 6, 2)

# Plot the two parallel lines
y1 = (line1['C'] - line1['A'] * x_range) / line1['B']
y2 = (line2['C'] - line2['A'] * x_range) / line2['B']
ax.plot(x_range, y1, 'k-', label=line1['label'])
ax.plot(x_range, y2, 'k-', label=line2['label'])

# --- Plot Solution 1 (x=2) ---
# Calculate intersection points B1 and D1
B1 = np.linalg.solve(np.array([[1,0],[2,1]]), np.array([2,3]))
D1 = np.linalg.solve(np.array([[1,0],[2,1]]), np.array([2,5]))
# Plot the line and its intercept
ax.axvline(x=2, color='r', linestyle='--', label='Solution: x = 2')
ax.plot([B1[0], D1[0]], [B1[1], D1[1]], 'r-', linewidth=3, label='Intercept Segment 1')
ax.plot(B1[0], B1[1], 'ro'); ax.text(B1[0] + 0.1, B1[1], 'B1', color='r', fontweight='bold')
ax.plot(D1[0], D1[1], 'ro'); ax.text(D1[0] + 0.1, D1[1], 'D1', color='r', fontweight='bold')

# --- Plot Solution 2 (3x+4y=18) ---
# Calculate intersection points B2 and D2
B2 = np.linalg.solve(np.array([[3,4],[2,1]]), np.array([18,3]))
D2 = np.linalg.solve(np.array([[3,4],[2,1]]), np.array([18,5]))
# Plot the line and its intercept
y_sol2 = (18 - 3 * x_range) / 4
ax.plot(x_range, y_sol2, 'g--', label='Solution: 3x+4y=18')
ax.plot([B2[0], D2[0]], [B2[1], D2[1]], 'g-', linewidth=3, label='Intercept Segment 2')
ax.plot(B2[0], B2[1], 'go'); ax.text(B2[0] + 0.1, B2[1], 'B2', color='g', fontweight='bold')
ax.plot(D2[0], D2[1], 'go'); ax.text(D2[0] + 0.1, D2[1], 'D2', color='g', fontweight='bold')

# Plot the starting point P
ax.plot(P[0], P[1], 'bo', markersize=10, label='Point P(2, 3)')
ax.text(P[0] + 0.1, P[1] - 0.1, 'P(2,3)', color='b', fontweight='bold')

# --- 5. Format and Save Plot ---
ax.set_aspect('equal', adjustable='box')
ax.set_xlim(-5, 10); ax.set_ylim(-5, 7)
ax.axhline(0, color='black', linewidth=0.5); ax.axvline(0, color='black', linewidth=0.5)
ax.set_xlabel('x-axis'); ax.set_ylabel('y-axis')
ax.grid(True, linestyle=':', alpha=0.7)
ax.legend(); ax.set_title("Line Intercept Problem Verification")

plt.savefig("/home/shriyasnh/Desktop/matgeonew/4.13.57/figs/line_intercept_plot.png", dpi=300)
plt.show()

