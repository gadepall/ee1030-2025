#include <stdio.h>
#include <math.h>

// Function to calculate distance
double distance(int x1, int y1, int x2, int y2) {
    return sqrt((x2 - x1) * (x2 - x1) + (y2 - y1) * (y2 - y1));
}

// Function to generate points (returns through array)
void get_points(int points[4]) {
    // Point A(0,6), Point B(0,-2)
    points[0] = 0;  // x1
    points[1] = 6;  // y1
    points[2] = 0;  // x2
    points[3] = -2; // y2
}

