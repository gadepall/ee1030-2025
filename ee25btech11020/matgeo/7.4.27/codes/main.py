import ctypes
import numpy as np
import matplotlib.pyplot as plt

lib = ctypes.CDLL("./solve_angle.so")
lib.solve_angle.restype = ctypes.c_double
lib.solve_angle.argtypes = [ctypes.c_double, ctypes.c_double,
                            ctypes.c_double, ctypes.c_double]

Q = np.array([3, 4])
R = np.array([-4, 3])
O = np.array([0, 0])
P = np.array([5, 0])   # choose a point on the circle

angle = lib.solve_angle(Q[0], Q[1], R[0], R[1])
print("Angle QPR (radians) =", angle)

theta = np.linspace(0, 2*np.pi, 500)
x = 5*np.cos(theta)
y = 5*np.sin(theta)

fig, ax = plt.subplots()
ax.plot(x, y, 'b')  # circle

ax.plot(Q[0], Q[1], 'ro')
ax.text(Q[0]+0.2, Q[1]+0.2, 'Q', fontsize=10)

ax.plot(R[0], R[1], 'ro')
ax.text(R[0]+0.2, R[1]+0.2, 'R', fontsize=10)

ax.plot(O[0], O[1], 'ko')
ax.text(O[0]+0.2, O[1]-0.3, 'O', fontsize=10)

ax.plot(P[0], P[1], 'go')
ax.text(P[0]+0.2, P[1]-0.3, 'P', fontsize=10)

ax.plot([Q[0],R[0]],[Q[1],R[1]],'r--')   # chord QR
ax.plot([O[0],Q[0]],[O[1],Q[1]],'k--')   # radius OQ
ax.plot([O[0],R[0]],[O[1],R[1]],'k--')   # radius OR
ax.plot([P[0],Q[0]],[P[1],Q[1]],'g-')    # PQ
ax.plot([P[0],R[0]],[P[1],R[1]],'g-')    # PR

ax.set_aspect('equal')
ax.set_xlim(-6,6)
ax.set_ylim(-6,6)

plt.savefig("../figs/img1.png", dpi=300)
plt.close()

