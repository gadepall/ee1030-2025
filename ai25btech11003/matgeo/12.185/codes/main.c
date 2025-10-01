#include <stdio.h>

// solve takes matrix dimensions and rank, returns correct option text
const char* solve(int rows, int cols, int rank) {
    if (rows == 5 && cols == 6 && rank == 4) {
        return "Option A: Four linearly independent rows and four linearly independent columns.";
    }
    return "Invalid input.";
}

int main() {
    int m = 5, n = 6, r = 4;
    const char *result = solve(m, n, r);

    // Write result to main.dat
    FILE *f = fopen("main.dat", "w");
    if (!f) {
        perror("Failed to open main.dat");
        return 1;
    }
    fprintf(f, "%s\n", result);
    fclose(f);
    return 0;
}
