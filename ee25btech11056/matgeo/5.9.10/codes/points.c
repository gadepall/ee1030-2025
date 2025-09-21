#include <stdio.h>

double *gaussian_elimination(double a[2][3]) {

  static double sol[2];
  int i, j, k;
  double ratio;
  int n = 2;

  // forward elimination (j for rows and i for columns of augmented_matrix,)
  for (i = 0; i < n - 1; i++) {

    for (j = i + 1; j < n; j++) {
      ratio = a[j][i] / a[i][i];

      for (k = i; k < n + 1; k++) { // k is also for columns
        a[j][k] -=
            ratio *
            a[i][k]; // to do R2 -> R2 - ratio*R1 , then R3 -> R3 -ratio*R1
      }
    }
  }

  // Back substitution
  for (i = n - 1; i >= 0; i--) {

    sol[i] = a[i][n];

    for (j = i + 1; j < n; j++) {
      sol[i] -= a[i][j] * sol[j];
    }

    sol[i] /= a[i][i];
  }

  return sol;
}
