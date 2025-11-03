#include <stdio.h>
#include <math.h>

#define PI 3.1415926535

double calculate_circular_sector_area() {
    double radius = 2.0;
    double angle_in_radians = PI / 6.0;
    double area = 0.5 * radius * radius * angle_in_radians;
    
    return area;
}


