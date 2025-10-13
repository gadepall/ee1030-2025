#include <stdio.h>

// Define a simple structure for a 2D point
// This structure must match the one defined in the Python script
typedef struct {
    double x;
    double y;
} Point;

// This function calculates the coordinates of A, B, and the dividing point P.
// It accepts a pointer to an array of 3 Points (allocated in Python) and fills it.
void get_points(Point* points_out) {
    // --- Mathematical Calculation ---
    Point A = {3.0, 2.0};
    Point B = {5.0, 1.0};
    Point P;

    double m = 1.0;
    double n = 2.0;

    // Calculate coordinates of P using the section formula
    P.x = (m * B.x + n * A.x) / (m + n);
    P.y = (m * B.y + n * A.y) / (m + n);
    
    // Fill the output array
    points_out[0] = A;
    points_out[1] = B;
    points_out[2] = P;
}

// This function generates a specified number of points for the line 3x - 18y + 19 = 0.
// It accepts a pointer to an array of Points (allocated in Python) and fills it.
void generate_line_points(Point* line_points_out, int num_points) {
    double k = 19.0;
    double x_start = 0.0;
    double x_end = 6.0;
    double step = (x_end - x_start) / (num_points - 1);

    for (int i = 0; i < num_points; i++) {
        double x_val = x_start + i * step;
        // y = (3x + k) / 18
        double y_val = (3.0 * x_val + k) / 18.0;
        line_points_out[i].x = x_val;
        line_points_out[i].y = y_val;
    }
}
