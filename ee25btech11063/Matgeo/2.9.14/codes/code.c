#include <stdio.h>
#include <math.h>

/* magnitude of a 3D vector */
double magnitude(const double v[3]) {
    return sqrt(v[0]*v[0] + v[1]*v[1] + v[2]*v[2]);
}

/* normalize a 3D vector into unit; if zero vector, sets unit to 0,0,0 */
void normalize(const double v[3], double unit[3]) {
    double mag = magnitude(v);
    if (mag == 0.0) {
        unit[0] = unit[1] = unit[2] = 0.0;
        return;
    }
    unit[0] = v[0] / mag;
    unit[1] = v[1] / mag;
    unit[2] = v[2] / mag;
}

int main(void) {
    FILE *fp = fopen("plgm.dat", "w");
    if (fp == NULL) {
        perror("fopen");
        return 1;
    }

    /* Given adjacent sides */
    double a[3] = {2.0, 4.0, -5.0};
    double b[3] = {1.0, 2.0, 3.0};

    /* Diagonals */
    double d1[3], d2[3];
    for (int i = 0; i < 3; ++i) {
        d1[i] = a[i] + b[i]; /* first diagonal */
        d2[i] = a[i] - b[i]; /* second diagonal */
    }

    /* Unit vectors parallel to diagonals */
    double u1[3], u2[3];
    normalize(d1, u1);
    normalize(d2, u2);

    /* Cross product of diagonals and area = 0.5 * |d1 x d2| */
    double cross[3];
    cross[0] = d1[1]*d2[2] - d1[2]*d2[1];
    cross[1] = d1[2]*d2[0] - d1[0]*d2[2];
    cross[2] = d1[0]*d2[1] - d1[1]*d2[0];
    double area = 0.5 * magnitude(cross);

    /* Write results to plgm.dat */
    fprintf(fp, "Adjacent sides:\n");
    fprintf(fp, "a = (%.2f, %.2f, %.2f)\n", a[0], a[1], a[2]);
    fprintf(fp, "b = (%.2f, %.2f, %.2f)\n\n", b[0], b[1], b[2]);

    fprintf(fp, "Diagonals:\n");
    fprintf(fp, "d1 = (%.2f, %.2f, %.2f)\n", d1[0], d1[1], d1[2]);
    fprintf(fp, "d2 = (%.2f, %.2f, %.2f)\n\n", d2[0], d2[1], d2[2]);

    fprintf(fp, "Unit vectors parallel to diagonals:\n");
    fprintf(fp, "u1 = (%.6f, %.6f, %.6f)\n", u1[0], u1[1], u1[2]);
    fprintf(fp, "u2 = (%.6f, %.6f, %.6f)\n\n", u2[0], u2[1], u2[2]);

    fprintf(fp, "Area of parallelogram = %.6f\n", area);

    fclose(fp);

    printf("plgm.dat written successfully.\n");
    return 0;
}

