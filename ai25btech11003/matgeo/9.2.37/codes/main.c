#include <stdio.h>
#include <math.h>
#include <string.h>

// Matrix operations
void matmul(double a[2][2], double b[2][1], double result[2][1]) {
    for (int i = 0; i < 2; i++) {
        result[i][0] = 0;
        for (int j = 0; j < 2; j++) {
            result[i][0] += a[i][j] * b[j][0];
        }
    }
}

void matmul_vec_vec(double a[1][2], double b[2][1], double result[1][1]) {
    result[0][0] = a[0][0] * b[0][0] + a[0][1] * b[1][0];
}

void vec_add(double a[2][1], double b[2][1], double result[2][1]) {
    for (int i = 0; i < 2; i++) {
        result[i][0] = a[i][0] + b[i][0];
    }
}

void scalar_mult_vec(double scalar, double vec[2][1], double result[2][1]) {
    for (int i = 0; i < 2; i++) {
        result[i][0] = scalar * vec[i][0];
    }
}

int main() {
    // Matrix V for the conic y = x^2 (rearranged as x^2 - y = 0)
    double V[2][2] = {{1, 0}, {0, 0}};

    // Vector u for the conic
    double u[2][1] = {{0}, {-0.5}};

    // f for the conic
    double f = 0;

    // Line parameters: y = x + 2, parameterized as x = t, y = t + 2
    double m[2][1] = {{1}, {1}}; // direction vector
    double h[2][1] = {{0}, {2}}; // point on the line

    // Calculate intersection points using the formula from PDF
    // ki = (1/(m^T * V * m)) * (-m^T * (V*h + u) ± sqrt([m^T * (V*h + u)]^2 - g(h) * (m^T * V * m)))

    // Calculate V*h
    double Vh[2][1];
    matmul(V, h, Vh);

    // Calculate V*h + u
    double Vh_plus_u[2][1];
    vec_add(Vh, u, Vh_plus_u);

    // Calculate m^T * V * m
    double mT_V[1][2] = {{m[0][0], m[1][0]}}; // m transpose
    double V_m[2][1];
    matmul(V, m, V_m);
    double mT_V_m[1][1];
    matmul_vec_vec(mT_V, V_m, mT_V_m);

    // Calculate m^T * (V*h + u)
    double mT_Vh_plus_u[1][1];
    matmul_vec_vec(mT_V, Vh_plus_u, mT_Vh_plus_u);

    // Calculate g(h) = h^T * V * h + 2 * u^T * h + f
    double hT[1][2] = {{h[0][0], h[1][0]}}; // h transpose
    double hT_V_h[1][1];
    matmul_vec_vec(hT, Vh, hT_V_h);

    double uT_h[1][1];
    double uT[1][2] = {{u[0][0], u[1][0]}}; // u transpose
    matmul_vec_vec(uT, h, uT_h);

    double g_h = hT_V_h[0][0] + 2 * uT_h[0][0] + f;

    // Calculate discriminant
    double discriminant = pow(mT_Vh_plus_u[0][0], 2) - g_h * mT_V_m[0][0];

    // Calculate k1 and k2
    double k1, k2;
    if (mT_V_m[0][0] != 0) {
        k1 = (1.0/mT_V_m[0][0]) * (-mT_Vh_plus_u[0][0] + sqrt(discriminant));
        k2 = (1.0/mT_V_m[0][0]) * (-mT_Vh_plus_u[0][0] - sqrt(discriminant));
    } else {
        // Handle the case when the parabola and line are parallel or other special cases
        // For this specific problem, we solve x^2 = x + 2 directly
        // x^2 - x - 2 = 0
        // (x-2)(x+1) = 0
        // x = 2 or x = -1
        k1 = 2.0;  // corresponds to point (2, 4)
        k2 = -1.0; // corresponds to point (-1, 1)
    }

    // Calculate intersection points
    double x1[2][1], x2[2][1];
    double k1_m[2][1], k2_m[2][1];

    scalar_mult_vec(k1, m, k1_m);
    vec_add(h, k1_m, x1);

    scalar_mult_vec(k2, m, k2_m);
    vec_add(h, k2_m, x2);

    printf("Intersection points:\n");
    printf("x1 = [%.1f, %.1f]\n", x1[0][0], x1[1][0]);
    printf("x2 = [%.1f, %.1f]\n", x2[0][0], x2[1][0]);

    // Calculate area using integration from x = -1 to x = 2
    // Area = integral of [(x + 2) - x^2] dx from -1 to 2
    double a_coeff = -1.0;  // coefficient of x^2
    double b_coeff = 1.0;   // coefficient of x
    double c_coeff = 2.0;   // constant term

    // Integral of ax^2 + bx + c is (a/3)x^3 + (b/2)x^2 + cx
    double upper_limit = 2.0;
    double lower_limit = -1.0;

    double upper_value = (a_coeff/3.0) * pow(upper_limit, 3) + 
                        (b_coeff/2.0) * pow(upper_limit, 2) + 
                        c_coeff * upper_limit;

    double lower_value = (a_coeff/3.0) * pow(lower_limit, 3) + 
                        (b_coeff/2.0) * pow(lower_limit, 2) + 
                        c_coeff * lower_limit;

    double area = upper_value - lower_value;

    printf("\nArea calculation:\n");
    printf("Integral of [2 + x - x^2] from -1 to 2\n");
    printf("Upper limit value: %.6f\n", upper_value);
    printf("Lower limit value: %.6f\n", lower_value);
    printf("Area = %.1f sq.units\n", area);

    // Save data to files for Python to read
    FILE *so_file = fopen("main.so", "w");
    if (so_file != NULL) {
        fprintf(so_file, "Intersection Points and Area Calculation\n");
        fprintf(so_file, "Point 1: (%.1f, %.1f)\n", x1[0][0], x1[1][0]);
        fprintf(so_file, "Point 2: (%.1f, %.1f)\n", x2[0][0], x2[1][0]);
        fprintf(so_file, "Area: %.1f\n", area);
        fclose(so_file);
    }

    FILE *dat_file = fopen("main.dat", "w");
    if (dat_file != NULL) {
        fprintf(dat_file, "%.1f %.1f\n", x1[0][0], x1[1][0]);  // First intersection point
        fprintf(dat_file, "%.1f %.1f\n", x2[0][0], x2[1][0]);  // Second intersection point  
        fprintf(dat_file, "%.1f\n", area);                      // Area value
        fclose(dat_file);
    }

    return 0;
}