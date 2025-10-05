#include <stdio.h>

// Function to multiply matrix and vector
void mat_vec_mult(double mat[2][2], double vec[2], double result[2]) {
    for (int i = 0; i < 2; ++i) {
        result[i] = 0;
        for (int j = 0; j < 2; ++j) {
            result[i] += mat[i][j] * vec[j];
        }
    }
}

// Solves the equation X = A_inv * B where A_inv is the inverse of the given matrix
void find_points(double x_vals[2], double y_vals[2], double points[2][2]) {
    // Inverse of given matrix A [[3, 1], [5, 2]] is [[2, -1], [-5, 3]]
    double inv[2][2] = {{2, -1}, {-5, 3}};
    for (int i = 0; i < 2; ++i) {
        double b[2] = {x_vals[i], y_vals[i]};
        double res[2];
        mat_vec_mult(inv, b, res);
        points[i][0] = res[0];
        points[i][1] = res[1];
    }
}

// Main just prints out by default
int main() {
    double x_vals[2] = {1, 4}; // Example points on x
    double y_vals[2] = {1, 4}; // Example points on y
    double points[2][2];
    find_points(x_vals, y_vals, points);
    for (int i = 0; i < 2; ++i) {
        printf("%lf %lf\n", points[i][0], points[i][1]);
    }
    return 0;
}

