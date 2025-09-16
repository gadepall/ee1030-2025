#include <stdio.h>
#include <math.h>

// Function to compute dot product of two vectors
double dot_product(double v1[3], double v2[3]) {
    return v1[0]*v2[0] + v1[1]*v2[1] + v1[2]*v2[2];
}

// Function to compute norm of a vector
double norm(double v[3]) {
    return sqrt(v[0]*v[0] + v[1]*v[1] + v[2]*v[2]);
}

int main() {
    double A[3], B[3], C[3], D[3];
    double AB[3], CD[3];
    int i;

    // Input points
    printf("Enter coordinates of A (x y z): ");
    scanf("%lf %lf %lf", &A[0], &A[1], &A[2]);

    printf("Enter coordinates of B (x y z): ");
    scanf("%lf %lf %lf", &B[0], &B[1], &B[2]);

    printf("Enter coordinates of C (x y z): ");
    scanf("%lf %lf %lf", &C[0], &C[1], &C[2]);

    printf("Enter coordinates of D (x y z): ");
    scanf("%lf %lf %lf", &D[0], &D[1], &D[2]);

    // Compute vectors AB and CD
    for (i = 0; i < 3; i++) {
        AB[i] = B[i] - A[i];
        CD[i] = D[i] - C[i];
    }

    // Print vectors
    printf("\nVector AB = (%.2lf, %.2lf, %.2lf)\n", AB[0], AB[1], AB[2]);
    printf("Vector CD = (%.2lf, %.2lf, %.2lf)\n", CD[0], CD[1], CD[2]);

    // Compute angle
    double dot = dot_product(AB, CD);
    double cos_theta = dot / (norm(AB) * norm(CD));
    int x = (cos_theta * 100);
    double y = x/100;
    double theta = acos(y)*180/M_PI;

    printf("\nDot product = %.2lf\n", dot);
    printf("cos(theta) = %.2lf\n", cos_theta);
    printf("Angle between AB and CD = %.2lf degrees\n", theta);

    if (cos_theta == 1 || -1){
        printf("\n AB and CD are collinear.\n");
    } else {
        printf("\n AB and CD are not collinear.\n");
    }

    return 0;
}

