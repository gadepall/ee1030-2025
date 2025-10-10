#include <stdio.h>

int main() {
    // Given points
    int x1 = 6, y1 = -4;
    int x2 = -2, y2 = -7;

    int m, n;  // ratio m:n

    // Equation: (m*x2 + n*x1) / (m + n) = 0
    // => m*x2 + n*x1 = 0
    // => m/n = -x1 / x2
    // Note: since x=0 (Y-axis)

    m = x1;       // numerator
    n = -x2;      // denominator (taking negative since formula is -x1/x2)

    // Simplify ratio if needed (but we'll just print as is)
    printf("The Y-axis divides the line in the ratio %d:%d\n", m, n);

    // Now find intersection point using section formula
    float x = (m * x2 + n * x1) / (float)(m + n);
    float y = (m * y2 + n * y1) / (float)(m + n);

    printf("Point of intersection: (%.2f, %.2f)\n", x, y);

    return 0;
}
