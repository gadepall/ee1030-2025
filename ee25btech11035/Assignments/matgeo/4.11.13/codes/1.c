#include <stdio.h>

typedef struct {
    double x, y, z;
} Point;

Point crossProduct(Point a, Point b) {
    Point result;
    result.x = a.y*b.z - a.z*b.y;
    result.y = a.z*b.x - a.x*b.z;
    result.z = a.x*b.y - a.y*b.x;
    return result;
}

// Exposed function for Python
void solvePlaneAndLine(
    double Ax, double Ay, double Az,
    double Bx, double By, double Bz,
    double Cx, double Cy, double Cz,
    double Px, double Py, double Pz,
    double Qx, double Qy, double Qz,
    double *nx, double *ny, double *nz, double *d,
    double *ix, double *iy, double *iz
) {
    Point A = {Ax, Ay, Az};
    Point B = {Bx, By, Bz};
    Point C = {Cx, Cy, Cz};
    Point P = {Px, Py, Pz};
    Point Q = {Qx, Qy, Qz};

    Point AB = {B.x - A.x, B.y - A.y, B.z - A.z};
    Point AC = {C.x - A.x, C.y - A.y, C.z - A.z};

    Point n = crossProduct(AB, AC);

    *nx = n.x;
    *ny = n.y;
    *nz = n.z;
    *d = -(n.x*A.x + n.y*A.y + n.z*A.z);

    Point PQ = {Q.x - P.x, Q.y - P.y, Q.z - P.z};

    double numerator = -(n.x*P.x + n.y*P.y + n.z*P.z + *d);
    double denominator = n.x*PQ.x + n.y*PQ.y + n.z*PQ.z;

    if (denominator == 0) {
        *ix = *iy = *iz = 0; // parallel case
        return;
    }

    double t = numerator / denominator;

    *ix = P.x + t*PQ.x;
    *iy = P.y + t*PQ.y;
    *iz = P.z + t*PQ.z;
}