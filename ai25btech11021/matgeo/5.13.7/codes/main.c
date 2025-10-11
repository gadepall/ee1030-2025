#include <stdio.h>

int main() {
    // Define two 3x3 matrices A and B
    int A[3][3] = {{1,2,3},{4,5,6},{7,8,9}};
    int B[3][3] = {{9,8,7},{6,5,4},{3,2,1}};
    int AB[3][3], ABt[3][3], BtAt[3][3], i, j, k;

    // Compute AB = A * B
    for(i=0;i<3;i++){
        for(j=0;j<3;j++){
            AB[i][j]=0;
            for(k=0;k<3;k++){
                AB[i][j]+=A[i][k]*B[k][j];
            }
        }
    }

    // Compute transpose of AB
    for(i=0;i<3;i++){
        for(j=0;j<3;j++){
            ABt[i][j]=AB[j][i];
        }
    }

    // Compute transpose of A and B
    int At[3][3], Bt[3][3];
    for(i=0;i<3;i++){
        for(j=0;j<3;j++){
            At[i][j]=A[j][i];
            Bt[i][j]=B[j][i];
        }
    }

    // Compute BtAt = B^T * A^T
    for(i=0;i<3;i++){
        for(j=0;j<3;j++){
            BtAt[i][j]=0;
            for(k=0;k<3;k++){
                BtAt[i][j]+=Bt[i][k]*At[k][j];
            }
        }
    }

    // Print (AB)^T
    printf("Transpose of AB:\n");
    for(i=0;i<3;i++){
        for(j=0;j<3;j++){
            printf("%d ",ABt[i][j]);
        }
        printf("\n");
    }

    // Print B^T A^T
    printf("Product B^T A^T:\n");
    for(i=0;i<3;i++){
        for(j=0;j<3;j++){
            printf("%d ",BtAt[i][j]);
        }
        printf("\n");
    }
    return 0;
}
