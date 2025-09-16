#include <stdio.h>

// Custom square root function using Newton-Raphson method
double mySqrt(double n) {
    if (n < 0) return -1;   // sqrt not defined for negatives
    if (n == 0 || n == 1) return n;

    double x = n;
    double y = 1.0;
    double eps = 1e-9;  // precision

    while (x - y > eps) {
        x = (x + y) / 2.0;
        y = n / x;
    }
    return x;
}

// Cross product of two 3D vectors
void crossProduct(int a[3], int b[3], int result[3]) {
    result[0] = a[1]*b[2] - a[2]*b[1];
    result[1] = a[2]*b[0] - a[0]*b[2];
    result[2] = a[0]*b[1] - a[1]*b[0];
}

// Magnitude of a vector
double magnitude(int v[3]) {
    return mySqrt(v[0]*v[0] + v[1]*v[1] + v[2]*v[2]);
}

int main() {
    // Given vectors
    int a[3] = {0, 0, 0};          // p = q = r = 0 (from solution)
    int b[3] = {-3, -1, 2};
    int c[3] = {3, 1, -2};

    // Check relation a = b + c
    int check[3] = {b[0] + c[0], b[1] + c[1], b[2] + c[2]};
    printf("Check: a = (%d, %d, %d), b+c = (%d, %d, %d)\n",
            a[0], a[1], a[2], check[0], check[1], check[2]);

    // Compute cross product
    int cross[3];
    crossProduct(b, c, cross);

    // Compute area = 0.5 * |b x c|
    double area = 0.5 * magnitude(cross);

    printf("Cross product (b x c) = (%d, %d, %d)\n",
            cross[0], cross[1], cross[2]);
    printf("Area of triangle = %.2f\n", area);

    // Compare with given area
    printf("Given area = 5*sqrt(6) ≈ %.2f\n", 5*mySqrt(6));

    if (area == 0)
        printf("Conclusion: Triangle is degenerate, no valid solution exists.\n");
    else
        printf("Triangle exists.\n");

    return 0;
}
