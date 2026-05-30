#include <stdio.h>
void main()
{
    int i,a,b,c=1;
    printf("enter the base");
    scanf("%d",&a);
    printf("enter the power");
    scanf("%d",&b);
    printf("the value of each power is:");
    for(i=1;i<=b;i++){
        c=c*a;
        printf("%d,",c);
    }
    printf("\nthe value of %d^%d is %d",a,b,c);
}