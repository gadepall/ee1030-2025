#include<stdio.h>

struct Vec2{
		float x,y;
};


int dotVec2(struct Vec2 v1,struct Vec2 v2){
		//struct Vec2 v;
		return v1.x*v2.x+v1.y*v2.y;
}
