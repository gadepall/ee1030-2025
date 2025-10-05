// code.c
// Compile with: gcc -shared -fPIC -o points.so code.c

void tangent_points(double* pts) {
    // Store two points of tangency (x1, y1, x2, y2)
    pts[0] = 4.0;
    pts[1] = -2.0;
    pts[2] = 2.0;
    pts[3] = 2.0;
}

