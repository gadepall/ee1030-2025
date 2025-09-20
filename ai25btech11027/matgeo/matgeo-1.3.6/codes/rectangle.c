#include "geometry.h"

int is_rectangle(double *pts) {
    if (!is_parallelogram(pts)) return 0;

    int x0=pts[0], y0=pts[1];
    int x1=pts[2], y1=pts[3];
    int x3=pts[6], y3=pts[7];

    // AB = (x1-x0, y1-y0), AD = (x3-x0, y3-y0)
    int abx = x1-x0, aby = y1-y0;
    int adx = x3-x0, ady = y3-y0;

    // dot product = 0 for right angle
    int dot = abx*adx + aby*ady;
    return (dot==0);
}
