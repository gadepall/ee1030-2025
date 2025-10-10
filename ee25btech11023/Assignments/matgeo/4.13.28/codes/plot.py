
import numpy as np
import matplotlib.pyplot as plt

from call import get_data_from_c

# Get the points and slopes from the C library
P, Q1, Q2, slopes = get_data_from_c()
slope1, slope2 = slopes

print(f"The two possible slopes are: {slope1:.4f} and {slope2:.4f}")

# --- Generate points for plotting the lines ---
x_line_given = np.array([-2, 8])
y_line_given = 7 - x_line_given

# Create points for the two possible solution lines
x_line_1 = np.array([P[0], Q1[0]])
y_line_1 = np.array([P[1], Q1[1]])
x_line_2 = np.array([P[0], Q2[0]])
y_line_2 = np.array([P[1], Q2[1]])

fig, ax = plt.subplots(figsize=(10, 8))

ax.plot(x_line_given, y_line_given, 'b-', label='Line x+y=7')
ax.plot(x_line_1, y_line_1, 'r-', label=f'Line with slope m={slope1:.2f}')
ax.plot(x_line_2, y_line_2, 'g-', label=f'Line with slope m={slope2:.2f}')

# Plot and label the points directly
ax.scatter(P[0], P[1], color='black', s=80)
ax.scatter(Q1[0], Q1[1], color='purple', s=80)
ax.scatter(Q2[0], Q2[1], color='purple', s=80)

ax.text(P[0] - 0.5, P[1] + 0.5, f'P({P[0]:.0f}, {P[1]:.0f})')
ax.text(Q1[0] + 0.3, Q1[1], 'Q1')
ax.text(Q2[0] - 1.0, Q2[1], 'Q2')

ax.set_title('Two Possible Lines and Their Slopes')
ax.set_xlabel('X-axis')
ax.set_ylabel('Y-axis')

ax.grid(True)
ax.axis('equal')
ax.legend()
plt.show()
plt.savefig('fig1.png')