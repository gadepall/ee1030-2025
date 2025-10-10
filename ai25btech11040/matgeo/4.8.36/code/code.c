#include <math.h>

double cross_x(double a_x, double a_y, double a_z, double b_x, double b_y, double b_z){
    return a_y*b_z - a_z*b_y;
}

double cross_y(double a_x, double a_y, double a_z, double b_x, double b_y, double b_z){
    return - (a_x*b_z - a_z*b_x);
}

double cross_z(double a_x, double a_y, double a_z, double b_x, double b_y, double b_z){
    return a_x*b_y - a_y*b_x;
}

double norm(double x, double y, double z){
    return sqrt(x*x + y*y + z*z);
}