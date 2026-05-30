#include<stdio.h>
void main()
{
    int a;
    printf("enter number a:");
    scanf("%d",&a);
    for (int i=1;i<=a;i++){
        for (int j=1;j<=a;j++){
            printf("%d ",j);
        }
        printf("\n");
    }
}