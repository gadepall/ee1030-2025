import matplotlib.pyplot as plt

def findA(xp, yp, xb, yb):
    xa = 2*xp - xb
    ya = 2*yp - yb
    return xa, ya


xp, yp = 0, 4
xb, yb = -2, 3

xa, ya = findA(xp, yp, xb, yb)
print(f"Coordinates of A: ({xa}, {ya})")


plt.figure(figsize=(6,6))
plt.scatter([xa, xb, xp], [ya, yb, yp], color=['red','blue','green'], s=100)

plt.text(xa+0.1, ya, "A(2,5)", fontsize=12)
plt.text(xb+0.1, yb, "B(-2,3)", fontsize=12)
plt.text(xp+0.1, yp, "P(0,4)", fontsize=12)


plt.plot([xa, xb], [ya, yb], 'k--', label="AB")
plt.scatter(xp, yp, color='green', s=120, marker='x', label="Midpoint P")

plt.axhline(0, color='gray', linewidth=0.5)
plt.axvline(0, color='gray', linewidth=0.5)
plt.legend()
plt.grid(True)
plt.show()

