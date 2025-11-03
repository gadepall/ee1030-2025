#include <stdio.h>

void intersection(double sol[]) {

  double u = 4;
  double v = 2;

  double x = (u + v) / 6;
  double y = (u - v) / 2;

  sol[0] = x;
  sol[1] = y;
}
