import matplotlib.pyplot as plt
from call import send_data
import numpy as np

data, Ax, Ay, Bx, By = send_data()

x = np.linspace(-3.010, 3.010, 2500)
y = np.sqrt(145/9-(16*x**2)/9)

Xt = np.linspace(-5, 5, 100)
Yt = (145/27) * (1 - (32/145)*Xt)

Xn = np.linspace(-5, 5, 100)
Yn = (54/64) * (Xn - 2) + 3

plt.plot(x, y, "r")
plt.plot(x, -y, "r")
plt.plot(Xt, Yt, "g")
plt.plot(Xn, Yn, "b--")

plt.plot(2, 3, "ko")
plt.text(2.1, 3.1, "(2,3)", color="black")
plt.text(2.36, -2.77, r'$16x^2+9y^2=145$', color = "black")
plt.text(-3.04, 9.18, r'$32x+27y=145$', color="black")
plt.text(4.35,4.95,r'$-27x+32y=42$', color="black")

plt.xlabel("X-axis")
plt.ylabel("Y-axis")
plt.axis("equal")
plt.grid(True)
plt.savefig("../figs/plot.png")
plt.show()
