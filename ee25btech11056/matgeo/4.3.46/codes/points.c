#include <stdio.h>

double intersection() {

  double k, final = -1;

  double a[3] = {2, 1, 1};

  double dot;

  for (k = -100; k <= 100; k++) {

    double x[3] = {2 - k, -3 + k, 1 + 6 * k};

    dot = a[0] * x[0] + a[1] * x[1] + a[2] * x[2];

    if (dot == 7) {
      final = k;
      break;
    }
  }

  return final;
}
