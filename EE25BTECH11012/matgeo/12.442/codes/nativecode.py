import numpy as np
import matplotlib.pyplot as plt

# Define the matrix
A = np.array([[5, 3], 
              [1, 4]])

# Calculate the eigenvalues using numpy for verification
eigenvalues = np.linalg.eigvals(A)
# Sort for consistent plotting
eigenvalues = np.sort(eigenvalues) 

print(f"Calculated Eigenvalues: {eigenvalues}")

# Define the characteristic polynomial: lambda^2 - 9*lambda + 17
def characteristic_polynomial(lmbda):
    return lmbda**2 - 9*lmbda + 17

# Generate lambda values for plotting the curve
lmbda_values = np.linspace(1, 8, 400)
poly_values = characteristic_polynomial(lmbda_values)

# Create the plot
plt.style.use('seaborn-v0_8-whitegrid')
fig, ax = plt.subplots(figsize=(10, 6))

# Plot the characteristic polynomial
ax.plot(lmbda_values, poly_values, label=r'$f(\lambda) = \lambda^2 - 9\lambda + 17$', color='royalblue', linewidth=2)

# Plot the x-axis (y=0)
ax.axhline(0, color='black', linewidth=0.75)

# Plot the roots (eigenvalues)
ax.plot(eigenvalues, characteristic_polynomial(eigenvalues), 'o', color='crimson', markersize=8, label=f'Eigenvalues (Roots)')

# Annotate the eigenvalues
for eig in eigenvalues:
    ax.annotate(f'$\\lambda \\approx {eig:.2f}$',
                xy=(eig, 0),
                xytext=(eig, -3), # Position the text slightly below the point
                textcoords='data',
                arrowprops=dict(arrowstyle="->", connectionstyle="arc3,rad=.2", color='black'),
                fontsize=12,
                ha='center')

# Set titles and labels for clarity
ax.set_title('Graph of the Characteristic Polynomial', fontsize=16)
ax.set_xlabel(r'$\lambda$ (Lambda)', fontsize=12)
ax.set_ylabel(r'$f(\lambda)$', fontsize=12)
ax.legend(fontsize=11)
ax.grid(True)

# Set plot limits
ax.set_ylim(-4, 10)

# Display the plot
plt.show()