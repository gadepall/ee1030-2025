def dot_product(a, b):
    return sum(x * y for x, y in zip(a, b))

def scalar_multiply(vector, scalar):
    return [scalar * x for x in vector]

def vector_subtract(a, b):
    return [x - y for x, y in zip(a, b)]

def main():
    a = [2, -1, -2]
    b = [7, 2, -3]

    # Compute dot products
    a_dot_b = dot_product(a, b)
    a_dot_a = dot_product(a, a)

    # Compute scalar k
    k = a_dot_b // a_dot_a  # Use // for integer division like in C
    # You can also use: k = a_dot_b / a_dot_a for floating point precision

    # Compute b1 = k * a
    b1 = scalar_multiply(a, k)

    # Compute b2 = b - b1
    b2 = vector_subtract(b, b1)

    # Display results
    print(f"Vector a: {a}")
    print(f"Vector b: {b}")
    print(f"Scalar k: {k}")
    print(f"Vector b1 (parallel to a): {b1}")
    print(f"Vector b2 (perpendicular to a): {b2}")

if __name__ == "__main__":
    main()
