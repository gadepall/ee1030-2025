#include <math.h>

// Distance between two parallel lines with same normal (nx, ny):
// nx*x + ny*y = c1  and  nx*x + ny*y = c2
double distance_between_lines(double c1, double c2, double nx, double ny) {
    double denom = sqrt(nx * nx + ny * ny);
    return fabs(c1 - c2) / denom;
}

// Projection of point (px, py) onto line: nx*x + ny*y = c
void projection_on_line(double px, double py, double nx, double ny, double c,
                        double* qx, double* qy) {
    double denom = nx * nx + ny * ny;
    double t = (c - (nx * px + ny * py)) / denom;
    *qx = px + nx * t;
    *qy = py + ny * t;
}
