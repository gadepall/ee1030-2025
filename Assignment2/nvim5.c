#include <stdio.h>
#include <math.h>

int main() {
    double result;

    result = (pow(2, 20) / pow(2, 15)) * pow(2, 3);

    printf("Result = %.0lf\n", result);  
    return 0;
}