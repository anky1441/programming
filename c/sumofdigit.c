/*#include <stdio.h>

void main()
{
    int X1,Y1,X2,Y2,X3,Y3,Z=234,sum=0;
    X1=Z/10;
    Y1=Z%10;
    X2=X1/10;
    Y2=X1%10;
    X3=X2/10;
    Y3=X2%10;
    sum=Y1+Y2+Y3;
    printf("the sum of the digits of number is %d",sum);

}*/
//sum of n digit of integer by using loops
#include <stdio.h>

void main()
{
    int a,ld,c,sum=0;
    printf("enter the number");
    scanf("%d",&a);
    while(a!=0){
    c=a/10;
    ld=a%10;
    sum=sum+ld;
    a=c;
}
printf("the sum of the digits of the integers is %d",sum);
}
