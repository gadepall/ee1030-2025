import numpy as np
import matplotlib.pyplot as plt

# Define values for a and b
a = 1  # Example value
b = 0  # Example value

# Define points as NumPy arrays
P = np.array([2*a, -3*b])  # Point P
Q = np.array([a, b])       # Point Q

# Ratio m:n
m = 3
n = 1

# Section formula for internal division
R = (m * Q + n * P) / (m + n)

# Print the result
print("Position vector of the point R:", R)

# Plotting
plt.figure(figsize=(6, 6))
plt.axhline(0, color='black', linewidth=0.8)
plt.axvline(0, color='black', linewidth=0.8)

# Plot P, Q, and R
plt.scatter(*P, color='blue', label='P (2a, -3b)')
plt.scatter(*Q, color='green', label='Q (a, b)')
plt.scatter(*R, color='red', label=f'R (ratio {m}:{n})')

# Draw line between P and Q
plt.plot([P[0], Q[0]], [P[1], Q[1]], color='gray', linestyle='--')

# Annotate points
plt.text(P[0]+0.2, P[1]+0.2, 'P')
plt.text(Q[0]+0.2, Q[1]+0.2, 'Q')
plt.text(R[0]+0.2, R[1]+0.2, 'R')

plt.xlabel('X-axis')
plt.ylabel('Y-axis')
plt.title('Section Formula Visualization')
plt.legend()
plt.grid(True)
plt.savefig("/home/arsh-dhoke/ee1030-2025/ee25btech11010/matgeo/1.4.26/figs/q1.png")
plt.show()
