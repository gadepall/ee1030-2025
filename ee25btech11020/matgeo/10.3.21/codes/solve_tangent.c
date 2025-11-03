#include <stdio.h>

void tangent_point(double *q)
{
    double V[2][2] = {{0, 0}, {0, 1}};
    double u[2] = {-2, 0};
    double h[2] = {0, 1};
    double m[2] = {1, 1};
    double f = 0;

    double mtVm = 0, mtVh = 0, utm = 0, htVh = 0, uth = 0;

    for (int i = 0; i < 2; i++)
        for (int j = 0; j < 2; j++)
            mtVm += m[i] * V[i][j] * m[j];

    for (int i = 0; i < 2; i++)
        for (int j = 0; j < 2; j++)
            mtVh += m[i] * V[i][j] * h[j];

    for (int i = 0; i < 2; i++)
        utm += u[i] * m[i];

    for (int i = 0; i < 2; i++)
        for (int j = 0; j < 2; j++)
            htVh += h[i] * V[i][j] * h[j];

    for (int i = 0; i < 2; i++)
        uth += u[i] * h[i];

    double A = mtVm;
    double B = 2 * (mtVh + utm);
    double C = htVh + 2 * uth + f;

    double D = B * B - 4 * A * C;

    double t = -B / (2 * A); // since D = 0

    q[0] = h[0] + t * m[0];
    q[1] = h[1] + t * m[1];
}

