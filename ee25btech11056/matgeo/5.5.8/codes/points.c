#include <stdio.h>

double *inverse_solve(int n, double A[n][n], double b[n]) {

  static double x[100];

  double aug[n][2 * n]; // augmented matrix[A|I]

  int i, j, k;

  // forming augmented matrix (i is for row and j is for column)
  for (i = 0; i < n; i++) {

    for (j = 0; j < n; j++) {
      aug[i][j] = A[i][j]; // filling in left side
    }

    for (j = n; j < 2 * n; j++) {
      aug[i][j] = (i == (j - n)) ? 1.0 : 0; // filling right side with identity
                                            // matrix using ternary operator
    }
  }

  // Gaussian elimination
  for (i = 0; i < n; i++) {

    double pivot = aug[i][i];

    for (j = 0; j < 2 * n; j++) {
      aug[i][j] /=
          pivot; // dividing to make the first element 1 for easy operation
    }

    for (k = 0; k < n; k++) { // k is for row

      if (k != i) {
        double factor = aug[k][i];
        for (j = 0; j < 2 * n; j++) {
          aug[k][j] -= factor * aug[i][j];
        }
      }
    }
  }

  // multiply inverse of a with b
  for (i = 0; i < n; i++) {

    x[i] = 0;

    for (j = 0; j < n; j++) {
      x[i] += aug[i][j + n] * b[j];
    }
  }

  return x;
}
