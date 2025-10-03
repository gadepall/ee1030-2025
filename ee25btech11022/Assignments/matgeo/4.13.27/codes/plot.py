import matplotlib.pyplot as plt
from call import extract_points

n_points = 20
concurrency_point = (0.75, 0.5)
t_values = [1.0, 1.5, 2.0, 2.5]  # Different lines in the family

plt.figure(figsize=(8,6))

for t in t_values:
    x, y = extract_points(n_points, t)
    plt.plot(x, y, label=f'p={t}')
    plt.scatter(x, y, s=10)

plt.scatter([concurrency_point[0]], [concurrency_point[1]], color='red', marker='X', s=100, label='Concurrency point')
plt.title('Family of lines passing through (3/4, 1/2)')
plt.xlabel('x')
plt.ylabel('y')
plt.grid(True)
plt.legend()
plt.show()

