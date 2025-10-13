import numpy as np

# --- 1. Problem Setup ---
# Given vectors and conditions from the question.
a = np.array([1, 1, 1])
dot_product_target = 1
cross_product_target = np.array([0, 1, -1])

print("--- Verifying the Correct Unique Solution ---")
print(f"Vector a = {a}")
print(f"Target a . b = {dot_product_target}")
print(f"Target a x b = {cross_product_target}\n")

# --- 2. Define and Verify the Correct Solution ---
# The correct unique solution is b = i, or [1, 0, 0].
b_correct = np.array([1, 0, 0])
print(f"Testing the correct solution: b = {b_correct}")

# Check the dot product (a . b)
dot_product_final = np.dot(a, b_correct)
print(f"\nCalculated a . b = {dot_product_final}")
print(f"--> Matches target? {dot_product_final == dot_product_target} ✅")

# Check the cross product (a x b)
cross_product_final = np.cross(a, b_correct)
print(f"\nCalculated a x b = {cross_product_final}")
print(f"--> Matches target? {np.array_equal(cross_product_final, cross_product_target)} ✅")

print("\nConclusion: Both conditions are met. The unique solution is b = i.")