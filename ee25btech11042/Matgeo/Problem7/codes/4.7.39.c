#include <math.h>

/*
  This C function is designed to interface with NumPy arrays.
  It takes a pointer to a double array for input and output.
*/
void calculate_distance_from_xaxis(
    double* input_P,        // Pointer to a 2-element array [Px, Py]
    double* output_distance // Pointer to a 1-element array to be filled
) {
    // Unpack the y-coordinate from the input point
    double Py = input_P[1];

    // The distance is the absolute value of the y-coordinate
    double distance = fabs(Py);

    // Fill the output array with the calculated distance
    output_distance[0] = distance;
}
