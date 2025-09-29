#include <stdio.h>

typedef struct {
    double x;
    double y;
    double z;
} Vector3;

double dotProduct(Vector3 a, Vector3 b) {
    return a.x * b.x + a.y * b.y + a.z * b.z;
}

void computePlaneEquation(double n1[3], double d1, double n2[3], double d2, double n3[3], double d3, double result[4]) {
    Vector3 vec_n1 = {n1[0], n1[1], n1[2]};
    Vector3 vec_n2 = {n2[0], n2[1], n2[2]};
    Vector3 vec_n3 = {n3[0], n3[1], n3[2]};

    double n3_dot_n1 = dotProduct(vec_n3, vec_n1);  // Should be -7
    double n3_dot_n2 = dotProduct(vec_n3, vec_n2);  // Should be 19

    if (n3_dot_n2 == 0) {
        printf("Error: Division by zero.\n");
        result[0] = result[1] = result[2] = result[3] = 0;
        return;
    }

    double lambda = -n3_dot_n1 / n3_dot_n2;  // Should be 7/19 ≈ 0.3684210526

    result[0] = vec_n1.x + lambda * vec_n2.x;  // 33/19 ≈ 1.7368421
    result[1] = vec_n1.y + lambda * vec_n2.y;  // 45/19 ≈ 2.3684211
    result[2] = vec_n1.z + lambda * vec_n2.z;  // 50/19 ≈ 2.6315789
    result[3] = d1 + lambda * d2;              // -41/19 ≈ -2.1578947
}

