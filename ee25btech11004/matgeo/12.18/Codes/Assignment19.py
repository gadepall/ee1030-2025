import matplotlib.pyplot as plt
import numpy as np
import math
import ctypes


c_lib = ctypes.CDLL('./19c.so')

c_lib.norm.argtypes = [ctypes.c_float, ctypes.c_float, ctypes.c_float, ctypes.c_float]
c_lib.norm.restype = ctypes.c_float

distance = c_lib.matmul(
    ctypes.c_float(0),
    ctypes.c_float(0), 
    ctypes.c_float(-math.sqrt(2)),
    ctypes.c_float(-1)
)

fig = plt.figure(figsize = (8,8))
ax = fig.add_subplot(111)

line = np.array([[0,0],
                 [-math.sqrt(2),-1]])

plt.scatter(0,0,label='X(0,0)')
plt.scatter(-math.sqrt(2)/2,-math.sqrt(2)/2,label='Y($-\sqrt{2}/2$, $-\sqrt{2}/2$)')
plt.scatter(-math.sqrt(2),0,label='Z($-\sqrt{2}$,0)')
plt.scatter(-1-math.sqrt(2),0,label='W($-1-\sqrt{2}$,0)')
plt.scatter(-1-math.sqrt(2),-1,label='P($-1-\sqrt{2}$,-1)')
plt.scatter(-math.sqrt(2),-1,label='Q($-\sqrt{2}$,-1)')
ax.plot(line[:,0], line[:,1], label = 'XQ')

plt.grid(linestyle='--', linewidth=0.7, alpha=0.6)
ax.legend()
plt.show()



list =["X is (0,0)"]

def rotationmatrix(x1,y1,theta,X):
    X = str(X)
    theta = theta*3.1415/180
    matrix = np.array([[math.cos(theta),-math.sin(theta)],
              [math.sin(theta),math.cos(theta)]])
    vector = np.array([x1,y1])
    newvector = vector + np.linalg.matmul(matrix,np.array([1,0]))
    list.append(f"{X} is ({newvector[0]}, {newvector[1]})")


answer = input("Type the previous vector, the angle, and the name of the vector you want to calculate")
while(answer!= "X"):
    answer.strip()
    x1,y1,theta,X = answer.split(" ")
    x1 = float(x1)
    y1 = float(y1)
    theta = int(theta)
    rotationmatrix(x1,y1,theta,X)
    answer = input("Type the previous vector, the angle, and the name of the vector you want to calculate")
    

for i in range(len(list)):
    print(list[i])


print(f"The distance between X and Q is {distance}")

