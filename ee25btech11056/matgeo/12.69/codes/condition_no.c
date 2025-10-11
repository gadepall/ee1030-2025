#include <math.h>
#include <stdio.h>

// Function to compute condition number of a 2x2 matrix
double condition_number(double A[2][2]) {
  // Step 1: Compute ATA = A^T * A
  double ATA[2][2];
  ATA[0][0] = A[0][0] * A[0][0] + A[1][0] * A[1][0];
  ATA[0][1] = A[0][0] * A[0][1] + A[1][0] * A[1][1];
  ATA[1][0] = ATA[0][1]; // symmetric
  ATA[1][1] = A[0][1] * A[0][1] + A[1][1] * A[1][1];

  // Step 2: Eigenvalues of 2x2 symmetric matrix
  double trace = ATA[0][0] + ATA[1][1];
  double det = ATA[0][0] * ATA[1][1] - ATA[0][1] * ATA[1][0];

  double disc = trace * trace - 4 * det;
  if (disc < 0)
    disc = 0; // numerical safeguard , if discriminant of eigen quadratic is
              // less than zero

  double lambda1 = (trace + sqrt(disc)) / 2.0;
  double lambda2 = (trace - sqrt(disc)) / 2.0;

  // Step 3: Singular values = sqrt(eigenvalues)
  double sigma1 = sqrt(lambda1);
  double sigma2 = sqrt(lambda2);

  // Step 4: Condition number = sigma_max / sigma_min
  double sigma_max = (sigma1 > sigma2) ? sigma1 : sigma2;
  double sigma_min = (sigma1 < sigma2) ? sigma1 : sigma2;

  if (sigma_min == 0)
    return INFINITY; // singular matrix , it means it is unbounded
  return sigma_max / sigma_min;
}
