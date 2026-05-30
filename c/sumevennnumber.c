/*#include <stdio.h>

void main()
{
    int a,b,sum=0;
    printf("enter the number");
    scanf("%d",&a);
    while(a!=0){
    b=a%10;
    if(b%2==0){
        sum=sum+b;
    }
    a=a/10;
}
    printf("the sum of the even digit is %d",sum);
}*/
#include <stdio.h>

void main()
{
    int a,b,sum=0;
    printf("enter the number");
    scanf("%d",&a);
    while(a!=0){
    b=a%10;
    if(b%2!=0){
        sum=sum+b;
    }
    a=a/10;
}
    printf("the sum of the odd digit is %d",sum);
}