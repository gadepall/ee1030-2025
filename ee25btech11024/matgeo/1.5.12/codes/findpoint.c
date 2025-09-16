#include <stdio.h>

//double is a data type gives more precise decimal values compared to float due to more bytes
//* is a pointer. *px is an adress that points to the no. of type double
void findpoint(double x1, double y1, double x2, double y2, int m, int n, double *px, double*py){
    *px = (m*x2 + n*x1)/(double)(m+n); //m,n defined as int. for m+n to be treated as double we use (double)
    *py = (m*y2 + n*y1)/(double)(m+n);

}
