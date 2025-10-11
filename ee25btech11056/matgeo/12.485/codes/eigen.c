#include <math.h>
#include <stdio.h>

// Function to compute eigenvalues and store eigenvectors
// A is 2x2 matrix
// eigenvalues is a double[2]
// eigenvectors is a double[3][2] for options (a), (b), (c)
void eigen_2x2(double A[2][2], double eigenvalues[2]) {

  // Step 1: Characteristic polynomial |A - λI| = 0
  double trace = A[0][0] + A[1][1];
  double det = A[0][0] * A[1][1] - A[0][1] * A[1][0];

  double disc = trace * trace - 4 * det;
  if (disc < 0)
    disc = 0; // safeguard

  eigenvalues[0] = (trace + sqrt(disc)) / 2.0;
  eigenvalues[1] = (trace - sqrt(disc)) / 2.0;
}
