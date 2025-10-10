#include <stdio.h>
#include "matfun.h"

int main() {
    double A[3] = {1, 2, 3};
    double B[3] = {3, 2, -1};
    double BA[3];
    double rhs;

    // Compute B - A
    vector_subtract(B, A, BA, 3);

    // Compute dot products B.B and A.A
    double BTB = dot_product(B, B, 3);
    double ATA = dot_product(A, A, 3);

    rhs = BTB - ATA;

    // Multiply BA by 2
    scalar_multiply(BA, BA, 2, 3);

    printf("Vector (2(B - A)) is: [%.2f, %.2f, %.2f]\n", BA[0], BA[1], BA[2]);
    printf("Right-hand side value (B.B - A.A): %.2f\n", rhs);

    printf("Equation of the plane in vector form: [%.2f %.2f %.2f] \\cdot X = %.2f\n", BA[0], BA[1], BA[2], rhs/2);

    return 0;
}
