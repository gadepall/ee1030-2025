#include <stdio.h>

double compute_c(double a, double b) {
    double denominator = 1 - a * b;
    if (denominator == 0) {
        printf("Error: Denominator is zero, a*b = 1 is not allowed.\n");
        return 0;
    }
    return (2 - a - b) / denominator;
}
