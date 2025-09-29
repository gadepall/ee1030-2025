#include <stdio.h>
#include <math.h>

// Function to compute magnitude of (3a - 2b + 2c)
double compute_magnitude() {
    // Given norms
    double norm_a = 1.0;
    double norm_b = 2.0;
    double norm_c = 3.0;

    // From conditions: b·c = 0, and a·b = a·c = k
    // But the k cancels in expansion, so result is independent of k.

    double result_squared =
        9 * (norm_a * norm_a) +       // 9|a|^2
        4 * (norm_b * norm_b) +       // 4|b|^2
        4 * (norm_c * norm_c) +       // 4|c|^2
        -12 * (0) + 12 * (0) + -8 * (0);

    // Simplified: 9*1 + 4*4 + 4*9 = 61
    return sqrt(result_squared);
}

int main() {
    double magnitude = compute_magnitude();
    printf("The magnitude of (3a - 2b + 2c) is: %.5f\n", magnitude);
    return 0;
}

