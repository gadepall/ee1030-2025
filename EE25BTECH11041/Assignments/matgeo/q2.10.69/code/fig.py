import numpy as np
import matplotlib.pyplot as plt

plt.figure(figsize=(8, 6), dpi=100)  

def quad(c,x):
    return c*x**2-6*c*x-12


x=np.linspace(-15,15,500)
c_valid=-1
y = quad(c_valid, x)
plt.plot(x,y, ':b', label="Graph for valid c")

x=np.linspace(-15,15,500)
c_wrong=-2
y=quad(c_wrong, x)
plt.plot(x,y, ':r', label="Graph for wrong c")

plt.legend()
plt.title("Graph of the Quadratic equation for different values of c")
plt.grid()
plt.xlim(-5, 10)
plt.ylim(-20, 20)
plt.savefig('figure.png', dpi=300, bbox_inches='tight')
plt.show()
