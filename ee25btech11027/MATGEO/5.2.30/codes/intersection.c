
#include <stdio.h>

void solve_system(double a1, double b1, double c1, double a2, double b2, double c2, double *x_sol, double *y_sol) {
    // Calculate the determinant of the coefficient matrix
    double determinant = a1 * b2 - a2 * b1;
    
    // Check for a unique solution
    if (determinant != 0) {
        *x_sol = (c1 * b2 - c2 * b1) / determinant;
        *y_sol = (a1 * c2 - a2 * c1) / determinant;
    } else {
        // Handle the case of no unique solution (parallel or coincident lines)
        // For this problem, we assume a unique solution exists.
        *x_sol = 0.0;
        *y_sol = 0.0;
    }
}

// Main function for standalone testing in C
int main() {
    double x, y;
    
    // Solve: 7x - 15y = 2 and x + 2y = 3
    solve_system(7.0, -15.0, 2.0, 1.0, 2.0, 3.0, &x, &y);
    
    printf("Solution from C:\n");
    printf("x = %f\n", x);
    printf("y = %f\n", y);
    
    return 0;
}
