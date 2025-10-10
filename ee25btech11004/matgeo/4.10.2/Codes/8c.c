#include<stdio.h>
#include<math.h>

float matmul (int array10, int array11, int array20, int array21 ){
    
    int multi = array20*array10 + array11*array21;
    
    int distance = multi/sqrt(29);
    
    return distance;

}
