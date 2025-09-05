import numpy as np
import matplotlib.pyplot as plt
import matplotlib as mp
mp.use("TkAgg")

# Fixed point B
B = (9, 8)

# Two A points
A1 = (1, 2)
A2 = (17, 2)

# Distances using numpy
d1 = np.sqrt((A1[0]-B[0])**2 + (A1[1]-B[1])**2)
d2 = np.sqrt((A2[0]-B[0])**2 + (A2[1]-B[1])**2)

# Plot line segments B->A1 and B->A2
plt.figure(figsize=(6,6))

# Line B->A1
plt.plot([B[0], A1[0]], [B[1], A1[1]], 'b-o', label=f"B→A1 {A1}, d={d1:.2f}")
plt.text(A1[0], A1[1], f"A1{A1}", fontsize=12, ha='left')

# Line B->A2
plt.plot([B[0], A2[0]], [B[1], A2[1]], 'g-o', label=f"B→A2 {A2}, d={d2:.2f}")
plt.text(A2[0], A2[1], f"A2{A2}", fontsize=12, ha='left')

# Mark B
plt.scatter(B[0], B[1], color='red')
plt.text(B[0], B[1], "B(9,8)", fontsize=12, ha='right')

# Labels & styling
plt.xlabel("X-axis")
plt.ylabel("Y-axis")
plt.title("Line Segments from B(9,8) to A1 and A2")
plt.legend()
plt.grid(True)
plt.axis("equal")
plt.savefig('/home/avaneesh1/Matrix/ee1030-2025/ee25btech11030/matgeo/1.9.19/figs/distance2.png')
plt.show(block=True)
