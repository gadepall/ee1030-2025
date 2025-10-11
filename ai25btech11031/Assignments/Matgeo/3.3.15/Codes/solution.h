#ifndef TRIANGLE_H
#define TRIANGLE_H

#include <math.h>
#include <stdio.h>

// Struct for a point
typedef struct {
    double x, y;
} Point;

// Function to compute intersections of two circles
__attribute__((visibility("default")))
int circle_intersections(Point c1, double r1, Point c2, double r2, Point *p1, Point *p2) {
    double dx = c2.x - c1.x;
    double dy = c2.y - c1.y;
    double d = hypot(dx, dy);

    if (d > r1 + r2 || d < fabs(r1 - r2) || d == 0) {
        return 0; // no intersection
    }

    double a = (r1*r1 - r2*r2 + d*d) / (2*d);
    double h = sqrt(fmax(r1*r1 - a*a, 0));
    double xm = c1.x + a*dx/d;
    double ym = c1.y + a*dy/d;
    double rx = -dy * (h/d);
    double ry = dx * (h/d);

    p1->x = xm + rx;
    p1->y = ym + ry;
    p2->x = xm - rx;
    p2->y = ym - ry;

    return 2; // two intersections
}

#endif

