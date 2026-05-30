#include <stdio.h>

void main()
{
    int n,b,d,c=0,sum=0;
    printf("enter the number");
    scanf("%d",&n);
    while(n>0){
        b=n%10;
        sum=sum+b;
        c=c*10;
        c=c+b;
        n=n/10;
        d=sum+c;

        }
    printf("the sum of the number is:%d",sum);
    printf("\nthe reverse of the number is:%d",c);
    printf("\nthe sum of reverse and the number is:%d",d);
    
}