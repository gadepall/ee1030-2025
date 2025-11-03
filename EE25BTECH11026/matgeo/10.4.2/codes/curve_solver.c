#include <stdio.h>
#include <math.h>

// Function to evaluate the curve y = (x-7)/((x-2)(x-3))
double curve(double x) {
    double denom = (x - 2.0) * (x - 3.0);
    if (fabs(denom) < 1e-9) {
        return NAN; // return NaN at asymptotes
    }
    return (x - 7.0) / denom;
}

// Function to evaluate tangent line at (7,0)
double tangent(double x) {
    double m_tan = 1.0 / 20.0; // slope of tangent
    return m_tan * (x - 7.0);
}

// Function to evaluate normal line at (7,0)
double normal(double x) {
    double m_norm = -20.0; // slope of normal
    return m_norm * (x - 7.0);
}

// Function to print tangent & normal equations
void print_equations() {
    double m_tan = 1.0 / 20.0;
    double m_norm = -20.0;

    printf("Tangent equation: y = %.1f*(x - 7)\n", m_tan);
    printf("Normal equation:  y = %.1f*(x - 7)\n", m_norm);
}


