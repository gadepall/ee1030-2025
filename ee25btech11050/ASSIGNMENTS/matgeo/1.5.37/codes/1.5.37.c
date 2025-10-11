// circle.c
#include <math.h>

// Given endpoints (x1,y1), (x2,y2), returns center (cx,cy) and radius r
void compute_circle(double x1, double y1,
                        double x2, double y2,
                        double *cx, double *cy, double *r) {
    *cx = 0.5 * (x1 + x2);
    *cy = 0.5 * (y1 + y2);
    double dx = x2 - x1, dy = y2 - y1;
    *r = 0.5 * sqrt(dx*dx + dy*dy);
}

