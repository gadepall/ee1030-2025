import math
import sys
sys.path.insert(0, '/home/kartik-lahoti/matgeo/codes/CoordGeo')
import numpy as np
import numpy.linalg as LA
import matplotlib.pyplot as plt
import matplotlib.image as mpimg

from conics.funcs import *

def intersect_hyperbola_circle(c, r):
    """
    Find intersection points of xy = c^2 and x^2 + y^2 = r^2
    """
    # Coefficients for quadratic in X = x^2
    # X^2 - r^2*X + c^4 = 0
    coeffs = [1, -r**2, c**4]
    roots = np.roots(coeffs)

    points = []
    for X in roots:
        if np.isreal(X) and X >= 0:   # valid x^2
            x_vals = [np.sqrt(X).real, -np.sqrt(X).real]
            for x in x_vals:
                if x != 0:  # avoid division by zero
                    y = c**2 / x
                    points.append((x, y))
    return points

lt = intersect_hyperbola_circle(1,3)
inter1 = np.array([lt[0][0] , lt[0][1]]).reshape(-1,1)
inter2 = np.array([lt[1][0] , lt[1][1]]).reshape(-1,1)
inter3 = np.array([lt[2][0] , lt[2][1]]).reshape(-1,1)
inter4 = np.array([lt[3][0] , lt[3][1]]).reshape(-1,1)
prod = lt[0][0] * lt[1][0] * lt[2][0] * lt[3][0] 
print('m_1m_2m_3m_4 = ',prod)
# xy = c^2 
y_n = np.linspace(-30, -0.1 , 400)
y_n = y_n[y_n!=0]
x_n = 1**2/y_n 
 
y_p = np.linspace(0.1, 30 , 400)
y_p = y_p[y_p!=0]
x_p = 1**2/y_p 

plt.figure()
plt.plot(x_p,y_p,"r-",label="Rectangular Hyperbola")
plt.plot(x_n,y_n,"r-")
O = np.zeros(2,dtype=np.float64).reshape(-1,1)
x_circ = circ_gen(O,3)
plt.plot(x_circ[0,:],x_circ[1,:],"blue",label="Circle")

coords = np.block([[inter1,inter2,inter3,inter4]])
plt.scatter(coords[0,:],coords[1,:])
vert_labels = [r'$m_1$',r'$m_2$',r'$m_3$',r'$m_4$']

for i, txt in enumerate(vert_labels):
    plt.annotate(f'({txt},1/{txt})',
                 (coords[0,i], coords[1,i]),
                 textcoords="offset points",
                 xytext=(10,-15),
                 ha='center')

plt.xlabel('$x$')
plt.ylabel('$y$')

plt.legend(loc='best')
plt.grid() # minor
plt.axis('equal')
plt.xlim([-10/2,10/2])
plt.ylim([-10/2,10/2])
plt.title("7.4.39")
plt.axhline(0, color='black', linewidth=0.7)
plt.axvline(0, color='black', linewidth=0.7)
plt.savefig("../figs/graph2.png")
plt.show()
