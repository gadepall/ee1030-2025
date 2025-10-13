#include <math.h>



/**
 * @brief Calculates the area of a semicircle using Simpson's 1/3 rule.
 * * @param a The radius of the semicircle.
 * @param n The number of intervals to use for the integration.
 * @return The calculated area as a double.
 */
double calculate_area_c(double a, int n) {
    // For Simpson's rule, n must be an even number.
    if (n % 2 != 0) {
        n++;
    }

    double lower_limit = -a;
    double upper_limit = a;
    double h = (upper_limit - lower_limit) / n;
    double integral_sum = 0.0;

    // The function to integrate is f(x) = sqrt(a*a - x*x)
    
    // Sum the terms according to Simpson's rule: y0 + 4y1 + 2y2 + ...
    for (int i = 0; i <= n; i++) {
        double x = lower_limit + i * h;
        double y = sqrt(a*a - x*x);

        if (i == 0 || i == n) {
            integral_sum += y; // First and last terms
        } else if (i % 2 != 0) {
            integral_sum += 4 * y; // Odd-indexed terms
        } else {
            integral_sum += 2 * y; // Even-indexed terms
        }
    }

    return (h / 3.0) * integral_sum;
}

