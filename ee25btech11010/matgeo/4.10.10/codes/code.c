#include <math.h>

double point_line_plane_distance(
    double Px, double Py, double Pz,
    double ax, double ay, double az,
    double bx, double by, double bz,
    double nx, double ny, double nz,
    double c
) {
    double dot_na = nx*ax + ny*ay + nz*az;
    double dot_nb = nx*bx + ny*by + nz*bz;

    double lambda = (c - dot_na) / dot_nb;

    double Xx = ax + lambda * bx;
    double Xy = ay + lambda * by;
    double Xz = az + lambda * bz;

    double dx = Px - Xx;
    double dy = Py - Xy;
    double dz = Pz - Xz;

    return sqrt(dx*dx + dy*dy + dz*dz);
}
