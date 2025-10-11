#include <math.h>

// Define the function we want to integrate: sqrt(9/4 - x^2) - x^2/4
double integrand(double x) {
    return sqrt(9.0 / 4.0 - x * x) - (x * x / 4.0);
}

// C function to be called from Python
// It calculates the definite integral using Simpson's 1/3 rule.
// 'a' is the lower limit, 'b' is the upper limit.
// 'n' is the number of intervals and must be even.
double calculate_area(double a, double b, int n) {
    // Calculate the width of each interval
    double h = (b - a) / n;
    
    // Initialize the sum with the first and last terms
    double sum = integrand(a) + integrand(b);

    // Add the terms with coefficient 4 (odd indices)
    for (int i = 1; i < n; i += 2) {
        sum += 4 * integrand(a + i * h);
    }

    // Add the terms with coefficient 2 (even indices)
    for (int i = 2; i < n; i += 2) {
        sum += 2 * integrand(a + i * h);
    }

    // Apply the Simpson's 1/3 rule formula
    return (h / 3.0) * sum;
}

