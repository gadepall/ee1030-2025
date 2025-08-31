#include <stdio.h>
#include <math.h>


double cross2D(double x1, double y1, double x2, double y2) {
    return fabs(x1*y2 - y1*x2);
}


double triangle_area(double ax, double ay, double bx, double by, double cx, double cy) {
    double v1x = bx - ax;
    double v1y = by - ay;
    double v2x = cx - ax;    
    double v2y = cy - ay;
    return 0.5 * cross2D(v1x, v1y, v2x, v2y);
}


double quad_area(double ax, double ay, double bx, double by, double cx, double cy, double dx, double dy) {
    double area1 = triangle_area(ax, ay, bx, by, cx, cy);
    double area2 = triangle_area(ax, ay, cx, cy, dx, dy);
    return area1 + area2;
}
