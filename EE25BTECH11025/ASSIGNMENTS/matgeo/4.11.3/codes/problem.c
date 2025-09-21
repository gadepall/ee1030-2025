#include <stdio.h>

int lpoint1[3] = {2, -1, 2};
int lpoint2[3] = {5, 3, 4};
int ppoint[3][4] = {{2, 0, 3, 1}, {1,1,5,1}, {3,2,4,1}};

int get_lpoint1(int index){
    return lpoint1[index];
}

int get_lpoint2(int index){
    return lpoint2[index];
}

int get_ppoint(int index1, int index2){
    return ppoint[index1][index2];
}


