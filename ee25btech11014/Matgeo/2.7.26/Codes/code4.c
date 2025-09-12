#include <stdio.h>
#include <math.h>

// Function to calculate area of quadrilateral using shoelace formula
float quadArea(int x[], int y[], int n) {
    float area = 0.0;
    int i, j;

    for (i = 0; i < n; i++) {
        j = (i + 1) % n;  // Next vertex index
        area += (x[i] * y[j]) - (y[i] * x[j]);
    }

    return fabs(area) / 2.0;
}

// Expose function for Python
float findQuadArea(int x1, int y1, int x2, int y2,
                   int x3, int y3, int x4, int y4) {
    int x[4] = {x1, x2, x3, x4};
    int y[4] = {y1, y2, y3, y4};
    return quadArea(x, y, 4);
}
