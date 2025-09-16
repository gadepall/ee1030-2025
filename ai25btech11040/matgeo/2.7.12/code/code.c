#include<math.h>

double area(double a_x, double a_y, double b_x, double b_y, double c_x, double c_y) {
    return 0.5 * fabs((a_x - b_x) * (a_y - c_y) - (a_x - c_x) * (a_y - b_y));
}