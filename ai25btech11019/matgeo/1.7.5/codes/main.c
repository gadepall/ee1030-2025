#include <stdio.h>

int main() {
    // Points
    int A[2] = {-5, 1};
    int C[2] = {4, -2};

    // We want to find p for Point B = (1, p)
    int p;

    // From row reduction condition:
    // (B-A , C-A)^T must have rank 1
    // After elimination => -3(p+1) = 0  => p = -1
    p = -1;

    // Compute difference vectors
    int BA[2] = {1 - A[0], p - A[1]};   // B - A
    int CA[2] = {C[0] - A[0], C[1] - A[1]}; // C - A

    // Construct matrix (B-A  C-A)^T
    int M[2][2] = {
        {BA[0], BA[1]},
        {CA[0], CA[1]}
    };

    printf("Value of p = %d\n\n", p);

    printf("Matrix (B-A  C-A)^T before row reduction:\n");
    printf("[%d  %d]\n", M[0][0], M[0][1]);
    printf("[%d  %d]\n", M[1][0], M[1][1]);

    // Row operation: R2 -> 2*R2 - 3*R1 (to avoid fractions)
    int R2_0 = 2*M[1][0] - 3*M[0][0];
    int R2_1 = 2*M[1][1] - 3*M[0][1];

    printf("\nAfter row reduction:\n");
    printf("[%d  %d]\n", M[0][0], M[0][1]);
    printf("[%d  %d]\n", R2_0, R2_1);

    if (R2_0 == 0 && R2_1 == 0) {
        printf("\nThe points A(-5,1), B(1,%d), C(4,-2) are collinear.\n", p);
    } else {
        printf("\nThe points are not collinear.\n");
    }

    return 0;
}
