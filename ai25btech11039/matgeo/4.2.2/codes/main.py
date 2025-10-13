import matplotlib.pyplot as plt
import numpy as np

# Define the line: y = 5x - 100
x = np.linspace(15, 25, 200)
y = 5*x - 100

plt.figure(figsize=(7,5))
plt.axhline(0, color='black', linewidth=0.8)
plt.axvline(0, color='black', linewidth=0.8)
plt.plot(x, y, label=r"$x - \dfrac{y}{5} - 10 = 10$", color="blue")

# Point A on the line (20,0)
A = (20, 0)
plt.scatter(*A, color="black")
plt.text(A[0]-0.5, A[1]-2, r"$\vec{A}$", fontsize=12)

# Normal vector n = (1,-1/5) scaled
n = np.array([1, -0.2])*10
plt.arrow(A[0], A[1], n[0], n[1], head_width=0.5, head_length=1,
          fc='red', ec='red')
plt.text(A[0]+n[0]/2, A[1]+n[1]/2-2, r"$\vec{n}$", color="red", fontsize=12)

# Direction vector m = (1,5)
m = np.array([1, 5])
plt.arrow(A[0], A[1], m[0], m[1], head_width=0.5, head_length=1,
          fc='green', ec='green')
plt.text(A[0]+m[0]/2, A[1]+m[1]/2, r"$\vec{m}$", color="green", fontsize=12)

plt.xlim(15, 27)
plt.ylim(-15, 30)
plt.xlabel("$x$")
plt.ylabel("$y$")
plt.legend()
plt.grid(True)
plt.title("Graph of line with normal and direction vectors")

# Save to figs folder
plt.savefig("figs/4.2.2.png", dpi=300, bbox_inches='tight')
plt.show()
