#ifndef LINE_SOLVER_H
#define LINE_SOLVER_H

typedef struct {
    double a;
    double b;
    double c;
} LineEquation;

// Returns the line equation ax + by + c = 0 for a horizontal line through (x, y)
LineEquation get_horizontal_line_through_point(double x, double y);

// Prints the line equation in readable form
void print_line_equation(LineEquation line);

#endif

