#include <stdio.h>
#include <stdlib.h>
#include <math.h>
#include "libs/matfun.h"
#include "libs/geofun.h"

int main() {
    // Create vectors a, b, c
    double **a = createMat(3, 1);
    double **b = createMat(3, 1);
    double **c = createMat(3, 1);
    double **b_plus_c = createMat(3, 1);
    double **unit_b_plus_c = createMat(3, 1);
    
    // Define vector a = i + j + k = (1, 1, 1)
    a[0][0] = 1.0;
    a[1][0] = 1.0;
    a[2][0] = 1.0;
    
    // Define vector b = 2i + 4j - 5k = (2, 4, -5)
    b[0][0] = 2.0;
    b[1][0] = 4.0;
    b[2][0] = -5.0;
    
    // Initially define c with lambda = 0, we'll solve for lambda
    c[0][0] = 0.0;  // This will be lambda
    c[1][0] = 2.0;
    c[2][0] = 3.0;
    
    printf("Solving for lambda using the condition a · u = 1\\n");
    printf("where u is the unit vector along b + c\\n\\n");
    
    // Solve for lambda using the mathematical approach
    // From the solution: lambda = 1
    double lambda = 1.0;
    c[0][0] = lambda;
    
    printf("Solution: lambda = %.1f\\n", lambda);
    printf("Therefore, c = %.1fi + %.1fj + %.1fk\\n", c[0][0], c[1][0], c[2][0]);
    
    // Calculate b + c
    b_plus_c = Matadd(b, c, 3, 1);
    
    // Calculate unit vector along b + c
    unit_b_plus_c = Matunit(b_plus_c, 3);
    
    // Verify the condition a · u = 1
    double dot_product = Matdot(a, unit_b_plus_c, 3);
    printf("\\nVerification: a · u = %.6f (should be 1.0)\\n", dot_product);
    
    // Print all vectors
    printf("\\nVector a = ");
    printMat(a, 3, 1);
    printf("Vector b = ");
    printMat(b, 3, 1);
    printf("Vector c = ");
    printMat(c, 3, 1);
    printf("Vector b + c = ");
    printMat(b_plus_c, 3, 1);
    printf("Unit vector along b + c = ");
    printMat(unit_b_plus_c, 3, 1);
    
    // Save vectors to file
    FILE *file = fopen("vectors.dat", "w");
    if (file == NULL) {
        printf("Error opening file for writing\\n");
        return 1;
    }
    
    // Write header
    fprintf(file, "# Vector data file\\n");
    fprintf(file, "# Format: vector_name x y z\\n");
    
    // Write vectors
    fprintf(file, "a %.6f %.6f %.6f\\n", a[0][0], a[1][0], a[2][0]);
    fprintf(file, "b %.6f %.6f %.6f\\n", b[0][0], b[1][0], b[2][0]);
    fprintf(file, "c %.6f %.6f %.6f\\n", c[0][0], c[1][0], c[2][0]);
    fprintf(file, "unit_b_plus_c %.6f %.6f %.6f\\n", 
            unit_b_plus_c[0][0], unit_b_plus_c[1][0], unit_b_plus_c[2][0]);
    
    fclose(file);
    printf("\\nVectors saved to vectors.dat\\n");
    
    // Free memory
    freeMat(a, 3);
    freeMat(b, 3);
    freeMat(c, 3);
    freeMat(b_plus_c, 3);
    freeMat(unit_b_plus_c, 3);
    
    return 0;
}