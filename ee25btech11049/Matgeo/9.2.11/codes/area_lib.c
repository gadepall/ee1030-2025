#include <math.h>

/**
 * @brief Defines the parabola y = 3*sqrt(x) for the first quadrant.
 * * @param x The x-coordinate.
 * @return The corresponding y-coordinate.
 */
double parabola_func(double x) {
    return 3.0 * sqrt(x);
}

/**
 * @brief Calculates the definite integral of the parabola function 
 * using the trapezoidal rule.
 * * @param a The lower limit of integration.
 * @param b The upper limit of integration.
 * @param n The number of trapezoids (steps) to use for the approximation.
 * @return The calculated area under the curve in the first quadrant.
 */
double trapezoidal_area(double a, double b, int n) {
    double h = (b - a) / n;
    // Initialize sum with the first and last terms of the trapezoidal rule
    double sum = 0.5 * (parabola_func(a) + parabola_func(b));
    
    // Add the intermediate terms
    for (int i = 1; i < n; i++) {
        sum += parabola_func(a + i * h);
    }

    return h * sum;
}

