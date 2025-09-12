#include <stdio.h>

// Function to compute rank of 2x2 integer matrix using arrays
int rank_matrix(int row1[2], int row2[2]) {
    // Both rows zero → rank 0
    if ((row1[0] == 0 && row1[1] == 0) && (row2[0] == 0 && row2[1] == 0))
        return 0;

    // One row zero → rank 1
    if ((row1[0] == 0 && row1[1] == 0) || (row2[0] == 0 && row2[1] == 0))
        return 1;

    // Check proportionality
    if (row1[0] * row2[1] == row1[1] * row2[0])
        return 1;  // dependent → rank 1

    return 2;  // independent → rank 2
}
