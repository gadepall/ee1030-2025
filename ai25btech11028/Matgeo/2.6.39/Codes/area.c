// quad_area.c
#include <math.h>

double quad_area(double Px, double Py, double Pz, double Qx, double Qy, double Qz) {
    // cross product components
    double cx = Py*Qz - Pz*Qy;
    double cy = Pz*Qx - Px*Qz;
    double cz = Px*Qy - Py*Qx;

    // magnitude of cross product
    double magnitude = sqrt(cx*cx + cy*cy + cz*cz);

    // area = half the magnitude
    return 0.5 * magnitude;
}
