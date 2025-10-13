#include <stdio.h>
int are_collinear(float A[3], float B[3], float C[3]);

int main() {
    float A[3] = {-2, 3, 5};
    float B[3] = {1, 2, 3};
    float C[3] = {7, 0, -1};

    if (are_collinear(A, B, C)) {
        printf("The points are collinear.\n");
    } else {
        printf("The points are not collinear.\n");
    }

    return 0;
}
