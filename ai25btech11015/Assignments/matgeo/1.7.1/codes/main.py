#  The value of m which makes 
# the points (0,0), (2m,−4), and (3,6) collinear, is

import numpy as np 
import matplotlib.pyplot as plt

m = -1 

pt1 = np.array([0,0]).reshape(-1,1)
pt2 = np.array([2*m,-4]).reshape(-1,1)
pt3 = np.array([3,6]).reshape(-1,1)

#checking if m = -1 satisfies the collinearity condition
rank = np.linalg.matrix_rank(np.hstack((pt2-pt1,pt3-pt1)))
if rank == 1:
    print("The points are collinear")
else:
    print("The points are not collinear")
    
pts = np.array([pt1,pt2,pt3])
print(pts[:,0])
plt.plot(pts[:,0],pts[:,1])
plt.scatter(pts[:,0],pts[:,1])

plt.text(pt1[0],pt1[1],"A")
plt.text(pt2[0],pt2[1],"B")
plt.text(pt3[0],pt3[1],"C")


plt.axhline(0, color='black')   # x-axis
plt.axvline(0, color='black')   # y-axis
plt.xlabel("x")
plt.ylabel("y")
plt.grid(True)
plt.axis("equal")
# plt.legend(loc="best")


plt.savefig('../figs/fig.png', dpi=300)
