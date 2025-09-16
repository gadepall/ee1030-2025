#include <stdio.h>

// Function to compute rank of 2x3 matrix
int rank_matrix_2x3(int v1[3], int v2[3]) {
    // Check if both rows are zero
    if ((v1[0] == 0 && v1[1] == 0 && v1[2] == 0) &&
        (v2[0] == 0 && v2[1] == 0 && v2[2] == 0))
        return 0;

    // If one row is zero
    if ((v1[0] == 0 && v1[1] == 0 && v1[2] == 0) ||
        (v2[0] == 0 && v2[1] == 0 && v2[2] == 0))
        return 1;

    // Check if v1 and v2 are linearly dependent
    if (v1[0] * v2[1] == v1[1] * v2[0] &&
        v1[0] * v2[2] == v1[2] * v2[0] &&
        v1[1] * v2[2] == v1[2] * v2[1])
        return 1;

    return 2;
}

// Function to check collinearity of 3 points
int check_collinear(int pts[3][3]) {
    int v1[3], v2[3];

    // Vector from point 1 to point 2
    for (int i = 0; i < 3; i++)
        v1[i] = pts[1][i] - pts[0][i];

    // Vector from point 1 to point 3
    for (int i = 0; i < 3; i++)
        v2[i] = pts[2][i] - pts[0][i];

    int r = rank_matrix_2x3(v1, v2);
    return (r == 1);
}

