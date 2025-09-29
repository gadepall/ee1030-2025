#include<stdio.h>

void get_x_coords(float ax, float ay, float *x_out, float *y_out) {
    float mag_x = 3.0f;
    *x_out = mag_x * ax;
    *y_out = mag_x * ay;
}
