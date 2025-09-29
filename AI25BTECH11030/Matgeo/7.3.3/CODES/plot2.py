import ctypes
import numpy as np
import matplotlib.pyplot as plt

# Load the shared library (ensure libmatfun.so is in the same directory)
matfun = ctypes.CDLL('./libmatfun.so')

# Declare return types
matfun.compute_cos_theta.restype        = ctypes.c_double
matfun.compute_coefficient_sq.restype   = ctypes.c_double
matfun.compute_r_squared_coeff.restype  = ctypes.c_double

# 1. Compute required values via the .so functions
cos_theta      = matfun.compute_cos_theta()        # cos(2π/3)
coeff_sq       = matfun.compute_coefficient_sq()   # (cosθ - 1)^2
r2_coeff       = matfun.compute_r_squared_coeff()  # r²/a² = 4

# 2. Print final answer
print(f"Answer: (c) x² + y² = {int(r2_coeff)}a²")

# 3. For plotting set a = 1
a = 1.0
r = np.sqrt(r2_coeff * a**2)

# Compute triangle vertices
theta = 2 * np.pi / 3
A = np.array([r, 0.0])
B = np.array([r * np.cos(theta),  r * np.sin(theta)])
C = np.array([r * np.cos(theta), -r * np.sin(theta)])
M = (B + C) / 2.0  # midpoint

# 4. Plot
plt.figure(figsize=(8,8))

# Circle
t = np.linspace(0, 2*np.pi, 200)
plt.plot(r*np.cos(t), r*np.sin(t), 'b-', lw=2, label=f'Circle: x²+y²={int(r2_coeff)}a²')

# Triangle
plt.plot([A[0],B[0],C[0],A[0]], [A[1],B[1],C[1],A[1]],
         'r-', lw=2, label='Equilateral Triangle')

# Median
plt.plot([A[0],M[0]], [A[1],M[1]], 'g--', lw=2, label='Median=3a')

# Points and labels
plt.plot(0,0,'ko');  plt.text(0.05,0.05, 'O(0,0)')
plt.plot(A[0],A[1],'ro'); plt.text(A[0]+0.1,A[1]+0.1, 'A(2,0)')
plt.plot(B[0],B[1],'ro'); plt.text(B[0]-0.4,B[1]+0.1, 'B(-1,√3)')
plt.plot(C[0],C[1],'ro'); plt.text(C[0]-0.4,C[1]-0.2, 'C(-1,-√3)')
plt.plot(M[0],M[1],'go'); plt.text(M[0]+0.1,M[1]+0.1, 'M')

plt.axis('equal')
plt.xlim(-3,3); plt.ylim(-3,3)
plt.grid(alpha=0.3)
plt.xlabel('x'); plt.ylabel('y')
plt.title('Circle + Equilateral Triangle (Median=3a)')
plt.legend()
plt.tight_layout()
plt.show()
