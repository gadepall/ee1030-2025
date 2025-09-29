import numpy as np #for arrays
import matplotlib.pyplot as plt #for plotting graphs

A = np.array([-6,10])
B = np.array([3,-8])
P = np.array([-4,6])

plt.figure(figsize=(7,7)) #creates 7*7 inches graph
plt.plot([A[0], B[0]], [A[1], B[1]], 'g--', label = "Line AB") #plt.plot(x_list, y_list, style, label=...)

plt.scatter(*A, color="red")#colour of points
plt.scatter(*B, color="blue")
plt.scatter(*P, color="black")

plt.text(A[0], A[1]+0.5, "A(-6, 10)", fontsize = 10)#places text on the plot +0.5 prevents overlap
plt.text(B[0], B[1]-0.8, "B(3,-8)", fontsize = 10)
plt.text(P[0]+0.5, P[1], "C(-4,6)", fontsize = 10)

plt.xlabel("X-Axis")
plt.ylabel("Y-Axis")
plt.title("Point P divides AB in the ratio 2:7")
plt.legend()
plt.grid(True)
plt.axis("equal")
plt.savefig("fig.png")
plt.show()
