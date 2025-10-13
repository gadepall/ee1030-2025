// vector_solver_matrix_mul.c
#include <stdio.h>
#include <math.h>

// Matrix multiplication: result = u^T * v (both are 3x1 vectors)
double matrix_multiply_transpose(const double u[3], const double v[3]) {
    double result = 0.0;
    for (int i = 0; i < 3; ++i)
        result += u[i] * v[i];  // Equivalent to u^T * v
    return result;
}

// Solves y from matrix-based condition: (a + b)^T * (a - b) = 0
int solve_y_matrix_form(double* y1, double* y2) {
    // Let a = [2, y, 1]
    // Let b = [1, 2, 3]

    // Instead of computing symbolic expression,
    // construct u = a + b and v = a - b with variable y
    // and then expand (u^T * v) = 0 as a function of y

    // Compute constant terms
    double u1 = 2 + 1;     // a1 + b1 = 3
    double u3 = 1 + 3;     // a3 + b3 = 4
    double v1 = 2 - 1;     // a1 - b1 = 1
    double v3 = 1 - 3;     // a3 - b3 = -2

    // u2 = y + 2, v2 = y - 2
    // So: result = u1*v1 + (y+2)(y-2) + u3*v3
    // => result = 3*1 + (y^2 - 4) + 4*(-2)
    // => result = y^2 - 9

    double A = 1.0;   // Coefficient of y^2
    double B = 0.0;
    double C = -9.0;

    double discriminant = B*B - 4*A*C;
    if (discriminant < 0)
        return -1;

    double sqrt_disc = sqrt(discriminant);
    *y1 = (-B + sqrt_disc) / (2*A);
    *y2 = (-B - sqrt_disc) / (2*A);
    return 0;
}


