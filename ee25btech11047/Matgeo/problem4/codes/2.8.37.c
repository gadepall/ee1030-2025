#include <stdio.h>
#include <math.h>

int main() {
    // Given values
    double a = 4.0;   // |a| = 4
    double lhs = 144; // |a × b|^2 + (a · b)^2 = 144

    // From identity: |a × b|^2 + (a · b)^2 = |a|^2 * |b|^2
    // => |b|^2 = lhs / (|a|^2)
    double b_squared = lhs / (a * a);
    double b = sqrt(b_squared);

    printf("|b| = %.2f\n", b);

    return 0;
}
