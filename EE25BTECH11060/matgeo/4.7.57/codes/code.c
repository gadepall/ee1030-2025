#include <stdio.h>
#include <math.h>

int main() {
    // Line: 3x - 4y - 26 = 0
    double n[2] = {3, -4};   // normal vector
    double c = 26;
    double P[2] = {3, -5};   // point (3, -5)

    // Compute n^T * P
    double dot = n[0]*P[0] + n[1]*P[1];

    // Numerator |n^T P - c|
    double numerator = fabs(dot - c);
    // Denominator ||n||
    double norm = sqrt(n[0]*n[0] + n[1]*n[1]);
    // Distance
    double distance = numerator / norm;
    printf("Distance = %lf\n", distance);
    return 0;
}
