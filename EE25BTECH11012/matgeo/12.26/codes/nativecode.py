import matplotlib.pyplot as plt

# Define the points in the journey
p = (0, 0)
north_point = (0, 3)
q = (4, 3)
r = (-8, -6)
s = (-8, 0)

# Create the plot
plt.figure(figsize=(10, 8))
ax = plt.gca()

# Plot the path segments
# 1. P to North Point
plt.plot([p[0], north_point[0]], [p[1], north_point[1]], 'r-o', label='Path 1: 3 km North')
plt.annotate('3 km', xy=(0.1, 1.5), xytext=(0.1, 1.5))

# 2. North Point to Q
plt.plot([north_point[0], q[0]], [north_point[1], q[1]], 'g-o', label='Path 2: 4 km East')
plt.annotate('4 km', xy=(2, 3.1), xytext=(2, 3.1))

# 3. Q to R (towards P and beyond)
plt.plot([q[0], r[0]], [q[1], r[1]], 'b-o', label='Path 3: 15 km towards P')
# Add an arrow for this segment
ax.arrow(q[0], q[1], r[0]-q[0], r[1]-q[1], head_width=0.5, head_length=0.7, fc='blue', ec='blue', length_includes_head=True)
plt.annotate('15 km', xy=(-3, -2), xytext=(-3, -2), color='blue')

# 4. R to S
plt.plot([r[0], s[0]], [r[1], s[1]], 'm-o', label='Path 4: 6 km North')
plt.annotate('6 km', xy=(-8.5, -3), xytext=(-8.5, -3), color='purple', rotation=90)

# 5. Final path from S to P
plt.plot([s[0], p[0]], [s[1], p[1]], 'k--o', label='Final: 8 km East to P')
# Add an arrow for the final path
ax.arrow(s[0], s[1], p[0]-s[0], p[1]-s[1], head_width=0.5, head_length=0.7, fc='black', ec='black', length_includes_head=True)
plt.annotate('8 km', xy=(-4, 0.2), xytext=(-4, 0.2), color='black')

# Label the points
plt.text(p[0] - 0.5, p[1] - 0.5, 'P (Start)', fontsize=12)
plt.text(q[0] + 0.2, q[1] + 0.2, 'Q', fontsize=12)
plt.text(r[0] - 0.5, r[1] - 1, 'R', fontsize=12)
plt.text(s[0] - 1.5, s[1] + 0.2, 'S (Final)', fontsize=12)

# Set plot limits and labels
plt.xlim(-15, 10)
plt.ylim(-10, 10)
plt.xlabel("East-West Direction (km)")
plt.ylabel("North-South Direction (km)")
plt.title("Phani's Journey")
plt.axhline(0, color='grey', lw=0.5)
plt.axvline(0, color='grey', lw=0.5)
plt.grid(True)
plt.gca().set_aspect('equal', adjustable='box')
plt.legend()

# Add compass directions
plt.text(0, 9, 'North', ha='center', va='center', fontsize=10)
plt.text(0, -9, 'South', ha='center', va='center', fontsize=10)
plt.text(9, 0, 'East', ha='center', va='center', fontsize=10)
plt.text(-14, 0, 'West', ha='center', va='center', fontsize=10)

# Save the figure
plt.savefig("phanis_journey.png")
