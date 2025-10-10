#include <stdio.h>
#include <math.h>

/*----------------------------------------------------------
  f(lambda) = (lambda + 6)^2 - (lambda + 2)^2 - 40
  We need f(lambda) = 0
----------------------------------------------------------*/
double f(double lambda) {
    return (lambda + 6.0)*(lambda + 6.0)
         - (lambda + 2.0)*(lambda + 2.0)
         - 40.0;
}

int main(void) {
    double left = -10.0;   // lower bound for search
    double right =  10.0;  // upper bound for search
    double mid;
    double tol = 1e-8;     // desired accuracy

    // Bisection method
    while ((right - left) > tol) {
        mid = (left + right) / 2.0;
        if (f(mid) == 0.0) break;

        // Root lies where sign changes
        if (f(left) * f(mid) < 0.0)
            right = mid;
        else
            left = mid;
    }

    double lambda = (left + right) / 2.0;
    printf("Computed value of lambda: %.10f\n", lambda);

    // Optional verification: compute the scalar product
    double sx = lambda + 2.0;
    double sy = 6.0;
    double sz = -2.0;
    double magnitude = sqrt(sx*sx + sy*sy + sz*sz);
    double scalar_product = (1.0*sx + 1.0*sy + 1.0*sz) / magnitude;
    printf("Verification (scalar product) : %.10f\n", scalar_product);

    return 0;
}