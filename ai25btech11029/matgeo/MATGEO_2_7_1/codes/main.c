#include <stdio.h>
#include "triangle.h"

int main() {
    double OA[3] = {1, 2, 3};
    double OB[3] = {-3, 1, 1};

    double area = triangle_area(OA, OB);
    printf("Area of triangle OAB: %.4f\n", area);

    return 0;
}

