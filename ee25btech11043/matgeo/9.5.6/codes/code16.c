#include <stdio.h>

// Function to find the sum and product of the roots of a quadratic equation
// For a quadratic equation ax^2 + bx + c = 0
// Sum of roots = -b/a
// Product of roots = c/a
void calculateRootsInfo(double a, double b, double c, double *sum_of_roots, double *product_of_roots) {
    *sum_of_roots = -b / a;
    *product_of_roots = c / a;
}