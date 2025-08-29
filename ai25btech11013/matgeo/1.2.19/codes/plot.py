import matplotlib.pyplot as plt

# Given points
points = [(-2, 4), (3, -1), (-1, 0), (1, 2), (-3, -5)]


# Plotting using plt only
plt.axhline(0, color='black')  # x-axis
plt.axvline(0, color='black')  # y-axis

for (x, y) in points:
    plt.scatter(x, y, s=80)
    plt.text(x+0.1, y+0.1, f"({x},{y})", fontsize=9)

plt.title("Points on Cartesian Plane (Q1.2.19)")
plt.xlabel("X-axis")
plt.ylabel("Y-axis")
plt.grid(True)
plt.gca().set_aspect('equal', adjustable='box')
plt.savefig("/home/gauthamp/ee1030-2025/ai25btech11013/matgeo/1.2.19/figs/Figure1.png")
plt.show()
