#include <math.h>
#include <stdio.h>

double
area_calculate(double b,
               double c) { // b is for the lower bound and c is the radius

  double area;

  double l = b;
  double u = c;

  double theta_1 = asin(u / c);
  double k1 = c * c - u * u;

  double theta_2 = asin(l / c);
  double k2 = c * c - l * l;

  double upper = (u / 2) * (sqrt(k1)) + ((c * c) / 2) * (theta_1);

  double lower = (l / 2) * (sqrt(k2)) + ((c * c) / 2) * (theta_2);

  area = 2 * (upper - lower);

  return area;
}
