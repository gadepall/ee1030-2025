from ctypes import c_double
from math import sqrt

def main():
    # Coefficients for the quadratic equation: x^2 - 55x + 750 = 0
    a = c_double(1.0)
    b = c_double(-55.0)
    c = c_double(750.0)

    # Calculate the discriminant (b^2 - 4ac)
    discriminant = c_double(b.value ** 2 - 4 * a.value * c.value)

    # Check if real solutions exist
    if discriminant.value >= 0:
        # Calculate the two possible roots using the quadratic formula
        root1 = c_double((-b.value + sqrt(discriminant.value)) / (2 * a.value))
        root2 = c_double((-b.value - sqrt(discriminant.value)) / (2 * a.value))

        print("The problem translates to the quadratic equation: x^2 - 55x + 750 = 0")
        print("Solving for x, we find two possible solutions.\n")

        print(f"The number of toys produced on that day was either {root1.value:.0f} or {root2.value:.0f}.\n")

        # Verification for both cases
        print("Verification:")
        cost1 = c_double(55 - root1.value)
        total_cost1 = c_double(root1.value * cost1.value)
        print(f"Case 1: If {root1.value:.0f} toys were produced, the cost per toy is "
              f"(55 - {root1.value:.0f}) = {cost1.value:.0f}. Total cost = "
              f"{root1.value:.0f} * {cost1.value:.0f} = {total_cost1.value:.0f}")

        cost2 = c_double(55 - root2.value)
        total_cost2 = c_double(root2.value * cost2.value)
        print(f"Case 2: If {root2.value:.0f} toys were produced, the cost per toy is "
              f"(55 - {root2.value:.0f}) = {cost2.value:.0f}. Total cost = "
              f"{root2.value:.0f} * {cost2.value:.0f} = {total_cost2.value:.0f}")

    else:
        print("The equation has no real solutions, which means there is an error in the problem's premises.")

if __name__ == "__main__":
    main()
