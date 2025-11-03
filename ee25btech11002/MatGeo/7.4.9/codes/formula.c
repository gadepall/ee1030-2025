#include <stdio.h>
double get_circle_radius() {
    return 2.449489742783178; // sqrt(6)
}
double line_equation(double x) {
    return (2*x - 1)/3;
}

int is_inside_circle(double x, double y) {
    return (x*x + y*y <= 6) ? 1 : 0;
}

int is_on_positive_side(double x, double y) {
    return (2*x - 3*y - 1 > 0) ? 1 : 0;
}

int is_inside_smaller_region(double x, double y) {
    return is_inside_circle(x, y) && is_on_positive_side(x, y);
}
