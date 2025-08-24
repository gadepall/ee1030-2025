
#include<stdio.h>

void profitorloss(int cp, int sp){
	if(cp>sp){
		printf("Loss = %d",cp-sp);
	}
	else{
		printf("Profit = %d",sp-cp);
	}
}

void percent(float cp, float sp){
	if(cp>sp){
		printf("and Loss percent = %f %%",(cp-sp)/cp*100);
	}
	else{
		printf("and Profit percent = %f %%",(sp-cp)/cp*100);
	}
}

int main(){
	printf("Case1\n");
	profitorloss(250,325);
	percent(250,325);
	printf("\nCase2\n");
	profitorloss(12000,13500);
	percent(12000,13500);
	printf("\nCase3\n");
	profitorloss(2500,3000);
	percent(2500,3000);
	printf("\nCase4\n");
	profitorloss(250,150);
	percent(250,150);
	return 0;
}



