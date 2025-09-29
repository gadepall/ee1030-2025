
import matplotlib
matplotlib.use('Agg')            
import matplotlib.pyplot as plt


x = [-2, -1, 0, 1, 3]
y = [8, 7, -1.25, 3, -1]


plt.figure(figsize=(6, 4))
plt.axhline(0, color='black', linewidth=1)   # x-axis
plt.axvline(0, color='black', linewidth=1)   # y-axis
plt.scatter(x, y, color='tab:blue', s=60, zorder=3)
plt.plot(x, y, color='tab:blue', linestyle='--', alpha=0.7, zorder=2)

for xi, yi in zip(x, y):
    plt.annotate(f'({xi}, {yi})', (xi, yi), textcoords="offset points", xytext=(5, 5), fontsize=9)

plt.title('Plot of given points')
plt.xlabel('x')
plt.ylabel('y')
plt.grid(True, linestyle=':', alpha=0.6)

plt.xlim(min(x) - 0.5, 5)   # x-axis goes up to 5
plt.ylim(min(y) - 0.5, 10)  # y-axis goes up to 10


plt.tight_layout()
plt.savefig('fig1.png', dpi=200)

