#include <math.h>


void get_perpendicular_line(double px, double py, double pz,
                           double nx, double ny, double nz,
                           double *point_x, double *point_y, double *point_z,
                           double *dir_x, double *dir_y, double *dir_z)
{
    *point_x = px;
    *point_y = py;
    *point_z = pz;

    *dir_x = nx;
    *dir_y = ny;
    *dir_z = nz;
}

void get_point_on_line(double ax, double ay, double az,
                      double dx, double dy, double dz,
                      double t,
                      double *x, double *y, double *z)
{
    *x = ax + t * dx;
    *y = ay + t * dy;
    *z = az + t * dz;
}
