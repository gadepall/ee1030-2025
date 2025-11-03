#include <stdio.h>
#include <math.h>

// Function to calculate the cross product of two 3D vectors.
// Inputs: components of vector A (ax, ay, az) and vector B (bx, by, bz).
// Outputs: components of the result vector R (*rx, *ry, *rz).
void cross_product(double ax, double ay, double az,
                    double bx, double by, double bz,
                    double *rx, double *ry, double *rz) {
    *rx = ay * bz - az * by;
    *ry = az * bx - ax * bz;
    *rz = ax * by - ay * bx;
}

// Function to calculate the dot product of two 3D vectors.
// Inputs: components of vector A (ax, ay, az) and vector B (bx, by, bz).
// Returns: the scalar dot product.
double dot_product(double ax, double ay, double az,
                    double bx, double by, double bz) {
    return ax * bx + ay * by + az * bz;
}

// Helper function to calculate a term of the form (V1 x V2) x (V3 x V4).
// Inputs: components of four vectors (v1, v2, v3, v4).
// Outputs: components of the result vector R (*term_rx, *term_ry, *term_rz).
void calculate_vector_quad_cross(
    double v1x, double v1y, double v1z,
    double v2x, double v2y, double v2z,
    double v3x, double v3y, double v3z,
    double v4x, double v4y, double v4z,
    double *term_rx, double *term_ry, double *term_rz) {

    // Calculate V1 x V2
    double v1xv2_x, v1xv2_y, v1xv2_z;
    cross_product(v1x, v1y, v1z, v2x, v2y, v2z, &v1xv2_x, &v1xv2_y, &v1xv2_z);

    // Calculate V3 x V4
    double v3xv4_x, v3xv4_y, v3xv4_z;
    cross_product(v3x, v3y, v3z, v4x, v4y, v4z, &v3xv4_x, &v3xv4_y, &v3xv4_z);

    // Calculate (V1 x V2) x (V3 x V4)
    cross_product(v1xv2_x, v1xv2_y, v1xv2_z, v3xv4_x, v3xv4_y, v3xv4_z,
                  term_rx, term_ry, term_rz);
}


// Main function to calculate the full expression:
// (a × b) × (c × d) + (a × c) × (d × b) + (a × d) × (b × c)
// Inputs: components of vectors a, b, c, d.
// Outputs: components of the final sum vector (*result_x, *result_y, *result_z).
void calculate_full_expression(
    double ax, double ay, double az,
    double bx, double by, double bz,
    double cx, double cy, double cz,
    double dx, double dy, double dz,
    double *result_x, double *result_y, double *result_z) {

    // Components for each of the three terms
    double term1_x, term1_y, term1_z;
    double term2_x, term2_y, term2_z;
    double term3_x, term3_y, term3_z;

    // Term 1: (a x b) x (c x d)
    calculate_vector_quad_cross(ax, ay, az, bx, by, bz,
                                cx, cy, cz, dx, dy, dz,
                                &term1_x, &term1_y, &term1_z);

    // Term 2: (a x c) x (d x b)
    calculate_vector_quad_cross(ax, ay, az, cx, cy, cz,
                                dx, dy, dz, bx, by, bz,
                                &term2_x, &term2_y, &term2_z);

    // Term 3: (a x d) x (b x c)
    calculate_vector_quad_cross(ax, ay, az, dx, dy, dz,
                                bx, by, bz, cx, cy, cz,
                                &term3_x, &term3_y, &term3_z);

    // Sum the terms
    *result_x = term1_x + term2_x + term3_x;
    *result_y = term1_y + term2_y + term3_y;
    *result_z = term1_z + term2_z + term3_z;
}

// Function to check if three vectors are coplanar (scalar triple product is zero).
// Inputs: components of vectors B, C, D.
// Returns: the scalar triple product (B . (C x D)).
double scalar_triple_product(double bx, double by, double bz,
                             double cx, double cy, double cz,
                             double dx, double dy, double dz) {
    double cxd_x, cxd_y, cxd_z;
    cross_product(cx, cy, cz, dx, dy, dz, &cxd_x, &cxd_y, &cxd_z);
    return dot_product(bx, by, bz, cxd_x, cxd_y, cxd_z);
}