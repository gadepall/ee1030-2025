import subprocess
import matplotlib.pyplot as plt

# Compile the C code
subprocess.run(["gcc", "triangle.c", "-o", "triangle"])

# Run the compiled program and capture output
result = subprocess.run(["./triangle"], capture_output=True, text=True)
coords = list(map(int, result.stdout.split()))

# Extract points
A = (coords[0], coords[1])
B = (coords[2], coords[3])
C = (coords[4], coords[5])

# ---- Plot in Python ----
fig, ax = plt.subplots(figsize=(6,6))
ax.plot([A[0],B[0]],[A[1],B[1]],'gray')
ax.plot([B[0],C[0]],[B[1],C[1]],'gray')
ax.plot([C[0],A[0]],[C[1],A[1]],'gray')

ax.scatter(*A,color='green',s=100,marker='*',label="A (3,2)")
ax.scatter(*B,color='red',s=80,label="B (-2,-3)")
ax.scatter(*C,color='blue',s=80,label="C (2,3)")

ax.set_aspect("equal","box")
ax.set_xlim(-6,6)
ax.set_ylim(-6,6)
ax.grid(True,linestyle="--",alpha=0.6)
ax.set_title("Triangle from C output")
ax.legend()
plt.savefig("fig3.1.png")
plt.show()