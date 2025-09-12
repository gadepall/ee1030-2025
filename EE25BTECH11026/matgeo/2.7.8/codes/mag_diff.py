import ctypes
import matplotlib as mp
mp.use("TkAgg")
import matplotlib.pyplot as plt

lib = ctypes.CDLL('./libdiff.so')

lib.find_mag_diffvector.argtypes = [ctypes.c_double, ctypes.c_double, ctypes.c_double]
lib.find_mag_diffvector.restype = ctypes.c_double

a = 2.0
b = 3.0
dot = 4.0

diff = lib.find_mag_diffvector(a, b, dot)
print(f"The magnitude of difference vector of a and b is: {diff:.4f}")

#taking an example of vectors a and b to prove computationally
A=(2.0,0)
B=(0,3.0)

# Plotting
plt.figure()
plt.quiver(0, 0, A[0], A[1], angles='xy', scale_units='xy', scale=1, color='r', label='a')
plt.quiver(0, 0, B[0], B[1], angles='xy', scale_units='xy', scale=1, color='b', label='b')
plt.quiver(B[0], B[1], A[0]-B[0], A[1]-B[1],
           angles='xy', scale_units='xy', scale=1, color='g', label='a-b')

#Annotate magnitudes
plt.text((A[0]+B[0])/2, (A[1]+B[1])/2, f"|a-b|={diff:.4f}", color='g', fontsize=10, ha='center', va='bottom')

plt.xlim(-1, 5)
plt.ylim(-1, 5)
plt.gca().set_aspect('equal', adjustable='box')
plt.grid()
plt.legend()
plt.title("Magnitude of vector difference: a - b")
plt.savefig("/home/user/Matrix/Matgeo_assignments/2.7.8/figs/Figure_1.png")
plt.show()



