#include<stdio.h>
int main()
{
    int n,i,sum=0,a;
    printf("enter total numbers");
    scanf("%d",&a);
    for(i=1;i<=a;i++){
        printf("\nenter the numbers to add");
        scanf("%d",&n);
        sum=sum+n;
    }
    printf("\nsum is %d",sum);
    return 0;
}