import numpy as np
import matplotlib as mp
mp.use("TkAgg") 
import matplotlib.pyplot as plt

def cross_via_row_reduction(a, b):
     A = np.array([a, b], dtype=float)   # 2x3 system
    
    # Row reduction manually
    # Step 1: make pivot in first column
     if A[0,0] == 0:
         A[[0,1]] = A[[1,0]]   # swap rows if needed
    
    # Eliminate below
     factor = A[1,0] / A[0,0]
     A[1] = A[1] - factor*A[0]
    
    # Now we have 2 equations in 3 variables => free variable (say x3 = t)
    # Solve system Ax=0
    # Extract coefficients
     eq1 = A[0]
     eq2 = A[1]
    
    # Free variable x3 = t
     t = 1  # choose t=1 for direction
    
    # Solve eq2 for x2 in terms of t
     if abs(eq2[1]) > 1e-12:
        x2 = -(eq2[2]/eq2[1])*t
     else:
        x2 = 0
    
    # Solve eq1 for x1
     x1 = -(eq1[1]*x2 + eq1[2]*t) / eq1[0]
    
     return np.array([x1, x2, t])

# Given vectors
a = np.array([2, 1, 2], dtype=np.int32)
b = np.array([0, 1, 1], dtype=np.int32)

x = cross_via_row_reduction(a, b)
print("Cross product :", x)

mag = np.linalg.norm(x)

u=x/mag

print("Unit vector perpendicular to vectors a and b is \u00B1 [" + ", ".join(f"{val:.2f}" for val in u) + "]")
print("That is,")
print("+u =", [format(val, ".2f") for val in u])
print("-u =", [format(val, ".2f") for val in -u])



# --- Plotting ---
fig = plt.figure(figsize=(8,8))
ax = fig.add_subplot(111, projection='3d')

# Origin
origin = np.zeros(3)

# Plot a, b, and cross product
ax.quiver(*origin, *a, color='r', label='a', arrow_length_ratio=0.1)
ax.quiver(*origin, *b, color='g', label='b', arrow_length_ratio=0.1)
ax.quiver(*origin, *-u, color='b', label='-(a × b)', arrow_length_ratio=0.1)
ax.quiver(*origin, *u, color='c', label='(a × b)' , arrow_length_ratio=0.1) 

ax.set_xlim([min(a[0], b[0], u[0], -u[0], 0),
             max(a[0], b[0], u[0], -u[0], 0)])

ax.set_ylim([min(a[1], b[1], u[1], -u[1], 0),
             max(a[1], b[1], u[1], -u[1], 0)])

ax.set_zlim([min(a[2], b[2], u[2], -u[2], 0),
             max(a[2], b[2], u[2], -u[2], 0)])


ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Z')
ax.legend()
plt.savefig("/home/user/Matrix/Matgeo_assignments/2.4.21/figs/Figure_1.png")
plt.show()

