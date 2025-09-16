#include <stdio.h>
#include <math.h>

int main() {
    double A[3] = {1,2,-4};
    double B[3] = {3,3,-5};
    double d[3] = {2,3,6};
    double AB[3], cross[3];
    double dist;

    // Compute B - A
    for(int i=0;i<3;i++) AB[i] = B[i] - A[i];

    // Cross product (AB x d)
    cross[0] = AB[1]*d[2] - AB[2]*d[1];
    cross[1] = AB[2]*d[0] - AB[0]*d[2];
    cross[2] = AB[0]*d[1] - AB[1]*d[0];

    // Norms
    double num = sqrt(cross[0]*cross[0] + cross[1]*cross[1] + cross[2]*cross[2]);
    double den = sqrt(d[0]*d[0] + d[1]*d[1] + d[2]*d[2]);

    dist = num / den;
    printf("Distance between lines = %lf\n", dist);

    // Output A, B, direction vector for plotting
    printf("A: %lf %lf %lf\n", A[0], A[1], A[2]);
    printf("B: %lf %lf %lf\n", B[0], B[1], B[2]);
    printf("d: %lf %lf %lf\n", d[0], d[1], d[2]);

    return 0;
}
