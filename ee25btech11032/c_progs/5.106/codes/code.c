// 5.66
#include <stdio.h>
#include <math.h>

int main(void)
{
    float num1,num2,num3 , pow1,pow2 ,pow3 ;
    printf("Enter Fiirst number base (Ex: 2^3) and its power : ");
    scanf("%f %f",&num1,&pow1);
    printf("Enter Second number base (Ex: 3^2) and its power : ");
    scanf("%f %f",&num2,&pow2);
    printf("Enter THE PRODUCT base numberand its power : ");
    scanf("%f %f",&num3,&pow3);
    if (!(num1==0 && pow1==0) && !(num2 == 0 && pow2 == 0) && !(num3 == 0 && pow3 == 0) )
    {
        if ( pow(num1,pow1) * pow(num2,pow2) == pow(num3,pow3) )
        {
            printf("%.2f^%.2f x %.2f^%.2f = %.2f^%.2f is TRUE!",num1,pow1,num2,pow2,num3,pow3);
        }
        else
        {
            printf("%.2f^%.2f x %.2f^%.2f = %.2f^%.2f is FALSE!",num1,pow1,num2,pow2,num3,pow3);
        }
    }
    else
    {
        printf("0^O IS NOT DEFINED!");
    }
    return 0 ;
}
