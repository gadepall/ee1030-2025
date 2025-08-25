#include<stdio.h>
#include<math.h>

double find_magnitude(double *result)
{
	double mag;
	mag=sqrt(pow(result[0],2)+pow(result[1],2)+pow(result[2],2));
	return mag;

}

double find_cross_product(double *a, double *b, double *result)
{
    float A[2][3];
    float x1, x2, x3;
 

    // Build the 2x3 matrix [a; b]
    for(int j = 0; j < 3; j++) {
        A[0][j] = a[j];
        A[1][j] = b[j];
    }

    // Row reduction
    if (fabs(A[0][0]) < 1e-6) {
        for(int j = 0; j < 3; j++) {
            float tmp = A[0][j];
            A[0][j] = A[1][j];
            A[1][j] = tmp;
        }
    }

    float factor = A[1][0] / A[0][0];
    for(int j = 0; j < 3; j++) {
        A[1][j] -= factor * A[0][j];
    }

    // Solve system A * x = 0 with free variable x3 = 1
    x3 = 1;
    if (fabs(A[1][1]) > 1e-6) {
        x2 = -(A[1][2] * x3) / A[1][1];
    } else {
        x2 = 0;
    }
    x1 = -(A[0][1]*x2 + A[0][2]*x3) / A[0][0];

    result[0] = x1;
    result[1] = x2;
    result[2] = x3;

}
