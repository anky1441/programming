#include<stdio.h>
int product(int a, int b){
    return a*b;
}
int main()
{
    int x,y;
printf("enter the first number");
scanf("%d",&x);
printf("enter the second number");
scanf("%d",&y);
printf("%d",product(x,y));
return 0;
}
