
double calculate_y(double x, double a, double b, double c) {
    if (b == 0) {
        // Avoid division by zero for vertical lines
        return 0.0; 
    }
    return (c - a * x) / b;
}
