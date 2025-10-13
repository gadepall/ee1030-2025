import numpy as np
import matplotlib.pyplot as plt

# Load points and intersection from solver
data = np.load("rohan_points.npz")
x_line = data['x_line']
y_line = data['y_line']
rohan_age = data['rohan_age']
mother_age = data['mother_age']

# Generate conic points: (x+3)*(y+3)=360 => y = 360/(x+3)-3
x_conic = np.linspace(0.1, 40, 400)  # avoid x=-3
y_conic = 360 / (x_conic + 3) - 3

# Plotting
plt.figure(figsize=(8,6))
plt.plot(x_line, y_line, label="Line: y = x + 26", color='blue')
plt.plot(x_conic, y_conic, label="Conic: (x+3)(y+3)=360", color='red')
plt.scatter(rohan_age, mother_age, color='green', s=100, label=f"Intersection (x={rohan_age}, y={mother_age})")

plt.xlabel("Rohan's age x")
plt.ylabel("Mother's age y")
plt.title("Rohan's Age Problem - Line and Conic Intersection")
plt.grid(True)
plt.legend()
plt.show()

