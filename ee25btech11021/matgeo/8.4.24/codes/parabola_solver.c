#include <stdio.h>
#include <math.h>

// Generate points of parabola y^2 - kx + 8 = 0
void generate_parabola_points(double k, double x_start, double x_end, int n_points,
                              double *X, double *Y) {
    double step = (x_end - x_start) / (n_points - 1);
    for(int i = 0; i < n_points; i++){
        double x = x_start + i*step;
        double y_sq = k*x - 8;  // y^2 = kx - 8
        if (y_sq >= 0) {
            X[i] = x; Y[i] = sqrt(y_sq);           // positive branch
            X[i + n_points] = x; Y[i + n_points] = -sqrt(y_sq); // negative branch
        } else {
            X[i] = X[i + n_points] = x;
            Y[i] = Y[i + n_points] = 0; // skip imaginary
        }
    }
}

// Solve for k using matrix method formulas
double solve_k_matrix() {
    double f_target = 8;
    double temp = f_target + 1;  // f = ||F||^2 - 1 => (1 + k/2)^2 = 9
    double k1 = 2*(sqrt(temp) - 1);
    double k2 = 2*(-sqrt(temp) - 1);
    printf("Possible values of k: %f , %f\n", k1, k2);
    return k1; // return first value
}

