import numpy as np
import matplotlib.pyplot as plt

# Given points (from solution and problem statement)
P = np.array([-200, 0])
Q = np.array([200, 0])
A = np.array([200, 800])
O = np.array([0, 0])

# Step 1: Vector from P to Q
X = Q - P  # [400, 0]

# Step 2: Rotate X by 90 degrees anticlockwise to get Y (QR)
Y = np.array([0 - X[1], X[0]])  # [0, 400]

# Step 3: Find R and S using vector addition as in PDF
R = Q + Y     # [200, 400]
S = P + Y     # [-200, 400]

# Step 4: Area and diagonal of the square
side = np.linalg.norm(X)         # 400
area = side ** 2                 # 160000
diagonal = side * np.sqrt(2)     # 400*sqrt(2) ≈ 565.69

# Step 5: Find C as in PDF by solving with collinearity (x-axis, so y=0)
# Using determinant as in PDF: |A-Q| |C-Q| = 0 for being collinear with Q as origin
# But given in PDF as C = (-600, 0)
C = np.array([-600, 0])

# Step 6: Find K for S dividing CA in K:1, S = (K*A + C)/(K+1)
# Solve for K using y-coordinates
S_y = S[1]
K = (S_y - C[1]) / (A[1] - S_y)

# ---- Plot as in the PDF ----
plt.figure(figsize=(9,9))
# Triangle AQC (A->Q->C->A)
triangle_x = [A[0], Q[0], C[0], A[0]]
triangle_y = [A[1], Q[1], C[1], A[1]]
plt.plot(triangle_x, triangle_y, 'k-', label='Triangle AQC', linewidth=2)

# Square PQRS
square_x = [P[0], Q[0], R[0], S[0], P[0]]
square_y = [P[1], Q[1], R[1], S[1], P[1]]
plt.plot(square_x, square_y, 'b-', label='Square PQRS', linewidth=2)

# Points O, P, Q, A, R, S, C
pts = [O, P, Q, A, R, S, C]
lbls = ['O', 'P', 'Q', 'A', 'R', 'S', 'C']
for pt, name in zip(pts, lbls):
    plt.scatter(pt[0], pt[1], color='red')
    plt.text(pt[0]+10, pt[1]+20, name, fontsize=13)

# Diagonal PR
plt.plot([P[0], R[0]], [P[1], R[1]], 'r--', label='Diagonal PR')

# Area, Diagonal annotations
plt.text(-350, 200, f'Area = {area:.0f}', fontsize=13, color='blue', bbox=dict(facecolor='white', alpha=0.7))
plt.text(-350, 120, f'Diagonal = {diagonal:.2f}', fontsize=13, color='purple', bbox=dict(facecolor='white', alpha=0.7))

plt.xlabel('x')
plt.ylabel('y')
plt.xlim(-700, 300)
plt.ylim(-100, 900)
plt.grid(True)
plt.legend()
plt.title('Triangle AQC & Square PQRS ')
plt.tight_layout()
plt.show()

# For verification
print("Coordinates of R:", tuple(R))
print("Coordinates of S:", tuple(S))
print("Area of PQRS:", area)
print("Length of diagonal PR:", diagonal)
print("Coordinates of C:", tuple(C))
print("Value of K:", K)

