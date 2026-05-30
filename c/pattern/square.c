#include<stdio.h>
void main()
{
    int a,b;
    printf("enter the side");
    scanf("%d",&a);
    for(b=1;b<=a;b++){
        for(int i=1;i<=a;i++){
        printf("*");
     }
        printf("\n");
    }
    
}