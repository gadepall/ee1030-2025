#include <stdio.h>

// Define a structure to hold 3D vector components.
// This structure will be mirrored in the Python script.
typedef struct {
    double x;
    double y;
    double z;
} Vector3D;

/**
 * @brief Calculates the work done by a force moving a particle between two points.
 * * @param force A pointer to the force vector.
 * @param pos_a A pointer to the initial position vector (Point A).
 * @param pos_b A pointer to the final position vector (Point B).
 * @return The calculated work done as a double.
 */
double calculate_work_done(const Vector3D* force, const Vector3D* pos_a, const Vector3D* pos_b) {
    // 1. Calculate the displacement vector (d = B - A)
    Vector3D displacement;
    displacement.x = pos_b->x - pos_a->x;
    displacement.y = pos_b->y - pos_a->y;
    displacement.z = pos_b->z - pos_a->z;

    // 2. Calculate the dot product of Force and Displacement
    double work_done = force->x * displacement.x + 
                       force->y * displacement.y + 
                       force->z * displacement.z;

    return work_done;
}

// A main function is included for standalone testing of the C code.
// This part is not called by Python.
int main() {
    // Define the vectors from the problem
    Vector3D force_P    = {2.0, -5.0, 6.0};
    Vector3D position_A = {6.0, 1.0, -3.0};
    Vector3D position_B = {4.0, -3.0, -2.0};

    // Calculate work done by calling the function
    double work = calculate_work_done(&force_P, &position_A, &position_B);

    // Print the result to the console
    printf("--- Standalone C Execution ---\n");
    printf("Work Done: %f units\n", work);

    return 0;
}

