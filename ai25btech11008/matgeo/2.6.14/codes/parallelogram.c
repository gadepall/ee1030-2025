#include <stdio.h>
#include <math.h>

int main() {
    // Define diagonals as vectors
    int d1[3] = {2, -1, 1};
    int d2[3] = {1, 3, -1};

    // Cross product d1 x d2
    int cross[3];
    cross[0] = d1[1]*d2[2] - d1[2]*d2[1]; // y1*z2 - z1*y2
    cross[1] = d1[2]*d2[0] - d1[0]*d2[2]; // z1*x2 - x1*z2
    cross[2] = d1[0]*d2[1] - d1[1]*d2[0]; // x1*y2 - y1*x2

    // Magnitude of cross product
    double mag = sqrt(cross[0]*cross[0] + cross[1]*cross[1] + cross[2]*cross[2]);

    // Area of parallelogram
    double area = 0.5 * mag;

    // Output result
    printf("Area of the parallelogram = %lf\n", area);

    return 0;
}


