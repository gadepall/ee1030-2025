import matplotlib.pyplot as plt

# vertices
A = (-4, 5)
B = (0, 7)
C = (5, -5)
D = (-4, -2)

# polygon coordinates (close by repeating A at end)
xs = [A[0], B[0], C[0], D[0], A[0]]
ys = [A[1], B[1], C[1], D[1], A[1]]

# plot
fig, ax = plt.subplots()
ax.plot(xs, ys, marker='o')
labels = ['A(-4,5)', 'B(0,7)', 'C(5,-5)', 'D(-4,-2)']
for (x, y), lab in zip([A, B, C, D], labels):
    ax.annotate(lab, (x, y))

ax.set_aspect('equal', adjustable='box')
ax.set_title('Quadrilateral ABCD')

# save and show
out_file = "quad.png"
plt.savefig(out_file)
plt.show()

print("Saved image to", out_file)

