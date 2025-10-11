#include <stdio.h>

void Gaussian(double A[3], double B[3], double sol[2]) {
    // If A[0] == 0, swap rows to avoid division by zero
    //Also covers the case where the matrix is diagonal.
    if (A[0] == 0) {
        for (int i = 0; i < 3; i++) {
            double temp = A[i];
            A[i] = B[i];
            B[i] = temp;
        }
    }

    //the case of two same column elements being zero is meaningless because it yields two equations in one variable, for which gaussian elimination is not required.
   
    double factor = B[0] / A[0];
    for (int i = 0; i < 3; i++) {
        B[i] = B[i] - factor * A[i];
    }

    sol[1] = B[2] / B[1];
    sol[0] = (A[2] - A[1] * sol[1]) / A[0];
}
