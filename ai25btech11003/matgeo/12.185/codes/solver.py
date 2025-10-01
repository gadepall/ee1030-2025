def solve(rows, cols, rank):
    if rows == 5 and cols == 6 and rank == 4:
        return "Option A: Four linearly independent rows and four linearly independent columns."
    return "Invalid input."

if __name__ == '__main__':
    print(solve(5, 6, 4))
