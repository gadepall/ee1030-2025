#include <stdio.h>

void print_mat(float a[][3]);
void inverse(float a[3][3])
{
    float iden[3][3];
    for (int i = 0; i < 3; i++)
    {
        for (int j = 0; j < 3; j++)
        {
            iden[i][j] = (i == j) ? 1.0f : 0.0f;
        }
    }

    float pivot = a[0][0], val;
    for (int i = 0; i < 3; i++) // First row first element becoming 1, identity mat first row divided by a11
    {
        a[0][i] /= pivot;
        iden[0][i] /= pivot;
    }

    val = a[1][0];
    for (int i = 0; i < 3; i++) // a21 becoming 0 and the changes are reflected in iden
    {
        a[1][i] -= (val * a[0][i]);
        iden[1][i] -= (val * iden[0][i]);
    }
    val = a[2][0];
    for (int i = 0; i < 3; i++) // a31 becoming 0 and the changes are reflected in iden
    {
        a[2][i] -= (val * a[0][i]);
        iden[2][i] -= (val * iden[0][i]);
    }
    pivot = a[1][1];
    for (int i = 0; i < 3; i++) // a22 becomes 1 and changes are reflected
    {
        a[1][i] /= pivot;
        iden[1][i] /= pivot;
    }

    val = a[0][1];
    for (int i = 0; i < 3; i++) // a12 becomes 0
    {
        a[0][i] -= (val * a[1][i]);
        iden[0][i] -= (val * iden[1][i]);
    }

    val = a[2][1];
    for (int i = 0; i < 3; i++) // a32 becomes 0
    {
        a[2][i] -= (val * a[1][i]);
        iden[2][i] -= (val * iden[1][i]);
    }

    pivot = a[2][2];
    for (int i = 0; i < 3; i++) // a33 becomes 1 and changes are reflected
    {
        a[2][i] /= pivot;
        iden[2][i] /= pivot;
    }

    val = a[0][2];
    for (int i = 0; i < 3; i++) // a13 becomes 0
    {
        a[0][i] -= (val * a[2][i]);
        iden[0][i] -= (val * iden[2][i]);
    }

    val = a[1][2];
    for (int i = 0; i < 3; i++) // a23 becomes 0
    {
        a[1][i] -= (val * a[2][i]);
        iden[1][i] -= (val * iden[2][i]);
    }

    for (int i = 0; i < 3; i++)
    {
        for (int j = 0; j < 3; j++)
        {
            a[i][j] = iden[i][j];
        }
    }
    print_mat(a);
    return;
}
void print_mat(float a[][3])
{
    for (int i = 0; i < 3; i++)
    {
        for (int j = 0; j < 3; j++)
        {
            printf("%.2f ", a[i][j]);
        }
        printf("\n");
    }
}
