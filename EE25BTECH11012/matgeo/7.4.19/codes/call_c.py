from ctypes import c_double
import math

# Define M_PI if not available
M_PI = math.pi

# --- Given Parameters ---
# Radius of the main circle C
radius = c_double(3.0)

# Angle subtended by the chords at the center in radians
angle_rad = c_double((2.0 * M_PI) / 3.0)

# --- Calculation ---
# 1. Find half the angle
half_angle = c_double(angle_rad.value / 2.0)

# 2. Calculate the radius of the locus circle
locus_radius = c_double(radius.value * math.cos(half_angle.value))

# 3. Radius squared
locus_radius_squared = c_double(math.pow(locus_radius.value, 2))

# --- Output ---
print(f"Problem: Find the locus of the midpoints of chords of the circle x^2 + y^2 = {math.pow(radius.value, 2):.0f}")
print("where the chords subtend an angle of 2*pi/3 at the center.\n")

print("--- Calculation Results ---")
print(f"Radius of the locus circle: {locus_radius.value:.2f}")
print(f"Radius of the locus circle squared: {locus_radius_squared.value:.2f}\n")

print(f"The final equation of the locus is: x^2 + y^2 = {locus_radius_squared.value:.2f}")
print("This corresponds to option (d): x^2 + y^2 = 9/4")
