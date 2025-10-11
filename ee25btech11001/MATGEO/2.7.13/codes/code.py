import matplotlib.pyplot as plt

# Correct order: A -> B -> D -> C
points = [(-4, -5), (-1, -6), (4, 5), (-5, 7)]
x = [p[0] for p in [*points, points[0]]]
y = [p[1] for p in [*points, points[0]]]

# Shoelace formula
area = 0
for i in range(len(points)):
    x1, y1 = points[i]
    x2, y2 = points[(i + 1) % len(points)]
    area += x1 * y2 - x2 * y1
area = abs(area) / 2

plt.fill(x, y, alpha=0.3, color="skyblue", edgecolor="black")
plt.scatter(x, y, color="red")

labels = ["A(-4,-5)", "B(-1,-6)", "D(4,5)", "C(-5,7)"]
for xi, yi, lbl in zip(x[:-1], y[:-1], labels):
    plt.text(xi, yi, lbl, fontsize=9, ha="right")

plt.title(f"Quadrilateral ABCD, Area={area}")
plt.gca().set_aspect("equal", adjustable="box")
plt.show()

