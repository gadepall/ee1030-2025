#include <stdio.h>

// Perform external division in k:1 ratio for 2D vectors stored as arrays.
// a[0],a[1] and b[0],b[1] are inputs.
// v[0],v[1] is the output point V = (k*Y - X)/(k - 1),
// where X = 3a + b and Y = a - 3b.
void external_division_k1_array(const double a[2],
                                const double b[2],
                                double k,
                                double v[2]) {
    double X[2], Y[2];
    // Compute X = 3a + b
    X[0] = 3.0 * a[0] + b[0];
    X[1] = 3.0 * a[1] + b[1];
    // Compute Y = a - 3b
    Y[0] = a[0] - 3.0 * b[0];
    Y[1] = a[1] - 3.0 * b[1];
    // Compute V = (k*Y - X)/(k - 1)
    double denom = k - 1.0;
    v[0] = (k * Y[0] - X[0]) / denom;
    v[1] = (k * Y[1] - X[1]) / denom;
}
