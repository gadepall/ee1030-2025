#include <math.h>
#include <stdio.h>

// Function to compute slope
double slope(double A[], double l1[], double l2[], double l3[], double c1,
             double c2, double c3) {

  double m;

  // Search for slope m in a reasonable range
  for (m = -10; m <= 0; m += 0.0001) {

    // compute k1, k2, k3 for this m
    double k1 = (c1 - A[0] * l1[0] - A[1] * l1[1]) / (l1[0] + l1[1] * m);
    double s1 = k1 * k1;

    double k2 = (c2 - A[0] * l2[0] - A[1] * l2[1]) / (l2[0] + l2[1] * m);
    double s2 = k2 * k2;

    double k3 = (c3 - A[0] * l3[0] - A[1] * l3[1]) / (l3[0] + l3[1] * m);
    double s3 = k3 * k3;

    // compute the equation
    double eq = (225.0 / s1) + (100.0 / s2) - (36.0 / s3);

    // check if eq is close to zero
    if (fabs(eq) < 1e-3) {
      return m;
    }
  }
}
