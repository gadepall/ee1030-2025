#include <stdio.h>
#include <math.h>

// Function to compute b given a·b and a×b
void find_b(double *b) {
    // Given vector a = (1,1,1)
    double a[3] = {1, 1, 1};
    double dot = 1; // a·b
    double cross[3] = {0, 1, -1}; // a×b = j - k

    // We solve using conditions:
    // b = (x,y,z)
    // a·b = x+y+z = 1
    // a×b = (z-y, x-z, y-x) = (0,1,-1)

    // From equations: z-y=0 -> z=y
    // x-z=1 -> x=y+1
    // y-x=-1 -> consistent
    // x+y+z=1 -> (y+1)+y+y=1 -> 3y+1=1 -> y=0 -> x=1, z=0

    b[0] = 1; // x
    b[1] = 0; // y
    b[2] = 0; // z
}

int main() {
    double b[3];
    find_b(b);

    FILE *file = fopen("values.dat", "w");
    if(file == NULL) {
        printf("Error opening file!\n");
        return 1;
    }

    fprintf(file, "b_x\tb_y\tb_z\n");
    fprintf(file, "%.2lf\t%.2lf\t%.2lf\n", b[0], b[1], b[2]);
    fclose(file);

    printf("Vector b written to values.dat: (%.2lf, %.2lf, %.2lf)\n", b[0], b[1], b[2]);
    return 0;
}
