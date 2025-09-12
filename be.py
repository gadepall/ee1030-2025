plt.title("Triangle formed by P, Q, R")
plt.axhline(0, color='black', linewidth=0.5)
plt.axvline(0, color='black', linewidth=0.5)
plt.grid(True)
plt.legend()
plt.axis("equal")

# Save as picture
plt.savefig("fig2d.png")   # saves in current folder
plt.show()
