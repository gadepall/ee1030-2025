import matplotlib.pyplot as plt
import numpy as np
from sympy import symbols, Eq, solve

# Given vertices
A = (1, -3)
C = (-9, 7)

# Solve for p when B = (4, p) such that area = 15
p = symbols('p', real=True)
x1, y1 = A
x2, y2 = 4, p
x3, y3 = C

expr = 0.5 * abs(x1*(y2 - y3) + x2*(y3 - y1) + x3*(y1 - y2))
solutions = solve(Eq(expr, 15), p)
print("Possible values of p:", solutions)

# Plot triangles for each p
fig, ax = plt.subplots(figsize=(7, 6))

colors = ['royalblue', 'darkorange']
for sol, col in zip(solutions, colors):
    B = (4, float(sol))
    xs = [A[0], B[0], C[0], A[0]]
    ys = [A[1], B[1], C[1], A[1]]
    ax.plot(xs, ys, marker='o', color=col, label=f'p = {sol}')
    ax.text(B[0]+0.2, B[1], f'B(4,{sol.evalf():.2f})', fontsize=10, color=col)

# Mark and label points A and C
ax.text(A[0]+0.2, A[1], 'A(1,-3)', fontsize=10, color='black')
ax.text(C[0]-2, C[1], 'C(-9,7)', fontsize=10, color='black')

# Draw axes lines for reference
ax.axhline(0, color='gray', linewidth=0.8)
ax.axvline(0, color='gray', linewidth=0.8)

ax.set_xlabel('X-axis')
ax.set_ylabel('Y-axis')
ax.set_title('Triangle for given area = 15 sq.units')
ax.legend()
ax.grid(True)
plt.show()