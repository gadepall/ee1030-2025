import matplotlib.pyplot as plt
import numpy as np
from call import send_data

data, findata = send_data()

a = np.linspace(-10, 10, 100)
b = ((data[0]*a)-data[2])/(-data[1])

A = np.linspace(-10, 10, 100)
B = ((-data[3]*A)+data[5])/data[4]

y = np.linspace(-10, 10, 100)
x = ((findata[4]*y)-findata[5])/(-findata[3])

X = np.linspace(-10, 10, 100)
Y = ((findata[0]*X)-findata[2])/(-findata[1])

plt.plot(a, b, 'r-') 
plt.plot(A, B, 'r-')
plt.plot(x, y, 'k-')
plt.plot(X, Y, 'k-')

plt.text(10, 12.3, "3x-2y=5", fontsize=10, color='black')
plt.text(-8.3, 15, "3x+2y=5", fontsize=10, color='black')
plt.text(15.2, -0.06, "y=0", fontsize=10, color='black')
plt.text(1.6, 14.6, "x=10/6", fontsize=10, color='black')


plt.xlabel('X-axis')
plt.ylabel('Y-axis')
plt.axis('equal')
plt.grid(True)
plt.savefig("../figs/plot.png")
plt.show()