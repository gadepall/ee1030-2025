#include <stdio.h>
#include <math.h>

void make_data(double *points) {
    double Px = 2; double Py = 2;
    double Qx = -4; double Qy = -4;
    double Rx = 5; double Ry = -8;

    double Mx = (Px + Qx)/2; double My = (Py + Qy)/2;

    double value = sqrt(((Mx - Rx)*(Mx - Rx))+((My - Ry)*(My - Ry)));

    points[0] = Px;points[1] = Py;
    points[2] = Qx;points[3] = Qy;
    points[4] = Rx;points[5] = Ry;
    points[6] = Mx;points[7] = My;
    points[8] = value;
}



