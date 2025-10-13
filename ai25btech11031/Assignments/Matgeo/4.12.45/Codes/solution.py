import numpy as np

def standard_form(A, B, constant_sum):
    # Distance between foci
    dist_AB = np.linalg.norm(np.array(A) - np.array(B))
    
    # Semi-major axis
    a = constant_sum / 2.0
    # Focal length
    c = dist_AB / 2.0
    # Semi-minor axis
    b = np.sqrt(a*a - c*c)

    return a*a, b*b, b*b  # a², b², c²

if __name__ == "__main__":
    A = list(map(float, input("Enter coordinates of point A (Ax Ay Az): ").split()))
    B = list(map(float, input("Enter coordinates of point B (Bx By Bz): ").split()))
    constant_sum = float(input("Enter the constant sum of distances: "))

    a2, b2, c2 = standard_form(A, B, constant_sum)

    print("\nStandard form of the locus equation:")
    print(f"x^2/({a2:.6f}) + y^2/({b2:.6f}) + z^2/({c2:.6f}) = 1")
    print("\nWhere:")
    print(f"a = {np.sqrt(a2):.6f}, b = {np.sqrt(b2):.6f}, c = {np.sqrt(c2):.6f}")

