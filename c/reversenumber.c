#include <stdio.h>
void main()
{
    int n,b,c=0;
    printf("enter the number");
    scanf("%d",&n);
    while(n>0){
        b=n%10;
        c=c*10;
        c=c+b;
        n=n/10;
    }
    printf("reverse of the number is %d",c);
}