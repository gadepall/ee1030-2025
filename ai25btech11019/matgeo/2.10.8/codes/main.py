import matplotlib.pyplot as plt

plt.figure(figsize=(6, 6))

# Draw axes
plt.axhline(0, color='black', linewidth=2)
plt.axvline(0, color='black', linewidth=2)

# Vectors from the origin
plt.arrow(0, 0, 4, 3, head_width=0.18, head_length=0.22, fc='black', ec='black', linewidth=2.8, length_includes_head=True)
plt.arrow(0, 0, -3, 4, head_width=0.18, head_length=0.22, fc='black', ec='black', linewidth=2.8, length_includes_head=True)
plt.arrow(0, 0, 2, -4, head_width=0.18, head_length=0.22, fc='black', ec='black', linewidth=2.8, length_includes_head=True)

# Labels and Formatting
plt.text(4.2, 3.1, r"$b = (4, 3)$", fontsize=16)         # b label
plt.text(-4.8, 4.3, r"$c = (-3, 4)$", fontsize=16)        # c label (fix typo to match usage)
plt.text(0.2, 2.1, "c", fontsize=16)                       # small c near center
plt.text(5.25, -0.3, "x", fontsize=18)                     # x axis label
plt.text(0.3, 5.45, "y", fontsize=18)                      # y axis label
plt.text(2.1, -3.8, r"$\frac{-2}{5} = \frac{11}{5}$", fontsize=16)  # fractional label

# Set tick positions and ranges
plt.xlim(-5, 6)
plt.ylim(-5, 6)
plt.xticks(range(-4, 7, 2))
plt.yticks(range(-4, 7, 2))

# Equal aspect for square grid
plt.gca().set_aspect('equal')
plt.tight_layout()
plt.show()
