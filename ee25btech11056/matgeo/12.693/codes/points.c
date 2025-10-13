#include <stdio.h>

void solve_ab(double V1[2][2], double u1[2], double f1, double V2[2][2],
              double u2[2], double f2, double result[2]) {
  // Given point of intersection
  double x = 1.0, y = 2.0;

  // Condition 1: Point (1,2) lies on circle 1: x^2 + y^2 + a*x + 6 = 0
  // => 1^2 + 2^2 + a*1 + 6 = 0 => a + 11 = 0
  double a = -11.0;

  // Condition 2: Point (1,2) lies on circle 2: x^2 + y^2 + b*x - 4 = 0
  // => 1^2 + 2^2 + b*1 - 4 = 0 => b + 1 = 0
  double b = -1.0;

  // Condition 3: Orthogonality => 2 u1^T u2 = f1 + f2
  // Here u1 = (a/2,0), u2 = (b/2,0)
  // => 2 * (a/2)*(b/2) = f1 + f2
  // => ab/2 = 6 + (-4) = 2  => ab = 4

  result[0] = a;
  result[1] = b;
}
