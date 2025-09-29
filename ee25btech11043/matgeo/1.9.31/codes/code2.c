#include <stdio.h>
#include <math.h>

// Function to calculate the midpoint of a line segment
void findMidpoint(double x1, double y1, double x2, double y2, double *mid_x, double *mid_y) {
    *mid_x = (x1 + x2) / 2.0;
    *mid_y = (y1 + y2) / 2.0;
}

// Function to calculate the distance between two points
double calculateDistance(double x1, double y1, double x2, double y2) {
    return sqrt(pow(x2 - x1, 2) + pow(y2 - y1, 2));
}

int main() {
    double A_x, A_y;
    double B_x, B_y;
    double C_x, C_y;
    double D_x, D_y;
    double length_AD;

    // Calculate midpoint D of BC
    findMidpoint(B_x, B_y, C_x, C_y, &D_x, &D_y);

    // Calculate the length of median AD
    length_AD = calculateDistance(A_x, A_y, D_x, D_y);

    return 0;
}