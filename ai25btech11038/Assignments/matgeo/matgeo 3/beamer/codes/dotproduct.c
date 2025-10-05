#include <math.h>

double dotproduct (double n1[], double n2[]){
    double dotpro[3];
    for(int i = 0; i < 2; i++){
        dotpro[i] = n1[i] * n2[i];
    }
    sum = dotpro[0] + dotpro[1] + dotpro[2];
    return sum;
}

double norm(double n[]){
    int a, b = 0;
    for(int i = 0; i < 2; i++){
        b = b + (n[i] * n[i]);
    }
    a = \pow(b, 0.5);
    return a;
}

double cosine(double dotproduct, double norm1, double norm2){
    double a;
    a = dotproduct / (norm1 * norm2)
    return a;
}
