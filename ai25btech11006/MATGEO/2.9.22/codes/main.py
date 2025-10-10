import math

# Given magnitudes
norm_a = 1
norm_b = 2
norm_c = 3

# Since b and c are perpendicular, dot product is zero
dot_bc = 0

# Calculate v squared
v_squared = 9 * norm_a**2 + 4 * norm_b**2 + 4 * norm_c**2 - 8 * dot_bc

# Final magnitude
v_magnitude = math.sqrt(v_squared)

print(f"The magnitude |3a - 2b + 2c| is √{int(v_squared)} ≈ {v_magnitude:.4f}")

