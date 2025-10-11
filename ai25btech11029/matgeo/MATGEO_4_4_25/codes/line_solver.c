#include "line_solver.h"
#include <stdio.h>

LineEquation get_horizontal_line_through_point(double x, double y) {
    LineEquation line;
    line.a = 0.0;
    line.b = 1.0;
    line.c = -y;
    return line;
}

void print_line_equation(LineEquation line) {
    printf("The line equation is: %.2fx + %.2fy + %.2f = 0\n", line.a, line.b, line.c);
}

