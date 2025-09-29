#include <stdio.h>

int main() {
    // Position vectors
    double A[3] = {3, 6, 9};
    double B[3] = {10, 20, 30};
    double C[3] = {24, -41, 5};

    // Compute dot products directly using vector differences
    double dot1 = (B[0]-A[0])*(C[0]-A[0]) +
                  (B[1]-A[1])*(C[1]-A[1]) +
                  (B[2]-A[2])*(C[2]-A[2]);

    double dot2 = (B[0]-A[0])*(C[0]-B[0]) +
                  (B[1]-A[1])*(C[1]-B[1]) +
                  (B[2]-A[2])*(C[2]-B[2]);

    double dot3 = (C[0]-A[0])*(C[0]-B[0]) +
                  (C[1]-A[1])*(C[1]-B[1]) +
                  (C[2]-A[2])*(C[2]-B[2]);

    // Check for right-angled triangle
    if(dot1 == 0 || dot2 == 0 || dot3 == 0)
        printf("Right-angled triangle\n");
    else
        printf("Not right-angled\n");

    return 0;
}

