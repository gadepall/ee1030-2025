#include <stdio.h>

// Function to compute determinant of a 3x3 matrix
double det3(double m[3][3]) {
    return m[0][0]*(m[1][1]*m[2][2] - m[1][2]*m[2][1])
         - m[0][1]*(m[1][0]*m[2][2] - m[1][2]*m[2][0])
         + m[0][2]*(m[1][0]*m[2][1] - m[1][1]*m[2][0]);
}

// Function to solve the system using Cramer's rule
// solution[0] -> x, solution[1] -> y, solution[2] -> z
void solve_system(double *solution) {
    double a[3][3] = {
        {2, 3, 3},
        {1, -2, 1},
        {3, -1, -2}
    };
    double b[3] = {5, -4, 3};

    double m[3][3];

    // Determinant of coefficient matrix
    double detA = det3(a);

    if(detA == 0) {
        solution[0] = solution[1] = solution[2] = 0.0;
        return;
    }

    // Dx (replace 1st column with b)
    for(int i=0;i<3;i++) for(int j=0;j<3;j++) m[i][j]=a[i][j];
    for(int i=0;i<3;i++) m[i][0] = b[i];
    double detX = det3(m);

    // Dy (replace 2nd column with b)
    for(int i=0;i<3;i++) for(int j=0;j<3;j++) m[i][j]=a[i][j];
    for(int i=0;i<3;i++) m[i][1] = b[i];
    double detY = det3(m);

    // Dz (replace 3rd column with b)
    for(int i=0;i<3;i++) for(int j=0;j<3;j++) m[i][j]=a[i][j];
    for(int i=0;i<3;i++) m[i][2] = b[i];
    double detZ = det3(m);

    solution[0] = detX / detA;
    solution[1] = detY / detA;
    solution[2] = detZ / detA;
}

// Optional main function (for direct C execution)
// This will be ignored when creating shared object
int main() {
    double solution[3];
    solve_system(solution);

    printf("Solution:\n");
    printf("x = %lf\n", solution[0]);
    printf("y = %lf\n", solution[1]);
    printf("z = %lf\n", solution[2]);

    return 0;
}

