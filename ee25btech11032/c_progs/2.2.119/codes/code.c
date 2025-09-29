//Code By Kartik Lahoti
//13 August, 2025
//Division of rational by integer 2.2.119

#include <stdio.h>

int main(void){
    int a ;
    float ratio , temp1,temp2 ;
    printf("Division by negative rational by integer : \n");
    printf("Enter a negative numerator (EX : -3) and a positive denominator (EX : 5) : ");
    scanf("%f %f",&temp1,&temp2);
    if (temp2!= 0 )
    {
        ratio = temp1 / temp2 ;
        printf("Enter a Integer (EX : 2) : ");
        scanf("%d",&a);
        if( a != 0 )
            printf("The result for %f divided by %d = %f ",ratio,a,ratio/a);
        else
            printf("DIVSION BY ZERO IS NOT POSSIBLE!");
    }
    else
    {
        printf("Denominator cannot be ZERO !");
    }
    return 0;
}
