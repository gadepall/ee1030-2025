#include <stdio.h>
#include <math.h>

int main() {
    // Given magnitudes
    int a = 3, b = 4, c = 5;

    // Since a, b, c are mutually perpendicular (proved in solution),
    // |a + b + c|^2 = |a|^2 + |b|^2 + |c|^2
    int sum_sq = a*a + b*b + c*c;

    // Calculate magnitude
    double magnitude = sqrt(sum_sq);

    // Print result
    printf("The magnitude |a + b + c| = %.2f\n", magnitude);

    return 0;
}