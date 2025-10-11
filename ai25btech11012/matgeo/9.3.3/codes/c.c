#include <math.h>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <unistd.h>
#include <sys/socket.h>
#include <netinet/in.h>

// Function for line y = (3/2)x + 6
double line(double x) {
    return 1.5*x + 6.0;
}

// Function for parabola y = (3/4)x^2
double parabola(double x) {
    return 0.75*x*x;
}

// Function for integrand (line - parabola)
double f(double x) {
    return line(x) - parabola(x);
}

// Numerical integration using trapezoidal rule
double integrate(double a, double b, int n) {
    double h = (b - a) / n;
    double sum = 0.5 * (f(a) + f(b));
    for(int i = 1; i < n; i++) {
        sum += f(a + i*h);
    }
    return sum * h;
}

int main() {
    double a = -2.0, b = 4.0;
    int n = 100000; // large n for accuracy
    double area = integrate(a, b, n);
    FILE*file;
    file = fopen("values.dat", "w");

    fprintf(file,"Area enclosed = %.6f\n", area);
     fclose(file);
	printf("Results have been written to values.dat\n");

    return 0;
}

