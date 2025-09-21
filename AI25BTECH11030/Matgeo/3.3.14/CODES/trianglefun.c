#include <math.h>
#include "trianglefun.h"

// Construct right triangle with sides 6 and 8 using angle 90 degrees
void construct_right_triangle(Point* A, Point* B, Point* C) {
    A->x = 0.0;
    A->y = 0.0;

    B->x = 6.0;
    B->y = 0.0;

    // Using degrees converted to radians for cos and sin
    C->x = 6.0 * cos(M_PI / 2);  // cos 90°
    C->y = 8.0 * sin(M_PI / 2);  // sin 90°
}

