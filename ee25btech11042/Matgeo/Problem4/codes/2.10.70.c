/*
  This C function is designed to interface with NumPy arrays.
  It takes pointers to double arrays for input and output.
*/
void calculate_points_from_arrays(
    double* input_A,      // Pointer to a 2-element array [Ax, Ay]
    double* input_B,      // Pointer to a 2-element array [Bx, By]
    double* input_C,      // Pointer to a 2-element array [Cx, Cy]
    double* output_points // Pointer to a 12-element array to be filled
) {
    // Unpack input points for clarity
    double Ax = input_A[0], Ay = input_A[1];
    double Bx = input_B[0], By = input_B[1];
    double Cx = input_C[0], Cy = input_C[1];

    // Calculate Point D
    double Dx = (1.0 * Bx + 2.0 * Cx) / 3.0;
    double Dy = (1.0 * By + 2.0 * Cy) / 3.0;

    // Calculate Point E
    double Ex = (1.0 * Ax + 3.0 * Cx) / 4.0;
    double Ey = (1.0 * Ay + 3.0 * Cy) / 4.0;

    // Calculate Point P
    double mu = 8.0 / 11.0;
    double Px = (1.0 - mu) * Bx + mu * Ex;
    double Py = (1.0 - mu) * By + mu * Ey;

    // Fill the output array (12 elements: Ax, Ay, Bx, By, ...)
    output_points[0] = Ax; output_points[1] = Ay;
    output_points[2] = Bx; output_points[3] = By;
    output_points[4] = Cx; output_points[5] = Cy;
    output_points[6] = Dx; output_points[7] = Dy;
    output_points[8] = Ex; output_points[9] = Ey;
    output_points[10] = Px; output_points[11] = Py;
}
