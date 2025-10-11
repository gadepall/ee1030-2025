import matplotlib.pyplot as plt

# Points
A = (3, 2)
B = (-2, -3)
C = (2, 3)

# Vectors AB, AC
AB = (B[0] - A[0], B[1] - A[1])
AC = (C[0] - A[0], C[1] - A[1])

# Dot product for perpendicular check
dot = AB[0]*AC[0] + AB[1]*AC[1]

# Plot
fig, ax = plt.subplots(figsize=(6,6))

# Triangle edges
ax.plot([A[0], B[0]], [A[1], B[1]], 'gray')
ax.plot([B[0], C[0]], [B[1], C[1]], 'gray')
ax.plot([C[0], A[0]], [C[1], A[1]], 'gray')

# Points
ax.scatter(A[0], A[1], color='green', marker='*', s=150, zorder=5, label="A (3,2)")
ax.scatter(B[0], B[1], color='red', s=80, zorder=5, label="B (-2,-3)")
ax.scatter(C[0], C[1], color='blue', s=80, zorder=5, label="C (2,3)")

# Labels
ax.text(A[0]+0.2, A[1]+0.2, "A (3,2)", fontsize=11, fontweight="bold")
ax.text(B[0]-0.8, B[1]-0.4, "B (-2,-3)", fontsize=11)
ax.text(C[0]+0.2, C[1]+0.2, "C (2,3)", fontsize=11)

# Arrows AB and AC
ax.arrow(A[0], A[1], AB[0]*0.9, AB[1]*0.9, 
         head_width=0.2, length_includes_head=True, color="red", alpha=0.8)
ax.arrow(A[0], A[1], AC[0]*0.9, AC[1]*0.9, 
         head_width=0.2, length_includes_head=True, color="blue", alpha=0.8)

# Arrow labels
ax.text(A[0] + AB[0]*0.45 - 0.2, A[1] + AB[1]*0.45 - 0.2, "AB", color="red")
ax.text(A[0] + AC[0]*0.45 + 0.1, A[1] + AC[1]*0.45 + 0.1, "AC", color="blue")

# Show dot product result
msg = f"AB·AC = {dot}  ⇒  {'Perpendicular' if dot == 0 else 'Not perpendicular'}"
ax.text(-4.5, 4.5, msg, bbox=dict(facecolor='white', edgecolor='black'))

# Axes + formatting
ax.axhline(0, color="black", linewidth=0.6)
ax.axvline(0, color="black", linewidth=0.6)
ax.set_xlim(-6, 6)
ax.set_ylim(-6, 6)
ax.set_aspect("equal", "box")
ax.grid(True, linestyle="--", alpha=0.6)
ax.set_title("Triangle ABC — check if right-angled at A")
plt.savefig("fig3.png")
plt.show()