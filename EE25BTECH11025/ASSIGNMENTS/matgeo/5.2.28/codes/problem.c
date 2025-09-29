#include<stdio.h>

double x = -24/5;
double y = -3/5;
double coefficient_mat[2][2] = {{5,-8},{3,-4.8}};
double constant[2][1] = {{-1}, {-0.6}};

double get_item(int i, int j){
    return coefficient_mat[i][j];
}
double get_constant(int i, int j){
    return constant[i][j];
}

