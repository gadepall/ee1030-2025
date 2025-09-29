#include <stdio.h>

// A structure to represent a vector with coefficients for a and b
typedef struct {
    int coeff_a;
    int coeff_b;
} Vector;

int main() {
    // P = 2a + 1b
    Vector P = {2, 1};
    // Q = 1a - 3b
    Vector Q = {1, -3};
    // Ratio m:n = 1:2
    int m = 1;
    int n = 2;

    // Applying the external division formula: R = (m*Q - n*P) / (m - n)
    
    // Numerator: (1 * Q) - (2 * P)
    int num_a = (m * Q.coeff_a) - (n * P.coeff_a); // (1*1) - (2*2) = -3
    int num_b = (m * Q.coeff_b) - (n * P.coeff_b); // (1*-3) - (2*1) = -5

    // Denominator: m - n
    int den = m - n; // 1 - 2 = -1
    Vector R;
    R.coeff_a = num_a / den; // -3 / -1 = 3
    R.coeff_b = num_b / den; // -5 / -1 = 5

    printf("The position vector of point R is (%d)a + (%d)b\n", R.coeff_a, R.coeff_b);
return 0;
}