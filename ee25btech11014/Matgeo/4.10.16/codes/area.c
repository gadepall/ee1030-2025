// area.c
// Function to compute area under y = x + 1 from a to b

double area_under_line(double a, double b) {
    if (a > b) {  // swap if needed
        double t = a;
        a = b;
        b = t;
    }
    return 0.5 * (b*b - a*a) + (b - a);
}
