#include <stdio.h>
#include <math.h>

int main() {
    // Given
    double e = 1.5;   // eccentricity
    double c = 2.0;   // focus distance

    // Compute parameters
    double a = c / e;       // semi-major axis
    double b2 = c*c - a*a;  // b^2
    double b = sqrt(b2);

    // Conic form coefficients (for Python V, u, f)
    double V11 = 9.0/16.0;
    double V22 = -9.0/20.0;
    double f   = -1.0;

    // Output in Python-readable format
    printf("# Hyperbola parameters\n");
    printf("a = %.6f\n", a);
    printf("b = %.6f\n", b);
    printf("V = [[%.6f, 0], [0, %.6f]]\n", V11, V22);
    printf("u = [[0], [0]]\n");
    printf("f = %.1f\n", f);

    return 0;
}
