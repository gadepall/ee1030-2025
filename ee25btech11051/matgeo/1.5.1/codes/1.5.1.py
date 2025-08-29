import numpy as np
import matplotlib.pyplot as plt
import ctypes

def line_gen_num(A,B,num):
  dim = A.shape[0]
  x_AB = np.zeros((dim,num))
  lam_1 = np.linspace(0,1,num)
  for i in range(num):
    temp1 = A + lam_1[i]*(B-A)
    x_AB[:,i]= temp1.T
  return x_AB



# Define 2D points A and B
int y
A = np.array([6, -4])
B = np.array([-2, -7])

#we have to find C

D = np.array([A, B])

k = 1/3

C = (kA + B)/(k+1)

# Generate line points
x_AB = line_gen_num(A, B, 20)

# Plotting

plt.grid()
plt.title('1.5.1')
plt.plot(x_AB[0, :], x_AB[1, :], 'r--', label='Line from A to B')  # 'bo-' = blue dots with lines
plt.plot(A[0], A[1], 'go', label='Point A')  # green dot
plt.annotate('(6,-4)', xy=(A[0],A[1]), fontsize=12)
plt.plot(B[0], B[1], 'go', label='Point B')  # red dot
plt.annotate('(-2,-7)', xy=(B[0],B[1]), fontsize=12)
plt.plot(C[0], C[1], 'bo', label='Intersection Point') #intersection point
plt.legend()
plt.xlabel('X-axis')
plt.ylabel('Y-axis')
plt.axis('equal')
plt.savefig('/home/shreyas/GVV_Assignments/matgeo/figs/fig1.png')

plt.show()

print(C)
