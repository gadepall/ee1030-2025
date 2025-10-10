#include <stdio.h>
#include <math.h>

int main() {
    // Given magnitudes
    double norm_a = 1.0;
    double norm_b = 2.0;
    double norm_c = 3.0;

    // Dot products not needed because they cancel or are zero
    double dot_bc = 0.0;

    // Calculate the magnitude squared of v = 3a - 2b + 2c
    double v_squared = 9 * norm_a * norm_a
                     + 4 * norm_b * norm_b
                     + 4 * norm_c * norm_c
                     - 12 * 0  // a.b cancels
                     + 12 * 0  // a.c cancels
                     - 8 * dot_bc;

    // Final magnitude
    double v_magnitude = sqrt(v_squared);

    printf("The magnitude |3a - 2b + 2c| is √%.0f ≈ %.4f\n", v_squared, v_magnitude);

    return 0;
}

