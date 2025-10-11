#include <stdio.h>
#include <stdlib.h>

// For part (a), we need to avoid double-counting matrices that are both
// symmetric and skew-symmetric (like the zero matrix). A simple 3D array
// can act as a "seen" set for the small primes we are testing.
int ***create_seen_array(int size) {
    int ***arr = (int ***)malloc(size * sizeof(int **));
    for (int i = 0; i < size; i++) {
        arr[i] = (int **)malloc(size * sizeof(int *));
        for (int j = 0; j < size; j++) {
            // calloc initializes memory to zero
            arr[i][j] = (int *)calloc(size, sizeof(int));
        }
    }
    return arr;
}

void free_seen_array(int ***arr, int size) {
    for (int i = 0; i < size; i++) {
        for (int j = 0; j < size; j++) {
            free(arr[i][j]);
        }
        free(arr[i]);
    }
    free(arr);
}

// Function to solve part (a): Symmetric OR Skew-Symmetric with det(A) = 0
// The __attribute__ makes sure the function is visible in the shared library.
__attribute__((visibility("default")))
int solve_part_a(int p) {
    int count = 0;
    int ***seen = create_seen_array(p);

    for (int a = 0; a < p; a++) {
        for (int b = 0; b < p; b++) {
            for (int c = 0; c < p; c++) {
                // Check determinant condition: a^2 - bc divisible by p
                if ((a * a - b * c) % p == 0) {
                    int is_symmetric = (c == b);
                    // In C, (-b) % p can be negative, so we ensure a positive result
                    int is_skew_symmetric = (a == 0 && c == (p - b) % p);
                    
                    if (is_symmetric || is_skew_symmetric) {
                        if (seen[a][b][c] == 0) {
                            seen[a][b][c] = 1; // Mark this matrix as seen
                            count++;
                        }
                    }
                }
            }
        }
    }
    free_seen_array(seen, p);
    return count;
}

// Function to solve part (b): tr(A) != 0 AND det(A) = 0
__attribute__((visibility("default")))
int solve_part_b(int p) {
    int count = 0;
    for (int a = 0; a < p; a++) {
        for (int b = 0; b < p; b++) {
            for (int c = 0; c < p; c++) {
                // Trace (2a) is not zero => a is not zero (since p is odd)
                int trace_ok = (a != 0);
                // Determinant is zero
                int det_ok = ((a * a - b * c) % p == 0);
                if (trace_ok && det_ok) {
                    count++;
                }
            }
        }
    }
    return count;
}

// Function to solve part (c): det(A) != 0
__attribute__((visibility("default")))
int solve_part_c(int p) {
    int count = 0;
    for (int a = 0; a < p; a++) {
        for (int b = 0; b < p; b++) {
            for (int c = 0; c < p; c++) {
                if ((a * a - b * c) % p != 0) {
                    count++;
                }
            }
        }
    }
    return count;
}


