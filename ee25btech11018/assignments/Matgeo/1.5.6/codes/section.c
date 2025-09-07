#include <stdio.h>

// Store the given values as global constants
const int Ax = 7, Ay = -6;
const int Bx = 3, By = 4;
const int m = 1, n = 2;

// Function to compute the dividing point
void get_dividing_point(float *Px, float *Py) {
    *Px = (n * Ax + m * Bx) / (float)(m + n);
    *Py = (n * Ay + m * By) / (float)(m + n);
}

// Optional: function to print stored values
void print_values() {
    printf("Point A = (%d, %d)\n", Ax, Ay);
    printf("Point B = (%d, %d)\n", Bx, By);
    printf("Ratio m:n = %d:%d\n", m, n);
}

