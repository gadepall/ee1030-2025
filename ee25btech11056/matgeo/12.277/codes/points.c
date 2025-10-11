#include <stdio.h>

double slope(double a[], double b[]) {

  double m;

  m = (b[1] - a[1]) / (b[0] - a[0]);

  return m;
}
