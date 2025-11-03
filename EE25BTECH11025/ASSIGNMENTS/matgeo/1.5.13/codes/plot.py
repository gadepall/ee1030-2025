import matplotlib.pyplot as plt
from call import get_data

P, A, B = get_data()

print(f"Intersection Point:({P[0]:.2f},{P[1]:.2f})")

x = [A[0], B[0]]
y = [A[1], B[1]]
px = P[0]
py = P[1]

plt.plot(x, y, color = 'black')
plt.plot(x, y, 'ko')
plt.plot(px, py, 'ko')

plt.text(x[0]+0.1, y[0]+0.1, f"({x[0]:.2f},{y[0]:.2f})", fontsize = 10, color='black')
plt.text(x[1]+0.1, y[1]+0.1, f"({x[1]:.2f},{y[1]:.2f})", fontsize = 10, color='black')
plt.text(px+0.1, py+0.1, f"({px:.2f},{py:.2f})", fontsize = 10, color='black')

plt.xlabel("X-axis")
plt.ylabel("Y-axis")
plt.axis("equal")
plt.grid(True)
plt.savefig("../figs/plot.png")
plt.show()

