#include <math.h>
#include <stdio.h>
#include <stdlib.h>
#include <stdio.h>

int main() {
    int A[3][3] = {{7, -3, -3},
                   {-1,  1,  0},
                   {-1,  0,  1}};
                   
    int B[3][3] = {{1, 3, 3},
                   {1, 4, 3},   // λ = 4
                   {1, 3, 4}};
                   
    int C[3][3] = {0};
    
    // Multiply A and B
    for(int i=0; i<3; i++) {
        for(int j=0; j<3; j++) {
            for(int k=0; k<3; k++) {
                C[i][j] += A[i][k] * B[k][j];
            }
        }
    }
    
    

    FILE*file;
	    file = fopen("values.dat","w");
	    fprintf(file,"%d",C[1][1]);
	    fclose(file);
	    printf("Results have been written to values.dat\n");
    return 0;
}

