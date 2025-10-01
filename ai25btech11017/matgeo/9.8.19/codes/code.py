# Code by GVV Sharma (modified & corrected)
# Released under GNU GPL

import sys
sys.path.insert(0, '/sdcard/github/matgeo/codes/CoordGeo')  # path to scripts
import numpy as np
import numpy.linalg as LA
import matplotlib.pyplot as plt

# Local import
from conics.funcs import circ_gen

# Circle 1: x^2 + y^2 = 6
O1 = np.array(([0,0])).reshape(-1,1)
r1 = np.sqrt(6)

# Circle 2: (x-3)^2 + y^2 = 1
O2 = np.array(([3,0])).reshape(-1,1)
r2 = 1

# Generate circles
C1 = circ_gen(O1,r1)
C2 = circ_gen(O2,r2)

# ---- Intersection points ----
# From equations: x^2 + y^2 = 6  and  (x-3)^2 + y^2 = 1
x_val = 7/3
y_vals = [np.sqrt(5)/3, -np.sqrt(5)/3]   # corrected values

P1 = np.array(([x_val, y_vals[0]])).reshape(-1,1)
P2 = np.array(([x_val, y_vals[1]])).reshape(-1,1)

print("Intersection points:", P1.T, P2.T)

# ---- Circle through P1, P2 and Q=(1,1) ----
Q = np.array(([1,1])).reshape(-1,1)

# Solve for general circle: x^2 + y^2 + 2ux + 2vy + f = 0
A = np.block([[2*P1.T],
              [2*P2.T],
              [2*Q.T]])
b = -np.array([[LA.norm(P1)**2],
               [LA.norm(P2)**2],
               [LA.norm(Q)**2]])
sol = LA.lstsq(A,b,rcond=None)[0]   # [u,v,f]

u,v,f = sol.flatten()
O3 = -np.array(([u,v])).reshape(-1,1)
r3 = np.sqrt(LA.norm(O3)**2 - f)

C3 = circ_gen(O3,r3)

# ---- Plotting ----
plt.plot(C1[0,:], C1[1,:], label='$C_1: x^2+y^2=6$')
plt.plot(C2[0,:], C2[1,:], label='$C_2: (x-3)^2+y^2=1$')
plt.plot(C3[0,:], C3[1,:], label='$C_3$ through P1,P2,(1,1)$')

# Plot centers
plt.scatter(O1[0],O1[1],color='blue')
plt.scatter(O2[0],O2[1],color='blue')
plt.scatter(O3[0],O3[1],color='blue')

# Plot intersection points + Q
plt.scatter([P1[0,0],P2[0,0],Q[0,0]],
            [P1[1,0],P2[1,0],Q[1,0]],
            color='red')
for pt,label in zip([P1,P2,Q],['P1','P2','Q']):
    plt.annotate(f'{label}\n({pt[0,0]:.2f},{pt[1,0]:.2f})',
                 (pt[0,0],pt[1,0]),
                 textcoords="offset points",
                 xytext=(0,10),ha='center')

# Axes
ax = plt.gca()
ax.spines['top'].set_color('none')
ax.spines['right'].set_color('none')
ax.spines['left'].set_position('zero')
ax.spines['bottom'].set_position('zero')

plt.axis('equal')
plt.legend()
plt.grid(True)

# If using termux
# import subprocess, shlex
# plt.savefig('chapters/11/11/1/11/figs/fig.pdf')
# subprocess.run(shlex.split("termux-open chapters/11/11/1/11/figs/fig.pdf"))
# else
plt.show()
