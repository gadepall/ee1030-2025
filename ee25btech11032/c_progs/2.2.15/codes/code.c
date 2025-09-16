//Code by Kartik Lahoti
//13 August, 2025
//Multiplication of two rationals using C prog
#include <stdio.h>

int main(void) {
    float temp1, temp2, temp3, temp4, a, b ;
    printf("Enter the numerator and denominator for the rational 2/3 : ");
    scanf("%f %f",&temp1, &temp2);

    printf("Enter the numerator and denominator for the rational 1/5 : ");
    scanf("%f %f",&temp3, &temp4);
    if (temp2 !=0 && temp4 != 0 )
    {
        a = temp1/temp2 ;

        b = temp3/temp4 ;
        printf("The result for 2/3 x 1/5 = %f",a*b);
    }
    else
    {
        printf("Division by ZERO is not defined!");
    }
    return 0 ;

}
