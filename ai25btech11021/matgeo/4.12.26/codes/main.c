#include <stdio.h>
#include <math.h>

int verify_locus(double x, double y, double c) {
    double lhs = (x * x) + (y * y);
    double rhs = c * c;
    double tolerance = 1e-9; 
    
    if (fabs(lhs - rhs) < tolerance) {
        return 1;
    } else {
        return 0;
    }
}

int main() {
    double constant_c = 5.0;

    double x1 = 3.0;
    double y1 = 4.0;
    
    if (verify_locus(x1, y1, constant_c)) {
        printf("Point (%.2f, %.2f) IS on the locus x^2 + y^2 = %.2f\n", 
               x1, y1, constant_c * constant_c);
    } else {
        printf("Point (%.2f, %.2f) is NOT on the locus.\n", x1, y1);
    }

    double x2 = 1.0;
    double y2 = 1.0;

    if (verify_locus(x2, y2, constant_c)) {
        printf("Point (%.2f, %.2f) IS on the locus x^2 + y^2 = %.2f\n", 
               x2, y2, constant_c * constant_c);
    } else {
        printf("Point (%.2f, %.2f) is NOT on the locus x^2 + y^2 = %.2f\n", 
               x2, y2, constant_c * constant_c);
    }

    return 0;
}