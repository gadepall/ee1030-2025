import numpy as np
import matplotlib.pyplot as plt
import matplotlib
matplotlib.use("Agg")  # headless backend
import matplotlib.pyplot as plt

# your plotting code...

# Point coordinates (coefficients of a and b)
Px, Py = 3.0, -2.0   # P = 3a - 2b
Qx, Qy = 1.0,  1.0   # Q = 1a + 1b
m, n = 2, 1          # ratio 2:1

# Internal Division: (mQ + nP) / (m+n)
Rx_int = (m*Qx + n*Px) / (m+n)
Ry_int = (m*Qy + n*Py) / (m+n)

# External Division: (mQ - nP) / (m-n)
Rx_ext = (m*Qx - n*Px) / (m-n)
Ry_ext = (m*Qy - n*Py) / (m-n)

# Print results
print(f"Internal Division: R = {Rx_int:.2f}a + {Ry_int:.2f}b")
print(f"External Division: R = {Rx_ext:.2f}a + {Ry_ext:.2f}b")

# Plotting
plt.figure(figsize=(6,6))
plt.scatter([Px, Qx, Rx_int, Rx_ext],
            [Py, Qy, Ry_int, Ry_ext],
            color=["red","blue","green","purple"], s=100)

# Labels
plt.text(Px, Py, "P", fontsize=12, color="red")
plt.text(Qx, Qy, "Q", fontsize=12, color="blue")
plt.text(Rx_int, Ry_int, "R_int", fontsize=12, color="green")
plt.text(Rx_ext, Ry_ext, "R_ext", fontsize=12, color="purple")

# Draw line PQ
plt.plot([Px, Qx], [Py, Qy], "k--", label="PQ")

# Axes styling
plt.axhline(0, color="gray", linewidth=0.5)
plt.axvline(0, color="gray", linewidth=0.5)
plt.xlabel("Coefficient of a")
plt.ylabel("Coefficient of b")
plt.legend()
plt.title("Section Formula Plot (Internal & External Division)")
plt.grid(True)
plt.savefig("q1.png")
plt.show()
