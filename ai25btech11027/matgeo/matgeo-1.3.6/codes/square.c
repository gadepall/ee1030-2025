#include "geometry.h"

int is_square(double *pts) {
    if (!is_rectangle(pts)) return 0;

    int x0=pts[0], y0=pts[1];
    int x1=pts[2], y1=pts[3];
    int x3=pts[6], y3=pts[7];

    // AB and AD lengths
    int abx = x1-x0, aby = y1-y0;
    int adx = x3-x0, ady = y3-y0;

    int ab2 = abx*abx + aby*aby;
    int ad2 = adx*adx + ady*ady;

    return (ab2 == ad2);
}
