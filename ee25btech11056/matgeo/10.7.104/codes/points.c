#include <math.h>

double eccentricity(double lambda, double a, double b) {
  // Point P (lambda, 2*lambda)
  double x = lambda;
  double y = 2 * lambda;

  // Slope of parabola tangent
  double m_p = (2 * lambda) / y;

  // Slope of ellipse tangent
  double m_e = -(b * b * x) / (a * a * y);

  double e = sqrt(1.0 - (a * a) / (b * b));
  return e;
}
