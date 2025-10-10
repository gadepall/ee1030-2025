#include <stdio.h>

// Function to compute cross product of two vectors in 3D
void crossProduct(int v1[3], int v2[3], int cross[3]) {
    cross[0] = v1[1]*v2[2] - v1[2]*v2[1];
    cross[1] = v1[2]*v2[0] - v1[0]*v2[2];
    cross[2] = v1[0]*v2[1] - v1[1]*v2[0];
}

// Function to check if three points are collinear in 3D
int areCollinear(int A[3], int B[3], int C[3]) {
    int AB[3], AC[3], cross[3];
    for (int i = 0; i < 3; i++) {
        AB[i] = B[i] - A[i];
        AC[i] = C[i] - A[i];
    }




    crossProduct(AB, AC, cross);
    return (cross[0] == 0 && cross[1] == 0 && cross[2] == 0);
}

int main() {
    int A[3] = {2, -1, 3};
    int B[3] = {3, -5, 1};
    int C[3] = {-1, 11, 9};
    if (areCollinear(A, B, C))
        printf("The points are collinear.\n");
    else
        printf("The points are not collinear.\n");
    return 0;
}
