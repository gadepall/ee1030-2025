#include <math.h>

void compute_triangle(double A[2], double B[2], double C[2]) {
    const double PI = 3.141592653589793;
    double AB = 6.0;
    double angle_A_deg = 30.0;
    double angle_B_deg = 60.0;

    double angle_A = angle_A_deg * PI / 180.0;
    double angle_B = angle_B_deg * PI / 180.0;

    // Point A at origin
    A[0] = 0.0;
    A[1] = 0.0;

    // Point B on x-axis
    B[0] = AB;
    B[1] = 0.0;

    // Length AC using sine rule
    double AC = AB * sin(angle_B);

    // Point C coordinates using angle A
    C[0] = AC * cos(angle_A);
    C[1] = AC * sin(angle_A);
}

