#code by Unnathi Garige
#1.2.18 represents graphically a parallelogram

import sys
sys.path.insert(0, '/Users/unnathi/Documents/ee1030-2025/ai25btech11012/matgeo/1.2.18/codes') 
import numpy as np
import matplotlib.pyplot as plt
import math

import subprocess
import shlex


# Function to generate line points
def line_gen(A,B,n=50):
    dim = A.shape[0]
    x_AB = np.zeros((dim,n))
    lam = np.linspace(0,1,n)
    for i in range(n):
        x_AB[:,i] = A + lam[i]*(B-A)
    return x_AB


data = np.loadtxt("values.dat", skiprows=1)  

xc = data[0]
yc = data[1]



A = np.array([6,1])
B = np.array([8,2])
C = np.array([9,4])
D = np.array(([xc,yc]))

# Generate line segments of parallelogram
xAB = line_gen(A,B)
xBC = line_gen(B,C)
xCD = line_gen(C,D)
xDA = line_gen(D,A)

# Plot the parallelogram
plt.plot(xAB[0,:], xAB[1,:], color="red", label='AB')   # Red
plt.plot(xBC[0,:], xBC[1,:], color="green", label='BC')   # Green
plt.plot(xCD[0,:], xCD[1,:], color="blue", label='CD')   # Blue
plt.plot(xDA[0,:], xDA[1,:], color="magenta", label='DA')   # Magenta

plt.legend()


# Scatter the vertices
coords = np.vstack((A,B,C,D)).T
plt.scatter(coords[0,:], coords[1,:], color='red')

# Labels
labels = ['A','B','C','D']
for i, txt in enumerate(labels):
    plt.annotate(txt, (coords[0,i], coords[1,i]),
                 textcoords="offset points",
                 xytext=(-5,10),
                 ha='center')

plt.xlabel("x-axis")
plt.ylabel("y-axis")
plt.title("Parallelogram ABCD")
plt.axis('equal')
plt.grid(True)

# Save and Show
plt.savefig('/Users/unnathi/Documents/ee1030-2025/ai25btech11012/matgeo/1.2.18/figs/fig.png')

plt.show()


