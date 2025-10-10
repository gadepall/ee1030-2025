import numpy as np
import matplotlib.pyplot as plt

# Points (convert to numpy int to ensure matrix ops but cast for display)
A = np.array([-5, 6])
B = np.array([-4, -2])
C = np.array([7, 5])

# Matrix difference and squared distance
def dist2(P, Q):
    diff = P - Q
    return diff @ diff   # dot product

# Distances squared
AB2 = dist2(A, B)
BC2 = dist2(B, C)
CA2 = dist2(C, A)

# Determine type
triangle_type = []
if np.isclose(AB2, BC2) or np.isclose(BC2, CA2) or np.isclose(CA2, AB2):
    triangle_type.append("Isosceles")
else:
    triangle_type.append("Scalene")

if (np.isclose(AB2 + BC2, CA2) or 
    np.isclose(BC2 + CA2, AB2) or 
    np.isclose(CA2 + AB2, BC2)):
    triangle_type.append("Right-angled")

triangle_type = " ".join(triangle_type)

print(f"AB^2 = {AB2}, BC^2 = {BC2}, CA^2 = {CA2}")
print(f"The triangle is {triangle_type}.")

# ---- Plotting ----
X = [A[0], B[0], C[0], A[0]]
Y = [A[1], B[1], C[1], A[1]]

plt.figure(figsize=(7,7))
plt.plot(X, Y, 'b-o', linewidth=2)

# Annotate points with pure int coordinates
plt.text(A[0], A[1], f"A({int(A[0])},{int(A[1])})", fontsize=12, color='red', ha='right')
plt.text(B[0], B[1], f"B({int(B[0])},{int(B[1])})", fontsize=12, color='red', ha='right')
plt.text(C[0], C[1], f"C({int(C[0])},{int(C[1])})", fontsize=12, color='red', ha='left')

# Show triangle type inside the plot
plt.text((A[0]+B[0]+C[0])/3, (A[1]+B[1]+C[1])/3, 
         f"{triangle_type} Triangle", 
         fontsize=14, color='green', ha='center', 
         bbox=dict(facecolor='yellow', alpha=0.3, edgecolor='black'))

plt.grid(True, linestyle="--", alpha=0.6)
plt.axis("equal")
plt.title("Triangle ABC with Coordinates and Type", fontsize=14)
plt.xlabel("X-axis")
plt.ylabel("Y-axis")
plt.show()
