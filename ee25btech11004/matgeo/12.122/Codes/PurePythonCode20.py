import matplotlib.pyplot as plt
import numpy as np
import math

theta = int(input("Input the angle."))
string = input("Input the vector as x y z")

theta = theta*3.14/180

rotation = np.array([[math.cos(theta), -math.sin(theta), 0],
                     [math.sin(theta), math.cos(theta), 0],
                     [0,0,1]])

string.strip()
x,y,z= string.split(" ")


vector = np.array([int(x), int(y), int(z)])

rotated = np.linalg.matmul(rotation,vector)

rotated[0] = round(rotated[0],2)
rotated[1] = round(rotated[1],2)
rotated[2] = round(rotated[2],2)

fig = plt.figure(figsize = (6,6))
ax = fig.add_subplot(111, projection='3d')


ax.scatter(vector[0], vector[1], vector[2], label = f'({vector[0]},{vector[1]},{vector[2]})')
ax.scatter(rotated[0], rotated[1], rotated[2], label = f'({rotated[0]},{rotated[1]},{rotated[2]})')

ax.grid(True)
ax.legend()
plt.show()
