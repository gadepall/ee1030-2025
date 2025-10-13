#include <stdio.h>
#include <math.h>

// Compute eigenvalues of a 2x2 real matrix
// A = [a b; c d]
void eigenvalues(double a, double b, double c, double d, double *eig1, double *eig2) {
    double trace = a + d;
    double det = a * d - b * c;
    double disc = trace * trace - 4 * det;

    if (disc < 0) { // complex case not handled
        *eig1 = *eig2 = NAN;
        return;
    }

    *eig1 = (trace + sqrt(disc)) / 2.0;
    *eig2 = (trace - sqrt(disc)) / 2.0;
}

// Compute eigenvector for given eigenvalue
void eigenvector(double a, double b, double c, double d, double eig, double *v) {
    double m11 = a - eig;
    double m12 = b;
    double m21 = c;
    double m22 = d - eig;

    // Try first row equation: m11*x + m12*y = 0
    if (fabs(m11) > 1e-6 || fabs(m12) > 1e-6) {
        if (fabs(m12) > 1e-6) {
            v[0] = 1.0;
            v[1] = -m11 / m12;
        } else {
            v[0] = -m12 / m11;
            v[1] = 1.0;
        }
    }
    // Otherwise try second row
    else if (fabs(m21) > 1e-6 || fabs(m22) > 1e-6) {
        if (fabs(m22) > 1e-6) {
            v[0] = 1.0;
            v[1] = -m21 / m22;
        } else {
            v[0] = -m22 / m21;
            v[1] = 1.0;
        }
    } else {
        v[0] = v[1] = 0.0; // degenerate case
    }
}

