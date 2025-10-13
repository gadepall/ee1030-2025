#include <stddef.h> // For size_t

/**
 * @brief Performs the operation: dest_row = dest_row + (factor * src_row)
 * This is the core operation for elimination.
 * @param dest_row The row to be modified.
 * @param src_row The row used for the operation.
 * @param factor The multiplication factor.
 * @param size The number of elements in the rows.
 */
void add_scaled_row(double* dest_row, const double* src_row, double factor, size_t size) {
    for (size_t i = 0; i < size; i++) {
        dest_row[i] += factor * src_row[i];
    }
}

/**
 * @brief Scales a row by multiplying each element by a factor.
 * Used for normalization (making pivots equal to 1).
 * @param row The row to be scaled.
 * @param factor The scaling factor.
 * @param size The number of elements in the row.
 */
void scale_row(double* row, double factor, size_t size) {
    for (size_t i = 0; i < size; i++) {
        row[i] *= factor;
    }
}
