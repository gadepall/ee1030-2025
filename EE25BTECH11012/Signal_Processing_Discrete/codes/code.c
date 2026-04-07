#include <stdio.h>
#include <math.h>

double calculate_coth(double x) {
    // Check for division by zero (coth(0) is undefined)
    if (x == 0.0) {
        printf("Error: coth(0) is undefined.\n");
        return NAN; // Returns 'Not a Number'
    }

    // Standard formula: cosh(x) / sinh(x)
    return cosh(x) / sinh(x);
}

int main() {
    double x;

    printf("Enter the value of x: ");
    if (scanf("%lf", &x) != 1) {
        printf("Invalid input.\n");
        return 1;
    }

    double result = calculate_coth(x);

    if (!isnan(result)) {
        printf("coth(%.4f) = %.6f\n", x, result);
    }

    return 0;
}