#include <stdio.h>
#include <math.h>


// Function to calculate the unit vector.
// It takes an input vector, its size, and an output array for the result.
void calculate_unit_vector_c(double *vector, int size, double *unit_vector_out) {
    double magnitude = 0.0;
    int i;

    // Calculate the magnitude of the vector
    for (i = 0; i < size; i++) {
        magnitude += vector[i] * vector[i];
    }
    magnitude = sqrt(magnitude);

    // To avoid division by zero, if magnitude is 0, return a zero vector.
    if (magnitude == 0) {
        for (i = 0; i < size; i++) {
            unit_vector_out[i] = 0.0;
        }
    } else {
        // Calculate the unit vector
        for (i = 0; i < size; i++) {
            unit_vector_out[i] = vector[i] / magnitude;
        }
    }
}


