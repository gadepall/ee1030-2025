#include <stdio.h>

void solveByMatrix(float *x, float *y)
{
    float a[2][3] = {
        {1, 10, 105},
        {1, 15, 155}
    };

    float ratio;

    // Eliminate x from second row
    ratio = a[1][0] / a[0][0];
    for (int j = 0; j < 3; j++)
        a[1][j] = a[1][j] - ratio * a[0][j];

    // Solve
    *y = a[1][2] / a[1][1];
    *x = (a[0][2] - a[0][1] * (*y)) / a[0][0];
}

