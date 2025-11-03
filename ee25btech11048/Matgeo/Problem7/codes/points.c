#include <stdio.h>

double *gaussian_elimination(double a[3][4]) {

  static double sol[3];
  int i, j, k;
  double ratio;
  int n = 3;

  // forward elimination
  for (i = 0; i < n - 1; i++) {
    for (j = i + 1; j < n; j++) {
      ratio = a[j][i] / a[i][i];
      for (k = i; k < n + 1; k++) {
        a[j][k] -= ratio * a[i][k];
      }
    }
  }

  // back substitution
  for (i = n - 1; i >= 0; i--) {
    sol[i] = a[i][n];
    for (j = i + 1; j < n; j++) {
      sol[i] -= a[i][j] * sol[j];
    }
    sol[i] /= a[i][i];
  }

  return sol;
}

int main() {
  // augmented matrix for:
  // 5x - y + 4z = 5
  // 2x + 3y + 5z = 2
  // 5x - 2y + 6z = -1
  double a[3][4] = {
      {5, -1, 4, 5},
      {2, 3, 5, 2},
      {5, -2, 6, -1}
  };

  double *sol = gaussian_elimination(a);

  printf("Solution: x = %lf, y = %lf, z = %lf\n", sol[0], sol[1], sol[2]);

  return 0;
}

