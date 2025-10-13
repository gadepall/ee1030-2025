import numpy as np
import sympy as sp
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# Symbolic setup
λ = sp.symbols('λ')
M = sp.Matrix([[2-λ, -2, 1],
               [2, -3-λ, 2],
               [-1, 2, -λ]])

# Characteristic polynomial and eigenvalues
charpoly = sp.factor(sp.simplify(sp.expand(M.det())))
eigs = sp.solve(sp.Eq(M.det(),0), λ)
eigs_simpl = [sp.simplify(e) for e in eigs]

print("Characteristic polynomial:", charpoly)
print("Eigenvalues (λ with non-trivial solutions):", eigs_simpl)

# Prepare plot
fig = plt.figure(figsize=(9,6))
ax = fig.add_subplot(111, projection='3d')
ax.set_xlabel('x1')
ax.set_ylabel('x2')
ax.set_zlabel('x3')
ax.set_title('Nullspace basis vectors for λ giving non-trivial solutions')

origin = np.array([0,0,0])

for val in eigs_simpl:
    val_num = float(val)
    Mat_num = sp.Matrix([[2-val, -2, 1],
                         [2, -3-val, 2],
                         [-1, 2, -val]])
    null_basis = Mat_num.nullspace()
    basis_np = []
    for v in null_basis:
        arr = np.array([float(sp.nsimplify(x)) for x in v]).astype(float)
        basis_np.append(arr)
    print(f"\nλ = {val_num}: nullspace basis (sympy):", null_basis)
    for b in basis_np:
        ax.quiver(origin[0], origin[1], origin[2],
                  b[0], b[1], b[2],
                  length=1.0, normalize=True, linewidth=2)
        ax.scatter([b[0]],[b[1]],[b[2]], label=f"λ={val_num} basis")

# set axis limits for visibility
ax.set_xlim([-1,1])
ax.set_ylim([-1,1])
ax.set_zlim([-1,1])

plt.legend()
plt.show()
