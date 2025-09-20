#include "geometry.h"

// pts = {x0,y0,x1,y1,x2,y2,x3,y3}
int is_parallelogram(double *pts) {
    int x0=pts[0], y0=pts[1];
    int x1=pts[2], y1=pts[3];
    int x2=pts[4], y2=pts[5];
    int x3=pts[6], y3=pts[7];

    // AB = (x1-x0, y1-y0), DC = (x2-x3, y2-y3)
    int abx = x1-x0, aby = y1-y0;
    int dcx = x2-x3, dcy = y2-y3;

    // AD = (x3-x0, y3-y0), BC = (x2-x1, y2-y1)
    int adx = x3-x0, ady = y3-y0;
    int bcx = x2-x1, bcy = y2-y1;

    // AB || DC and AD || BC → cross product zero
    int cond1 = abx*dcy - aby*dcx;
    int cond2 = adx*bcy - ady*bcx;

    return (cond1==0 && cond2==0);
}
