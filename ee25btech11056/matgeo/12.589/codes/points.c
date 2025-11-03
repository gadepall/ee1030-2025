#include <math.h>
#include <stdio.h>

double *gaussian_elimination(double a[3][4]) {
  static double sol[3];
  int i, j, k;
  double ratio;
  int n = 3;

  // Make a copy of 'a' so original isn't lost if no solution
  double A[3][4];
  for (i = 0; i < n; i++) {
    for (j = 0; j < n + 1; j++) {
      A[i][j] = a[i][j];
    }
  }

  // Forward elimination
  for (i = 0; i < n - 1; i++) {
    if (fabs(A[i][i]) < 1e-9) {
      // Pivot is zero -> singular system
      printf("No unique solution (zero pivot at row %d).\n", i);
      return sol; // return sol unchanged
    }

    for (j = i + 1; j < n; j++) {
      ratio = A[j][i] / A[i][i];

      for (k = i; k < n + 1; k++) {
        A[j][k] -= ratio * A[i][k];
      }
    }
  }

  if (fabs(A[n - 1][n - 1]) < 1e-9) {
    // Last pivot also zero -> singular
    printf("No unique solution (zero pivot at last row).\n");
    return sol; // return sol unchanged
  }

  // Back substitution
  for (i = n - 1; i >= 0; i--) {
    sol[i] = A[i][n];

    for (j = i + 1; j < n; j++) {
      sol[i] -= A[i][j] * sol[j];
    }

    sol[i] /= A[i][i];
  }

  return sol;
}
