#include <math.h>

// To ensure M_PI is defined, which is not standard in older C versions
#ifndef M_PI
#define M_PI 3.14159265358979323846
#endif

// Define a structure to hold 2D coordinates.
// This structure will be shared between C and Python.
typedef struct {
    double x;
    double y;
} Point;

// This is the function that will be called from Python.
// It takes a pointer to a Point and an angle in degrees,
// and it modifies the Point's data in place.
void rotate_point_c(Point* p, double angle_degrees) {
    // Convert the angle from degrees to radians for C's math functions
    double angle_radians = angle_degrees * M_PI / 180.0;

    // Store the original coordinates before overwriting them
    double x_old = p->x;
    double y_old = p->y;

    // Calculate the new coordinates using the standard 2D rotation formulas:
    // x_new = x_old * cos(theta) - y_old * sin(theta)
    // y_new = x_old * sin(theta) + y_old * cos(theta)
    p->x = x_old * cos(angle_radians) - y_old * sin(angle_radians);
    p->y = x_old * sin(angle_radians) + y_old * cos(angle_radians);
}

