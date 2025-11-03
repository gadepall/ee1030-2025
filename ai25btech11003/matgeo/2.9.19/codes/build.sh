#!/bin/bash

echo "====================================="
echo "Vector Problem Solution - Fixed Build"
echo "====================================="

# Check if libs directory exists
if [ ! -d "libs" ]; then
    echo "Error: libs directory not found!"
    echo "Please make sure geofun.h and matfun.h are in the libs/ directory"
    exit 1
fi

# Check if header files exist
if [ ! -f "libs/geofun.h" ] || [ ! -f "libs/matfun.h" ]; then
    echo "Error: Header files not found in libs/ directory!"
    echo "Please ensure libs/geofun.h and libs/matfun.h exist"
    exit 1
fi

# Create a combined source file that includes the necessary implementations
echo "Creating combined source file..."

cat > combined_vector_solution.c << 'EOF'
#include <stdio.h>
#include <stdlib.h>
#include <math.h>

// Essential function implementations (to avoid redefinition errors)
void freeMat(double **matrix, int rows) {
    if (matrix == NULL) return;
    for (int i = 0; i < rows; ++i) {
        free(matrix[i]);
    }
    free(matrix);
}

double **createMat(int m, int n) {
    double **matrix = (double **)malloc(m * sizeof(double *));
    for (int i = 0; i < m; i++) {
        matrix[i] = (double *)malloc(n * sizeof(double));
        for (int j = 0; j < n; j++) {
            matrix[i][j] = 0.0;
        }
    }
    return matrix;
}

void printMat(double **p, int m, int n) {
    for (int i = 0; i < m; i++) {
        for (int j = 0; j < n; j++) {
            printf("%.6f ", p[i][j]);
        }
        printf("\n");
    }
}

double Matnorm(double **a, int m) {
    double sum = 0.0;
    for (int i = 0; i < m; i++) {
        sum += a[i][0] * a[i][0];
    }
    return sqrt(sum);
}

double Matdot(double **a, double **b, int m) {
    double sum = 0.0;
    for (int i = 0; i < m; i++) {
        sum += a[i][0] * b[i][0];
    }
    return sum;
}

double **Matadd(double **a, double **b, int m, int n) {
    double **c = createMat(m, n);
    for (int i = 0; i < m; i++) {
        for (int j = 0; j < n; j++) {
            c[i][j] = a[i][j] + b[i][j];
        }
    }
    return c;
}

double **Matscale(double **a, int m, int n, double k) {
    double **c = createMat(m, n);
    for (int i = 0; i < m; i++) {
        for (int j = 0; j < n; j++) {
            c[i][j] = k * a[i][j];
        }
    }
    return c;
}

// Problem-specific functions
void saveVectorsToFile(double **a, double **b, double **c, double **result, const char *filename) {
    FILE *fp = fopen(filename, "w");
    if (fp == NULL) {
        printf("Error opening file!\n");
        return;
    }
    
    fprintf(fp, "# Vector data for the problem\n");
    fprintf(fp, "# Format: vector_name x y z\n");
    fprintf(fp, "a %.6f %.6f %.6f\n", a[0][0], a[1][0], a[2][0]);
    fprintf(fp, "b %.6f %.6f %.6f\n", b[0][0], b[1][0], b[2][0]);
    fprintf(fp, "c %.6f %.6f %.6f\n", c[0][0], c[1][0], c[2][0]);
    fprintf(fp, "result %.6f %.6f %.6f\n", result[0][0], result[1][0], result[2][0]);
    fprintf(fp, "# Magnitude of result vector: %.6f\n", Matnorm(result, 3));
    
    fclose(fp);
}

double **computeResult(double **a, double **b, double **c) {
    double **scaled_a = Matscale(a, 3, 1, 3.0);
    double **scaled_b = Matscale(b, 3, 1, -2.0);
    double **scaled_c = Matscale(c, 3, 1, 2.0);
    
    double **temp = Matadd(scaled_a, scaled_b, 3, 1);
    double **result = Matadd(temp, scaled_c, 3, 1);
    
    freeMat(scaled_a, 3);
    freeMat(scaled_b, 3);
    freeMat(scaled_c, 3);
    freeMat(temp, 3);
    
    return result;
}

// Function exported for Python to use
double compute_vector_magnitude(double *a, double *b, double *c) {
    double **vec_a = createMat(3, 1);
    double **vec_b = createMat(3, 1);
    double **vec_c = createMat(3, 1);
    
    for (int i = 0; i < 3; i++) {
        vec_a[i][0] = a[i];
        vec_b[i][0] = b[i];
        vec_c[i][0] = c[i];
    }
    
    double **result = computeResult(vec_a, vec_b, vec_c);
    double magnitude = Matnorm(result, 3);
    
    freeMat(vec_a, 3);
    freeMat(vec_b, 3);
    freeMat(vec_c, 3);
    freeMat(result, 3);
    
    return magnitude;
}

int main() {
    printf("Solving: Find |3a - 2b + 2c| where |a|=1, |b|=2, |c|=3\n");
    printf("Conditions: proj_a(b) = proj_a(c) and b ⊥ c\n\n");
    
    // Create vectors that satisfy the given conditions
    double **a = createMat(3, 1);
    a[0][0] = 1.0; a[1][0] = 0.0; a[2][0] = 0.0;
    
    // Choose k = 0.5 for the projection value
    double k = 0.5;
    
    // b = (k, sqrt(4-k²), 0)
    double **b = createMat(3, 1);
    b[0][0] = k;
    b[1][0] = sqrt(4 - k*k);
    b[2][0] = 0.0;
    
    // c = (k, m, n) where b·c = 0 and |c| = 3
    double **c = createMat(3, 1);
    c[0][0] = k;
    c[1][0] = -k*k / sqrt(4 - k*k);  // m = -k²/sqrt(4-k²)
    
    // Calculate n such that |c| = 3
    double m = c[1][0];
    double n_squared = 9 - k*k - m*m;
    c[2][0] = sqrt(n_squared);
    
    printf("Vector a: ");
    printMat(a, 3, 1);
    printf("Magnitude of a: %.6f\n\n", Matnorm(a, 3));
    
    printf("Vector b: ");
    printMat(b, 3, 1);
    printf("Magnitude of b: %.6f\n\n", Matnorm(b, 3));
    
    printf("Vector c: ");
    printMat(c, 3, 1);
    printf("Magnitude of c: %.6f\n\n", Matnorm(c, 3));
    
    // Verify conditions
    printf("Verification of conditions:\n");
    double proj_b = Matdot(b, a, 3);
    double proj_c = Matdot(c, a, 3);
    double dot_bc = Matdot(b, c, 3);
    
    printf("b·a = %.6f\n", proj_b);
    printf("c·a = %.6f\n", proj_c);
    printf("b·c = %.6f\n", dot_bc);
    printf("Equal projections: %s\n", (fabs(proj_b - proj_c) < 1e-10) ? "Yes" : "No");
    printf("Perpendicular: %s\n", (fabs(dot_bc) < 1e-6) ? "Yes" : "No");
    printf("\n");
    
    // Compute 3a - 2b + 2c
    double **result = computeResult(a, b, c);
    
    printf("Result vector (3a - 2b + 2c): ");
    printMat(result, 3, 1);
    
    double magnitude = Matnorm(result, 3);
    printf("Magnitude |3a - 2b + 2c| = %.6f\n", magnitude);
    printf("Theoretical value = sqrt(61) = %.6f\n", sqrt(61));
    printf("Error: %.10f\n\n", fabs(magnitude - sqrt(61)));
    
    // Save vectors to file
    saveVectorsToFile(a, b, c, result, "vectors.dat");
    printf("Vectors saved to vectors.dat\n");
    
    // Clean up
    freeMat(a, 3);
    freeMat(b, 3);
    freeMat(c, 3);
    freeMat(result, 3);
    
    return 0;
}
EOF

# Compile the executable
echo "Compiling executable..."
gcc -o vector_solution combined_vector_solution.c -lm
if [ $? -ne 0 ]; then
    echo "Error: Failed to compile executable"
    exit 1
fi

# Compile the shared library
echo "Creating shared library..."
gcc -fPIC -shared -o vectors.so combined_vector_solution.c -lm
if [ $? -ne 0 ]; then
    echo "Error: Failed to create shared library"
    exit 1
fi

# Run the program
echo "Running the program..."
./vector_solution
if [ $? -ne 0 ]; then
    echo "Error: Program execution failed"
    exit 1
fi

echo ""
echo "Build completed successfully!"
echo "Files created:"
echo "  - vector_solution (executable)"
echo "  - vectors.so (shared library)"
echo "  - vectors.dat (vector data)"
echo "  - combined_vector_solution.c (source)"
echo ""
echo "You can now run the Python analysis:"
echo "  python3 vector_analysis.py"