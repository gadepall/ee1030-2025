#include <stdio.h>

// Function to compute normal vector for line through A(3,1) and B(9,3)
void get_normal_vector(double *n1, double *n2) {
    int x1 = 3, y1 = 1;
    int x2 = 9, y2 = 3;

    // Normal vector = [y2-y1, -(x2-x1)]
    *n1 = y2 - y1;    // 3 - 1 = 2
    *n2 = -(x2 - x1); // -(9 - 3) = -6
}

int main() {
    double n1, n2;
    get_normal_vector(&n1, &n2);
    printf("Normal vector: n1=%lf, n2=%lf\n", n1, n2);
    return 0;
}

