#include <stdio.h>

// This function will be called from Python.
// It takes three integer values as arguments.
void process_point(int x, int y, int z) {
    // Print a confirmation message to the console.
    printf("✅ C function received point: (%d, %d, %d)\n", x, y, z);
}
