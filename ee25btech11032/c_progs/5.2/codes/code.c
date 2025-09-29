// Code by kartik
// Determain that a triangle with side 3cm, 4cm and 5cm is a
// right angled triangle
#include <stdio.h>
#include <math.h>

int main(void)
{
    int side1 , side2 , side3 ;
    printf("Enter integral side lengths of a triangle with 3rd input length as hypotenuse (if rt angled triangle) : ");
    scanf("%d %d %d",&side1,&side2,&side3);
    if(side1 != 0 && side2 != 0 && side3 !=0 )
    {
        if ( (side1 + side2) > side3 && (side2 + side3) > side1 && (side1+side3) > side2)
        {
            if (pow(side1,2) + pow(side2,2) == pow(side3,2))
            {
                printf("Given Triangle follows pythagoras theorem hence its right angled triangle.");
            }
            else
            {
                printf("Given Triangle does not follow pythagoras theorem hence its not a right angled triangle.");
            }
        }
        else
        {
            printf("Given lengths cannot form a Triangle!");
        }
    }
    else
    {
        printf("Side Length Cannot be zero!");
    }
    return 0 ;
}
