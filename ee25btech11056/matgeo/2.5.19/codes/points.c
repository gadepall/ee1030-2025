#include <math.h>
#include <stdio.h>

// Return the dot product instead of p
double product(double p) {
  double dot = 0;
  double a[3] = {-3, p, 2};
  double b[3] = {-3 * p, 1, -5};

  for (int i = 0; i < 3; i++) {
    dot += a[i] * b[i];
  }
  return dot; // return dot product
}
