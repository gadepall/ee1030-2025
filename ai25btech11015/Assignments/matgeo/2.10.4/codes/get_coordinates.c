
#include <stdio.h>

int main() {
	int arr1[3] = {1, -1, 2};
	int arr2[3] = {2, 0, -1};
	int arr3[3] = {3, -1, 2};
	FILE *fp = fopen("var.dat", "w");
	if (fp == NULL) {
		printf("Error opening file!\n");
		return 1;
	}
	for (int i = 0; i < 3; i++) fprintf(fp, "%d%c", arr1[i], i < 2 ? ' ' : '\n');
	for (int i = 0; i < 3; i++) fprintf(fp, "%d%c", arr2[i], i < 2 ? ' ' : '\n');
	for (int i = 0; i < 3; i++) fprintf(fp, "%d%c", arr3[i], i < 2 ? ' ' : '\n');
	fclose(fp);
	return 0;
}
