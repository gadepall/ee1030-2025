#include <stdio.h>
#include <math.h>

int main() {
    float A[3] = {1, 1, 1};
    float B[3] = {1, 2, 3};
    float C[3] = {2, 3, 1};

    float U[3], V[3], CP[3];

    for (int i = 0; i < 3; i++) {
        U[i] = B[i] - A[i];
        V[i] = C[i] - A[i];
    }

    CP[0] = U[1]*V[2] - U[2]*V[1];
    CP[1] = U[2]*V[0] - U[0]*V[2];
    CP[2] = U[0]*V[1] - U[1]*V[0];

    float mag = sqrt(CP[0]*CP[0] + CP[1]*CP[1] + CP[2]*CP[2]);
    float area = 0.5 * mag;

    printf("Area of triangle ABC = %.5f\n", area);
    return 0;
}
