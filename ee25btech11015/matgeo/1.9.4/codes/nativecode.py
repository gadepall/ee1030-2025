import numpy as np
import matplotlib.pyplot as plt

# Define range of λ
lmbda = np.linspace(-3, 2, 400)
y = 4 * np.abs(lmbda)

# Simple 2D plot
plt.plot(lmbda, y)
plt.xlabel("λ")
plt.ylabel("‖λa‖")
plt.title("Graph of ‖λa‖ = 4|λ|")
plt.grid(True)
plt.show()
