#include <stdio.h>
#include <math.h>

int main() {
    FILE *fp;
    fp = fopen("axis.dat", "w");   // Open file to write

    if (fp == NULL) {
        printf("Error opening file!\n");
        return 1;
    }

    // Since line makes equal angles with coordinate axes
    // direction cosines are ±1/sqrt(3)
    double val = 1.0 / sqrt(3.0);

    fprintf(fp, "Direction cosines of a line making equal angles with coordinate axes:\n");
    fprintf(fp, "Possible sets are:\n\n");

    // There are 8 possible combinations of signs
    int signs[8][3] = {
        { 1,  1,  1},
        { 1,  1, -1},
        { 1, -1,  1},
        { 1, -1, -1},
        {-1,  1,  1},
        {-1,  1, -1},
        {-1, -1,  1},
        {-1, -1, -1}
    };

    for (int i = 0; i < 8; i++) {
        fprintf(fp, "(%.4f, %.4f, %.4f)\n",
                signs[i][0] * val,
                signs[i][1] * val,
                signs[i][2] * val);
    }

    fclose(fp);
    printf("Direction cosines written to axis.dat successfully.\n");
    return 0;
}

