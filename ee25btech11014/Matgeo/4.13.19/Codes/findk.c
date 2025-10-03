// file: findk.c
#include <stdio.h>

// Function to compute k
// sol[0] = x, sol[1] = y, sol[2] = k
void find_k(double sol[3]) {
    // Points A(1,1), B(2,4)
    double x1 = 1, y1 = 1;
    double x2 = 2, y2 = 4;
    int m = 3, n = 2;

    // Internal division point (x, y)
    double x = (m*x2 + n*x1) / (double)(m+n);
    double y = (m*y2 + n*y1) / (double)(m+n);

    // Equation: 2x + y = k
    double k = 2*x + y;

    // Store results
    sol[0] = x;
    sol[1] = y;
    sol[2] = k;
}
