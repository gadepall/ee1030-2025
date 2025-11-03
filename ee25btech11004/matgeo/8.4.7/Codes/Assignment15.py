import matplotlib.pyplot as plt
import numpy as np

fig = plt.figure(figsize = (6,6))
ax = fig.add_subplot(111)

X = np.linspace(-10,10,50)

p1 = X*X/8

p2 = X*X/2
l = np.zeros(50) - 2

ax.plot(X,p1, label = '$x^2 = 8y$', color = 'green')
ax.plot(X,p2, label = '$x^2 = 2y$', color = 'red')
ax.plot(X,l, label = '$y=-2$', color = 'orange')

ax.scatter(4,2, label='(4,2)')
ax.scatter(1,0.5,label='(1,0.5)')
ax.scatter(8,8, label='(8,8)')
ax.scatter(2,2,label='(2,2)')
ax.scatter(0,0, color = 'black')

set1 = np.array([[4,2],
                 [1,0.5],
                 [0,0]])
set2 = np.array([[8,8],
                 [2,2],
                 [0,0]])

ax.plot(set1[:,0],set1[:,1])
ax.plot(set2[:,0],set2[:,1])

ax.grid(True)
ax.legend()
plt.show()
plt.show()
