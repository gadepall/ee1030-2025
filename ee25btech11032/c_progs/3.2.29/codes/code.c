//Code by Kartik Lahoti
//13 August 2025
//Check if given rational is negative for not - 3.2.29
#include <stdio.h>

int main(void)
{
    float ratio , temp1 , temp2 ;
    printf("Aim : To check if entered rational number is neagtive or not \n");
    printf("Enter the numberator and denominator for the rational (e.x. : 3/(-5)) : ");
    scanf("%f %f",&temp1,&temp2);

    if (temp2 != 0 )
    {
        ratio = temp1 / temp2 ;
        if (ratio < 0 )
        {
            printf("Given rational %f is negative ",ratio);
        }
        else
        {
            printf("Given rational %f not is negative",ratio);
        }
    }
    else
    {
        printf("Denominator Cannot be ZERO !");
    }
    return 0 ;
}
