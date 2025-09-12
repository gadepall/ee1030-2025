#include<stdio.h>
#include<math.h>

#define DIST(p,q) sqrt( ((p[0]-q[0])*(p[0]-q[0])) + \
                        ((p[1]-q[1])*(p[1]-q[1])) + \
                        ((p[2]-q[2])*(p[2]-q[2])) )
int main()
{
    int A[3] = {2,3,5}, B[3] = {4,3,1};
    int C[3] = {-3,7,2}, D[3] = {2,4,-1};
    int E[3] = {-1,3,-4}, F[3] = {1,-3,4};
    int G[3] = {2,-1,3}, H[3] = {-2,1,3};
    printf("AB = %.3f\n", DIST(A,B));
    printf("CD = %.3f\n", DIST(C,D));
    printf("EF = %.3f\n", DIST(E,F));
    printf("GH = %.3f\n", DIST(G,H));

    return 0;
}