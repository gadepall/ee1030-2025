#include <math.h>
#include <stdio.h>

// Gauss-Seidel solver for your specific system
// 10x - y + z = 0
// x + 10y     = 5
// y + 5z      = 1
void gauss_seidel(double sol[3], int max_iter, double tol) {
  double x = 0.0, y = 0.0, z = 0.0; // initial guess
  double x_new, y_new, z_new;

  for (int k = 0; k < max_iter; k++) {
    // Update x from eq(3)
    x_new = (y - z) / 10.0;

    // Update y from eq(1)
    y_new = (5.0 - x_new) / 10.0;

    // Update z from eq(2)
    z_new = (1.0 - y_new) / 5.0;

    // Check convergence
    if (fabs(x_new - x) < tol && fabs(y_new - y) < tol &&
        fabs(z_new - z) < tol) {
      x = x_new;
      y = y_new;
      z = z_new;
      break;
    }

    // Update values for next iteration
    x = x_new;
    y = y_new;
    z = z_new;
  }

  sol[0] = x;
  sol[1] = y;
  sol[2] = z;
}
