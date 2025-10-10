#include <stdio.h>

int main() {
    FILE *fp;
    double u, v, x, y;

    // Open file for writing (including status and solution)
    fp = fopen("answer.dat", "w");

    if (fp == NULL) {
        return 1;  // Cannot proceed if file can't be opened
    }

    // Solve the equations:
    // 3u + 8v = -1
    //  u - 2v =  2

    // Step 1: Solve second equation for u
    // u = 2 + 2v
    // Substitute into first equation:
    // 3(2 + 2v) + 8v = -1
    // => 6 + 6v + 8v = -1
    // => 14v = -7 => v = -0.5
    v = -0.5;
    u = 2 + 2 * v;  // u = 1.0

    // Check for division by zero
    if (u == 0.0 || v == 0.0) {
        fprintf(fp, "Error: Division by zero encountered while computing x or y.\n");
        fclose(fp);
        return 1;
    }

    // Compute x and y
    x = 1.0 / u;  // x = 1.0
    y = 1.0 / v;  // y = -2.0

    // Write the solution to file
    fprintf(fp, "The solution is:\n");
    fprintf(fp, "x = %.2lf\n", x);
    fprintf(fp, "y = %.2lf\n", y);

    fclose(fp);
    return 0;
}

