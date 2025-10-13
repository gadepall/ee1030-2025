#include <stdio.h>

double area_bounded() {
    double y1 = 0, y2 = 3;
    double area;

    // A = ∫[(2y + 3) - y^2] dy from 0 to 3
    area = (y2 * y2 + 3 * y2 - (y2 * y2 * y2) / 3.0) -
           (y1 * y1 + 3 * y1 - (y1 * y1 * y1) / 3.0);

    return area;
}

int main() {
    printf("Area bounded = %.2f\n", area_bounded());
    return 0;
}

