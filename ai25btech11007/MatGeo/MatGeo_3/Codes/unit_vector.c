#include <stdio.h>

// Custom sqrt function using Newton-Raphson method
double my_sqrt(double x) {
    if (x <= 0) return 0;
    double guess = x;
    double epsilon = 1e-9; // tolerance
    while (1) {
        double new_guess = 0.5 * (guess + x / guess);
        if ( (guess - new_guess < epsilon) && (new_guess - guess < epsilon) )
            break;
        guess = new_guess;
    }
    return guess;
}

int main() {
    // Define the vectors a and b
    double a[3] = {1, -7, 7};
    double b[3] = {3, -2, 2};
    double n[3];   // cross product result
    double magnitude;
    double unit[3];

    // Compute cross product n = a × b
    n[0] = a[1]*b[2] - a[2]*b[1]; // i-component
    n[1] = a[2]*b[0] - a[0]*b[2]; // j-component
    n[2] = a[0]*b[1] - a[1]*b[0]; // k-component

    // Compute magnitude of n using custom sqrt
    magnitude = my_sqrt(n[0]*n[0] + n[1]*n[1] + n[2]*n[2]);

    // Compute unit vector
    unit[0] = n[0] / magnitude;
    unit[1] = n[1] / magnitude;
    unit[2] = n[2] / magnitude;

    // Print formatted results
    printf("================= Results =================\n\n");

    printf("Vector a: ( %6.2f, %6.2f, %6.2f )\n", a[0], a[1], a[2]);
    printf("Vector b: ( %6.2f, %6.2f, %6.2f )\n\n", b[0], b[1], b[2]);

    printf("Cross product (a × b): ( %6.2f, %6.2f, %6.2f )\n\n", n[0], n[1], n[2]);

    printf("Magnitude of cross product: %.2f\n\n", magnitude);

    printf("Unit vector perpendicular to a and b:\n");
    printf("( %6.2f, %6.2f, %6.2f )\n\n", unit[0], unit[1], unit[2]);

    printf("===========================================\n");

    return 0;
}

