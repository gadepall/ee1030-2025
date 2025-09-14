#include <stdio.h>

// Function to print line equation given point (x0,y0) and slope
void line_equation(double x0, double y0, double slope) {
    // direction vector from slope
    double dx = 1.0;
    double dy = slope;

    // normal vector = (dy, -dx)
    double a = dy;
    double b = -dx;
    double c = -(a * x0 + b * y0);

    printf("Point on line: (%.2f, %.2f)\n", x0, y0);
    printf("Slope: %.2f\n", slope);
    printf("Cartesian form: %.2fx + %.2fy + %.2f = 0\n", a, b, c);
    printf("Vector form: r = (%.2f, %.2f) + t(%.2f, %.2f)\n",
           x0, y0, dx, dy);
}

// Function exposed for Python (shared object)
const char* get_line_equation() {
    static char result[200];
    double x0 = -2, y0 = 3, slope = -4;
    double dx = 1.0, dy = slope;
    double a = dy, b = -dx, c = -(a * x0 + b * y0);

    snprintf(result, sizeof(result),
             "Equation: %.2fx + %.2fy + %.2f = 0; Vector: r = (%.2f, %.2f) + t(%.2f, %.2f)",
             a, b, c, x0, y0, dx, dy);

    return result;
}

int main() {
    // Example: line through (-2,3) with slope -4
    line_equation(-2, 3, -4);
    return 0;
}

