import sys

import numpy as np

import numpy.linalg as LA
import matplotlib.pyplot as plt
import matplotlib.image as mpimg



P = np.array([1,2,-1]).reshape(-1,1)

Q = np.array([-1,1,1]).reshape(-1,1)

ratio = 2

R = (ratio*Q + P) / (ratio + 1)

S = (ratio*Q - P) / (ratio - 1)

x_PQ = np.block([P,Q,R,S])

fig = plt.figure(figsize=(8, 6))
ax = fig.add_subplot(111, projection='3d')


#Plotting all lines
ax.plot(x_PQ[0,:],x_PQ[1,:], x_PQ[2,:],label='$BC$')




# Scatter plot # 
all_coords = np.block([P, Q, R, S])  # Stack A, B, C vertically
ax.scatter(all_coords[0, :],all_coords[1, :],all_coords[2, :])
vert_labels = ['P', 'Q', 'R', 'S']

for i, txt in enumerate(vert_labels):
    # Annotate each point with its label and coordinates
    ax.text(all_coords[0, i], all_coords[1, i], all_coords[2, i], f'{txt}\n({all_coords[0, i]:.0f}, {all_coords[1, i]:.0f}, {all_coords[2, i]:.0f})',
             fontsize=12, ha='center', va='bottom')

ax.spines['top'].set_color('none')
ax.spines['left'].set_position('zero')
ax.spines['right'].set_color('none')
ax.spines['bottom'].set_position('zero')


plt.grid() # minor
plt.axis('equal')


plt.show()