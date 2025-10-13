import numpy as np
import matplotlib.pyplot as plt

# --- Step 1: Matrix method to find required line ---
n1 = np.array([2, 1])
c1 = 5
n2 = np.array([1, 3])
c2 = -8
n3 = np.array([3, 4])  # line to be parallel

lambda_val = 1  # from calculation

# Normal vector and constant of required line
N = n1 + lambda_val * n2
c = c1 + lambda_val * c2

print("Normal vector of required line:", N)
print("Constant term:", c)
print(f"Equation of line: {N[0]}x + {N[1]}y + {c} = 0\n")

# --- Step 2: Generate points along the line in Python ---
# Pick a direction vector perpendicular to normal
d = np.array([-N[1], N[0]])

# Pick t values for points along the line
t_values = np.linspace(-10, 10, 21)  # 21 points
# Pick a point on the line: x0 = 0, y0 = -c/N[1]
x0 = 0
y0 = -c / N[1]
points = np.array([ [x0 + t*d[0], y0 + t*d[1]] for t in t_values ])

# --- Step 3: Plot ---
plt.figure(figsize=(8,6))
plt.scatter(points[:,0], points[:,1], color='red', label='Generated points')

# Plot the exact line
x_vals = np.linspace(points[:,0].min()-1, points[:,0].max()+1, 100)
y_vals = -(N[0]*x_vals + c)/N[1]
plt.plot(x_vals, y_vals, label='Required line', color='blue')

plt.xlabel('x')
plt.ylabel('y')
plt.title('Line generated using matrix method')
plt.grid(True)
plt.legend()
plt.axis('equal')
plt.show()

