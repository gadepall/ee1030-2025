import ctypes
import platform
import matplotlib.pyplot as plt

# --- 1. Load the C Shared Library ---
calc_lib = ctypes.CDLL('./code.so')

# --- 2. Define the C Function's Signature ---
calculate_and_get_plot_data = calc_lib.calculate_and_get_plot_data
calculate_and_get_plot_data.argtypes = [
    ctypes.POINTER(ctypes.c_double), # a_in
    ctypes.POINTER(ctypes.c_double), # b_in
    ctypes.POINTER(ctypes.c_double), # p_out
    ctypes.POINTER(ctypes.c_double), # ratio_out
    ctypes.POINTER(ctypes.c_double), # line_x
    ctypes.POINTER(ctypes.c_double), # line_y
    ctypes.c_int                     # num_line_points
]
calculate_and_get_plot_data.restype = None

# --- 3. Get User Input for Points A and B ---
try:
    ax, ay = map(float, input("Enter coordinates for point A (e.g., -2 -5): ").split())
    bx, by = map(float, input("Enter coordinates for point B (e.g., 6 3): ").split())
except ValueError:
    print("Invalid input. Please enter two numbers separated by a space.")
    exit()

# --- 4. Prepare Data Buffers and Call C Function ---
a_in = (ctypes.c_double * 2)(ax, ay)
b_in = (ctypes.c_double * 2)(bx, by)

p_out = (ctypes.c_double * 2)()
ratio_out = (ctypes.c_double * 2)()
num_line_points = 50
line_x = (ctypes.c_double * num_line_points)()
line_y = (ctypes.c_double * num_line_points)()

calculate_and_get_plot_data(a_in, b_in, p_out, ratio_out, line_x, line_y, num_line_points)

# --- 5. Display Results and Plot ---
px, py = p_out[0], p_out[1]
m, n = ratio_out[0], ratio_out[1]

print("\n--- Calculation Results from C ---")
print(f"Intersection Point P: ({px:.2f}, {py:.2f})")
if n > 1e-9:
    print(f"Ratio AP:PB is {m:.2f}:{n:.2f}, which is approximately {m/n:.2f}:1")
else:
    print("Ratio is undefined (line may be parallel or input is degenerate).")

# Plotting
plt.figure(figsize=(10, 8))
plt.plot([ax, bx], [ay, by], 'b-o', label=f'Segment AB')
plt.plot(list(line_x), list(line_y), 'g--', label='Line x - 3y = 0')

# Annotate points
plt.scatter([ax, bx], [ay, by], color='blue', s=80, zorder=5)
plt.text(ax, ay + 0.3, f' A({ax}, {ay})')
plt.text(bx, by + 0.3, f' B({bx}, {by})')

plt.scatter(px, py, color='red', s=100, zorder=5, label=f'Intersection P({px:.2f}, {py:.2f})')
plt.text(px, py + 0.3, f' P')

# Finalize plot
plt.title(f'Intersection of Segment AB and Line x - 3y = 0')
plt.xlabel('X-axis')
plt.ylabel('Y-axis')
plt.axhline(0, color='black', linewidth=0.5)
plt.axvline(0, color='black', linewidth=0.5)
plt.grid(True, linestyle=':')
plt.legend()
plt.axis('equal')
# Save the plot to a file
plt.savefig('../figs/fig.png')
plt.show()
