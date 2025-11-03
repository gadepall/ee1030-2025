import numpy as np
import matplotlib.pyplot as plt

plt.figure(figsize=(6,6), dpi=200)

x1= np.linspace(-6,6,100)
y1=(x1+4)/2

x2= np.linspace(-6,6,100)
y2=(4*x2+2)/3

bx=np.linspace(-6,6,100)
by=(1.39-0.35*bx)/0.29

plt.plot(x1,y1, color='orange', label="line 1")
plt.plot(x2,y2, color='blue', label="line 2")
plt.plot(bx,by,':', color='green', label="Bisector 1")
plt.legend()
plt.grid()
plt.savefig("figure.png", dpi=250)
plt.show()
