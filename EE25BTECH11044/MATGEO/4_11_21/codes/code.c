#include <stdio.h>

int main() {
    // Given plane coefficients
    float a1 = 2, b1 = 2, c1 = -3, d1 = 7;
    float a2 = 2, b2 = 5, c2 = 3, d2 = 9;
    
    float lambda; // scalar parameter

    // Step 1: Equal intercepts condition -> a/c must be same for x and z intercepts
    // From: (2 + 2λ)x = 7 + 9λ and (-3 + 3λ)z = 7 + 9λ, with x = z
    // => (2 + 2λ) = (-3 + 3λ)
    lambda = 5.0;

    // Step 2: Substitute λ = 5 in general plane coefficients
    float a = a1 + lambda * a2;  // 2 + 2λ
    float b = b1 + lambda * b2;  // 2 + 5λ
    float c = c1 + lambda * c2;  // -3 + 3λ
    float d = d1 + lambda * d2;  // 7 + 9λ

    // Step 3: Display result
    printf("The required plane equation is:\n");
    printf("(%.0f)x + (%.0f)y + (%.0f)z = %.0f\n", a, b, c, d);

    // Optional: print intercepts for verification
    float x_intercept = d / a;
    float y_intercept = d / b;
    float z_intercept = d / c;
    
    printf("\nIntercepts on axes:\n");
    printf("x-intercept = %.2f\n", x_intercept);
    printf("y-intercept = %.2f\n", y_intercept);
    printf("z-intercept = %.2f\n", z_intercept);

    return 0;
}
