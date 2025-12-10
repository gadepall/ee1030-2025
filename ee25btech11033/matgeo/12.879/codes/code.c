double find_optimal_x(double* a, double* b, int size) {
    double a_dot_a = 0.0;
    double a_dot_b = 0.0;
    
    // Calculate the dot products
    for (int i = 0; i < size; i++) {
        a_dot_a += a[i] * a[i];
        a_dot_b += a[i] * b[i];
    }
    
    // Avoid division by zero if a is the zero vector
    if (a_dot_a == 0) {
        return 0.0;
    }
    
    return a_dot_b / a_dot_a;
}
