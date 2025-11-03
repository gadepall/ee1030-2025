import math

# --- Setup ---
r = 4
P_x, P_y = 6, 0

# --- Calculations for Points of Contact (q) ---

# From condition: 6 * q_x = 16
q_x = 16 / 6

# From condition: q_x^2 + q_y^2 = r^2
q_y_squared = r**2 - q_x**2
q_y = math.sqrt(q_y_squared)

# --- Verification ---

# Verify calculated q_x against the document's value (8/3)
assert q_x == 8/3

# Verify calculated q_y against the document's value (+/- 4*sqrt(5)/3)
expected_q_y = (4 * math.sqrt(5)) / 3
assert math.isclose(q_y, expected_q_y)

print(f"Calculated Point of Contact 1: ({q_x:.4f}, {q_y:.4f})")
print(f"Calculated Point of Contact 2: ({q_x:.4f}, {-q_y:.4f})\n")


# --- Verify Tangent Equations using Point P(6, 0) ---

# Tangent 1: 2x + sqrt(5)y = 12
tangent1_check = 2 * P_x + math.sqrt(5) * P_y
assert math.isclose(tangent1_check, 12)
print(f"Check Tangent 1 (2x + sqrt(5)y = 12) with P(6,0): {tangent1_check} == 12. Verified.")


# Tangent 2: 2x - sqrt(5)y = 12
tangent2_check = 2 * P_x - math.sqrt(5) * P_y
assert math.isclose(tangent2_check, 12)
print(f"Check Tangent 2 (2x - sqrt(5)y = 12) with P(6,0): {tangent2_check} == 12. Verified.")