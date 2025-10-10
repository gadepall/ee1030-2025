#include <math.h>
#include <stdio.h>

// Function to calculate tangent points from P to circle
void tangent_points(double P[2], double r, double sol[2][2]) {
  double x0 = P[0];
  double y0 = P[1];

  // Distance from center to point P
  double d = sqrt(x0 * x0 + y0 * y0);

  // Check external point
  if (d <= r) {
    printf("Point is inside or on the circle, no tangents exist.\n");
    return;
  }

  // Angle of OP
  double theta = atan2(y0, x0);

  // Angle between OP and normal
  double alpha = acos(r / d);

  // First tangent point
  double t1 = theta + alpha;
  sol[0][0] = r * cos(t1);
  sol[0][1] = r * sin(t1);

  // Second tangent point
  double t2 = theta - alpha;
  sol[1][0] = r * cos(t2);
  sol[1][1] = r * sin(t2);
}
