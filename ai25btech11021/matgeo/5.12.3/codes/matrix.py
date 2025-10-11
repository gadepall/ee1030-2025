count = 0

# Each entry can be 1, 2, or 3
for a in [1, 2, 3]:
    for b in [1, 2, 3]:
        for c in [1, 2, 3]:
            for d in [1, 2, 3]:
                count += 1
                print(f"Matrix {count}:")
                print(f"{a} {b}")
                print(f"{c} {d}\n")

print("Total matrices =", count)

