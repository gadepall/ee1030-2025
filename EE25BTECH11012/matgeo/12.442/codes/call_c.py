import ctypes
import math

def main():
    # Use ctypes to declare C-style float variables
    a = ctypes.c_float(5)
    b = ctypes.c_float(3)
    c = ctypes.c_float(1)
    d = ctypes.c_float(4)

    trace = ctypes.c_float(a.value + d.value)
    det = ctypes.c_float(a.value * d.value - b.value * c.value)

    discriminant = ctypes.c_float(trace.value * trace.value - 4 * det.value)

    if discriminant.value >= 0:
        sqrt_disc = math.sqrt(discriminant.value)
        lambda1 = ctypes.c_float((trace.value + sqrt_disc) / 2)
        lambda2 = ctypes.c_float((trace.value - sqrt_disc) / 2)

        print(f"Eigenvalues are: {lambda1.value:.2f} and {lambda2.value:.2f}")
    else:
        print("Eigenvalues are complex.")

if __name__ == "__main__":
    main()
