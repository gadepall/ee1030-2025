#include <math.h>
double volume(double a_x, double a_y, double a_z, double b_x, double b_y, double b_z, double c_x, double c_y, double c_z) {
    int g[3][3] = {
        {a_x*a_x + a_y*a_y + a_z*a_z, a_x*b_x + a_y*b_y + a_z*b_z, a_x*c_x + a_y*c_y + a_z*c_z},
        {b_x*a_x + b_y*a_y + b_z*a_z, b_x*b_x + b_y*b_y + b_z*b_z, b_x*c_x + b_y*c_y + b_z*c_z},
        {c_x*a_x + c_y*a_y + c_z*a_z, c_x*b_x + c_y*b_y + c_z*b_z, c_x*c_x + c_y*c_y + c_z*c_z}
    };
    return sqrt(fabs(g[0][0]*(g[1][1]*g[2][2] - g[1][2]*g[2][1]) - g[0][1]*(g[1][0]*g[2][2] - g[1][2]*g[2][0]) + g[0][2]*(g[1][0]*g[2][1] - g[1][1]*g[2][0])));
}