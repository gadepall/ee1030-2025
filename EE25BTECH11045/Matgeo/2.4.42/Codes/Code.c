 #include <stdio.h>
int main() {
    int A[3] = {1, 2, 3};
    int B[3] = {-1, -2, -1};
    int C[3] = {2, 3, 2};
    int D[3] = {4, 7, 6};
    int AB[3], DC[3], AD[3], BC[3];
    // Calculate vectors
    for (int i = 0; i < 3; i++) {
        AB[i] = B[i] - A[i];
        DC[i] = C[i] - D[i];
        AD[i] = D[i] - A[i];
        BC[i] = C[i] - B[i];
    }
    
 // Check parallelogram
    int isPara = 1;
    
    for (int i = 0; i < 3; i++) {
        if (AB[i] != DC[i] || AD[i] != BC[i]) {
            isPara = 0;
            break;
        }
    }
    if (isPara) {
        printf("ABCD is a parallelogram.\n");
        // Check rectangle (dot product AB·AD)
        int dot = AB[0]*AD[0] + AB[1]*AD[1] + AB[2]*AD[2];
        if (dot == 0)
            printf("It is also a rectangle.\n");
        else
            printf("It is not a rectangle.\n");
    } else {
        printf("ABCD is not a parallelogram.\n");
    }
   return 0;
}
