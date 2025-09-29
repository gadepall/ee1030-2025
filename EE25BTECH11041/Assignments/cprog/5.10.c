#include <stdio.h>

//5.10
/*question: find the value of the following expression for x =2:
 a. 19-5x^2
 b. 100 -10x^3
 */
void fun(int x){
int a,b;
a = 19-5*x*x;
b = 100-10*x*x*x;
printf("a. %d \n", a); //19-5x^2
printf("b. %d", b); //100-10x^3

}

int main(){
int x =2;
fun(x);
return 0;
}
