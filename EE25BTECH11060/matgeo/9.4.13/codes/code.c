#include <stdio.h>
int main() {
    // Define constants a, b, c (such that a^2 + b^2 + c^2 = 1)
    double a, b, c;
    printf("Enter values for a, b, c (a^2 + b^2 + c^2 = 1): ");
    scanf("%lf %lf %lf", &a, &b, &c);

    // Variables x and y
    double x, y;
    printf("Enter values for x and y: ");
    scanf("%lf %lf", &x, &y);

    // Original matrix M
    double M[3][3];
    M[0][0] = a*x - b*y - c; M[0][1] = b*x + a*y;      M[0][2] = c*x + a;
    M[1][0] = b*x + a*y;     M[1][1] = -a*x + b*y - c; M[1][2] = c*y + b;
    M[2][0] = c*x + a;       M[2][1] = c*y + b;        M[2][2] = -a*x - b*y + c;

    // Apply row operation: R3 -> R3 - c*R1 - b*R2
    double newR3[3];
    newR3[0] = M[2][0] - c*M[0][0] - b*M[1][0];
    newR3[1] = M[2][1] - c*M[0][1] - b*M[1][1];
    newR3[2] = M[2][2] - c*M[0][2] - b*M[1][2];

    // Determinant using expansion along R3 (simplified after operation)
    double det = M[0][0]*(M[1][1]*newR3[2] - M[1][2]*newR3[1])
               - M[0][1]*(M[1][0]*newR3[2] - M[1][2]*newR3[0])
               + M[0][2]*(M[1][0]*newR3[1] - M[1][1]*newR3[0]);

    printf("Determinant after row operation: %lf\n", det);

    // Since quadratic terms cancel, det is linear in x and y
    printf("This determinant represents a straight line in x and y.\n");

    return 0;
}








 
