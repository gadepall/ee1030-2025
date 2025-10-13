#include <stdio.h>
#include <math.h>

/*
   Program to find the area of the region:
   S = { (x, y): x^2 + y^2 <= 16a^2 and y^2 <= 6ax }

   We compute:
   A = 2 * [ ∫_0^{2a} sqrt(6ax) dx + ∫_{2a}^{4a} sqrt(16a^2 - x^2) dx ]
   using Simpson's 1/3 rule (numerical integration).
*/

// Function for the parabola y = sqrt(6*a*x)
double parabola(double x, double a) {
    return sqrt(6.0 * a * x);
}

// Function for the circle y = sqrt(16*a^2 - x^2)
double circle(double x, double a) {
    return sqrt(16.0 * a * a - x * x);
}

// Simpson’s rule for integration
double simpson(double (*f)(double, double), double a, double x0, double x1, int n) {
    double h = (x1 - x0) / n;
    double sum = f(x0, a) + f(x1, a);
    for (int i = 1; i < n; i++) {
        double x = x0 + i * h;
        if (i % 2 == 0)
            sum += 2 * f(x, a);
        else
            sum += 4 * f(x, a);
    }
    return (h / 3.0) * sum;
}

int main() {
    double a;
    printf("Enter the value of a: ");
    scanf("%lf", &a);

    int n = 10000; // number of subintervals for Simpson’s rule (even)

    // Integrate sqrt(6ax) from 0 to 2a
    double area1 = simpson(parabola, a, 0, 2 * a, n);

    // Integrate sqrt(16a^2 - x^2) from 2a to 4a
    double area2 = simpson(circle, a, 2 * a, 4 * a, n);

    // Total area (both above and below x-axis)
    double total_area = 2 * (area1 + area2);

    // Display results
    printf("\n--- Step-by-Step Integration Process ---\n");
    printf("Parabola: y = sqrt(6ax)\n");
    printf("Circle:   y = sqrt(16a^2 - x^2)\n");
    printf("Intersection point: (2a, 2√3 a)\n");

    printf("\nIntegrating in first quadrant:\n");
    printf("Area1 = ∫[0 to 2a] sqrt(6ax) dx = %.6lf\n", area1);
    printf("Area2 = ∫[2a to 4a] sqrt(16a^2 - x^2) dx = %.6lf\n", area2);

    printf("\nTotal Area (both halves): A = 2*(Area1 + Area2)\n");
    printf("=> Area = %.6lf\n", total_area);

    return 0;
}

