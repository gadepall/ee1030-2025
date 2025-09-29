#include <stdio.h>

#define size 2

double n[size], v1[size], v2[size], v3[size], v4[size], v5[size];

void insert_vector(int index, double vec[size]){
    double *target;
    switch (index){
        case 0: target = n; break;
        case 1: target = v1; break;
        case 2: target = v2; break;
        case 3: target = v3; break;
        case 4: target = v4; break;
        case 5: target = v5; break;
    }
    for (int i=0; i<size; i++){
        target[i] = vec[i];
    }
}

double* get_vector(int index){
    switch (index){
        case 0: return n;
        case 1: return v1;
        case 2: return v2;
        case 3: return v3;
        case 4: return v4;
        case 5: return v5;
        default: return NULL;
    }
}
