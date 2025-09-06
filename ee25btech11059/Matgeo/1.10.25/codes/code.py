import math

# Define the angles in degrees
alpha = 90.0  # Angle with X-axis
beta = 60.0   # Angle with Y-axis
gamma = 30.0  # Angle with Z-axis

# Convert degrees to radians
alpha_rad = math.radians(alpha)
beta_rad = math.radians(beta)
gamma_rad = math.radians(gamma)

# Calculate the direction cosines
l = math.cos(alpha_rad)  # cos(90 degrees)
m = math.cos(beta_rad)   # cos(60 degrees)
n = math.cos(gamma_rad)  # cos(30 degrees)

# Print the direction cosines
print("Direction Cosines of the vector:")
print(f"l = cos(90 degrees) = {l:.2f}")
print(f"m = cos(60 degrees) = {m:.2f}")
print(f"n = cos(30 degrees) = {n:.2f}")

# Display the vector (l, m, n)
print(f"Direction cosines of vector x = ({l:.2f}, {m:.2f}, {n:.2f})")
