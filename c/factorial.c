#include <stdio.h>
void main()
{
    int n,i,fact=1;
    printf("enter the number to find factorial");
    scanf("%d",&n);
    for (i=1;i<=n;i++){
        fact=fact*i;
        printf("\nthe factorial of %d is: %d",i,fact);
    }
    printf("\n1the factorial of %d is %d",n,fact);
}