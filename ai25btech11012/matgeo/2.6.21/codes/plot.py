# Code by Unnathi Garige
# 1.2.18 - Plotting a triangle ABC

import numpy as np
import matplotlib.pyplot as plt

# Function to generate line points
def line_gen(A,B,n=50):
    dim = A.shape[0]
    x_AB = np.zeros((dim,n))
    lam = np.linspace(0,1,n)
    for i in range(n):
        x_AB[:,i] = A + lam[i]*(B-A)
    return x_AB

# Triangle vertices
A = np.array([3,8])
B = np.array([-4,2])
C = np.array([5,1])

# Generate line segments of triangle
xAB = line_gen(A,B)
xBC = line_gen(B,C)
xCA = line_gen(C,A)

# Plot the triangle
plt.plot(xAB[0,:], xAB[1,:], color="red", label='AB')
plt.plot(xBC[0,:], xBC[1,:], color="green", label='BC')
plt.plot(xCA[0,:], xCA[1,:], color="blue", label='CA')

plt.legend()

# Scatter the vertices
coords = np.vstack((A,B,C)).T
plt.scatter(coords[0,:], coords[1,:], color='black')

# Labels
labels = ['A','B','C']
for i, txt in enumerate(labels):
    plt.annotate(txt,
                 (coords[0,i], coords[1,i]),
                 textcoords="offset points",
                 xytext=(-5,10),
                 ha='center')

plt.xlabel("x-axis")
plt.ylabel("y-axis")
plt.title("Triangle ABC")
plt.axis('equal')
plt.grid(True)

# Save and Show
plt.savefig('/Users/unnathi/Documents/ee1030-2025/ai25btech11012/matgeo/2.6.21/figs')
plt.show()

