import matplotlib.pyplot as plt
from call import send_data
import numpy as np
from numpy.lib import scimath

data , Ax, Ay, Bx, By = send_data()

x = np.linspace(-30, 150, 1000)
y = scimath.sqrt((-data[1]*x)-data[2])

A = np.linspace(-30, 150, 1000)
B = -(scimath.sqrt((-data[1]*A)-data[2]))

X = np.linspace(-100, 150, 20)
Y = X+30

plt.plot(x, y, "-r")
plt.plot(X, Y, "-g")
plt.plot(A, B, "-r")
plt.plot(Ax,Ay, "ko")
plt.text(Ax+0.1, Ay+0.1, f"({Ax:.0f},{Ay:.0f})", color = "black", fontsize = 12)
plt.plot(Bx,By, "ko")
plt.text(Bx+0.1, By+0.1, f"({Bx:.0f},{By:.0f})", color = "black", fontsize = 12)
plt.text(86.3, -115.3, r'$y^2=120(x+30)$', color = "black", fontsize = 12)
plt.text(-92.7, -60, "y=x+30", color = "black", fontsize = 12)

plt.xlabel("X-axis")
plt.ylabel("Y-axis")
plt.grid(True)
plt.axis("equal")
plt.savefig("../figs/plot.png")
plt.show()