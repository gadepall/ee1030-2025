typedef struct {
    double a;
    double b;
} Solution;

Solution solve_equations(double a1, double b1, double c1, double a2, double b2, double c2) {
    Solution sol;
    double determinant = a1 * b2 - a2 * b1;

    // Use Cramer's rule to find 'a' and 'b'
    if (determinant != 0) {
        sol.a = (c1 * b2 - c2 * b1) / determinant;
        sol.b = (a1 * c2 - a2 * c1) / determinant;
    } else {
        // Fallback for singular matrix
        sol.a = 0.0;
        sol.b = 0.0;
    }
    return sol;
}
